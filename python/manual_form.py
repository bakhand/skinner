#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 15:50:01 2022

@author: ab

to do: pedal log
to do: presses while rotating process (yes)
to do: save as
to do: autodisconnect (yes)
to do: full log
to do: пока приучается пока не проверила кормушку следующее нажатие кормушку не запускает (Автоматич)
to do: пол секунды не нажимать на педаль, чтобы следующее нажатие засчиталось 
to do: блок для фиксирования поведенческих реакций (груминг начало конец, стойки)
to do: пеллета съел не съел

element names
pushButtonMotorOn
pushButtonMotorOff
pushButtonOnePellet
pushButtonLever
pushButtonAuto
pushButtonSave

lcdNumberLever
lcdNumberNosePoke
lcdNumberFood

tableWidget
pushButtonConnect
comboBoxPort



labelState
pushButtonLog
"""

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import Qt

from ui.ui_manual_regime import Ui_Form

import sys


class TestForm(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(TestForm, self).__init__()
        self.setupUi(self)
        #uic.loadUi('ui/manual_regime.ui', self)

        self.comboBoxPort.addItems(
            [port.portName() for port in QSerialPortInfo().availablePorts()])

        self.pushButtonConnect.setCheckable(True)
        self.pushButtonConnect.toggled.connect(self.connectArduino)

        self.port = QSerialPort()
        #self.show()

        self.pushButtonMotorOn.clicked.connect(lambda: self.sendToPort("<11>"))
        self.pushButtonMotorOff.clicked.connect(
            lambda: self.sendToPort("<10>"))
        self.pushButtonOnePellet.clicked.connect(
            lambda: self.sendToPort("<12>"))

        self.pushButtonLever.setCheckable(True)
        self.pushButtonLever.toggled.connect(
            lambda x: self.sendToPort("<01>") if x else self.sendToPort("<00>"))

        self.pushButtonAuto.setCheckable(True)
        self.pushButtonAuto.toggled.connect(
            lambda x: self.sendToPort("<31>") if x else self.sendToPort("<30>"))

        self.pushButtonSave.clicked.connect(self.saveTable)
        self.pushButtonSaveAs.clicked.connect(self.saveTableAs)
       

        self.timer = QtCore.QTimer(self)

        self.recievedString = ""
        self.newMessage = False

        self.lcdNumberLever.setStyleSheet("color: rgb(0,0,0)")
        self.lcdNumberNosePoke.setStyleSheet("color: rgb(0,150,0)")
        self.lcdNumberFood.setStyleSheet("color: rgb(0,0,150)")

        self.lcdNumberLever.setSegmentStyle(2)
        self.lcdNumberNosePoke.setSegmentStyle(2)
        self.lcdNumberFood.setSegmentStyle(2)

        self.tableWidget.setRowCount(0)
        self.save_name = 'out.csv'
        
        self.logger = StateLogger(self)
        self.pushButtonLog.setCheckable(True)
        self.pushButtonLog.toggled.connect(
            lambda x: self.logger.go_active() if x else self.logger.go_passive())
        self.setFocus()
        
    def closeEvent(self, event):
        # here you can terminate your threads and do other stuff

        # and afterwards call the closeEvent of the super-class
        self.timer.stop()
        self.port.close()
        print('Port closed')
        super(TestForm, self).closeEvent(event)

    def getSaveFileName(self):
        nm =  QtWidgets.QFileDialog.getSaveFileName(self, 'Save Lattice', '', "csv (*.csv;;All Files (*)",
                     options=QtWidgets.QFileDialog.DontUseNativeDialog)
        self.save_name = nm[0] + '.' + nm[1].split(' ')[0]
        
    def saveTable(self):
        N = self.tableWidget.rowCount()
        with open(self.save_name, "w") as outfile:
            for i in range(N):
                for j in range(3):
                    text = self.tableWidget.item(i, j).text()
                    print(text, end=",", file=outfile)
                print("", file=outfile)
                
    def saveTableAs(self):
            
            self.getSaveFileName()
            self.saveTable()

    def connectArduino(self, flag=True):
        if flag:
            self.port.setBaudRate(115200)
            self.port.setPortName(self.comboBoxPort.currentText())
            r = self.port.open(QtCore.QIODevice.ReadWrite)

            if not r:
                print('Port open error')
                self.pushButtonConnect.setChecked(False)
            else:
                print('Port opened')
                self.timer.start(100)
                self.timer.timeout.connect(self.recvFromArduino)

        else:
            self.timer.stop()
            self.port.close()
            print('Port closed')

    # def readFromPort(self):
    #     data = self.port.readAll()

    #     if len(data) > 0:
    #         print(data)
           # self.textBrowserLog.insertPlainText(str(data.data(), encoding='utf-8'))
            # self.textBrowserLog.moveCursor(QtGui.QTextCursor.End)

    def sendToPort(self, text):
        self.port.write(text.encode())

    def processMessage(self):

        self.newMessage = False
        message = self.recievedString.split(" ")

        if (message[0] == "btn") or (message[0] == "Motor"):
            if (message[1] == "NosePoke") and ((message[2] == "pressed")):
                self.lcdNumberNosePoke.display(
                    self.lcdNumberNosePoke.intValue() + 1)
                self.updateRow("NosePoke", message[4], (0, 150, 0))
            if (message[1] == "Lever") and ((message[2] == "pressed")):
                self.lcdNumberLever.display(self.lcdNumberLever.intValue() + 1)
                self.updateRow("Lever", message[4], (0, 0, 0))
            if (message[1] == "GIVING"):
                self.lcdNumberFood.display(self.lcdNumberFood.intValue() + 1)
                self.updateRow("Feeder", message[3], (0, 0, 150))
            if (message[1] == "BUSY"):
                    self.updateRow("Too fast", message[3], (150, 0, 150))
        if (message[0] == "Auto"):
            self.updateRow(self.recievedString, "...", (150, 150, 150))
        if (message[0] == "Arduino"):
            self.updateRow("Start", "...", (150, 150, 150))

    def updateRow(self, ev_type, ard_time, style):
        N = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(N+1)
        time = QtCore.QTime.currentTime()
        label = QtWidgets.QTableWidgetItem(ev_type)
        label.setForeground(QtGui.QBrush(
            QtGui.QColor(style[0], style[1], style[2])))
        self.tableWidget.setItem(N, 0, label)
        label_time = QtWidgets.QTableWidgetItem(time.toString("hh:mm:ss"))
        label_time.setForeground(QtGui.QBrush(
            QtGui.QColor(style[0], style[1], style[2])))
        self.tableWidget.setItem(N, 1, label_time)
        label_ard_time = QtWidgets.QTableWidgetItem(ard_time)
        label_ard_time.setForeground(QtGui.QBrush(
            QtGui.QColor(style[0], style[1], style[2])))
        self.tableWidget.setItem(N, 2, label_ard_time)
        self.tableWidget.scrollToBottom()
        # self.tableWidget.cellWidget(N+1,1).

    def recvFromArduino(self):
        startMarker = b'<'
        endMarker = b'>'

        ck = b''
        x = self.port.read(1)  # any value that is not an end- or startMarker
        byteCount = -1  # to allow for the fact that the last increment will be one too many

      # wait for the start character
        if x == startMarker:
            while x != endMarker:
                if x != startMarker:
                    ck = ck + x
                    byteCount += 1
                if byteCount > 1000:
                    print("ERROR LONG MSG")
                    break
                x = self.port.read(1)

            self.recievedString = ck.decode("utf-8")
            self.newMessage = True
            self.processMessage()
            print(self.recievedString)
            
    def keyPressEvent(self, event):
        self.logger.process_key(event.key())

class StateLogger():
    def __init__(self, tf):
        self.state = 'off'
        self.log_active = False
        self.backgroud_state = 'no'
        self.tf = tf
        self.logging_list = ['груминг', 'пассивное', 'активное', 'стойка', 'удалить']
        self.momentary_list = ['стойка', 'удалить']
        
    def change_state(self, state):
        self.background_state = self.state
        self.state = state
        
        self.tf.labelState.setText(f"состояние: \n {self.state} ({self.background_state})")
        
        self.log_write(self.state, "")
            
                    
                
       
       
        self.tf.setFocus()
        
    def go_active(self):
        self.log_active = True
        self.change_state("log")
        self.tf.setFocus()
        
    def go_passive(self):
        self.log_active = False
        self.change_state("off")
        
    def process_key(self, key):
        if self.log_active:
            if key == Qt.Key_5: 
                self.change_state("груминг")
            elif key == Qt.Key_4: 
                self.change_state("активное")
            elif key == Qt.Key_6: 
                    self.change_state("пассивное")
            elif key == Qt.Key_8: 
                self.change_state("стойка")
            elif key == Qt.Key_0: 
                self.change_state("удалить")
            elif key == Qt.Key_1: 
                self.change_state("подход")
            elif key == Qt.Key_2: 
                self.change_state("обнюхивание")
            elif key == Qt.Key_3: 
                self.change_state("слабое нажатие")
            
    def log_write(self, state, switch):
        self.tf.updateRow(state+switch, "...", (50, 50, 50))
        

        

        
    

# Create an instance of QtWidgets.QApplication
# app = QtWidgets.QApplication(sys.argv)
# window = TestForm()  # Create an instance of our class

# app.exec_() 
 # Start the application
# window.port.close()
