from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTabWidget
import sys
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from RI_test import TestUiRi
from RR_test import TestUiRR
from manual_form import TestForm





# Subclass QMainWindow to customize your application's main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.trigger = False

        self.setWindowTitle("Manual + Auto + RI + RR")
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        self.crt = TestForm()
        self.ri = TestUiRi()
        self.rr = TestUiRR()
        
        layout.addWidget(self.crt)
        
        self.tab = QTabWidget()
        
        self.tab.addTab(self.ri, "RI")
        self.tab.addTab(self.rr, "RR")
        
        
        layout.addWidget(self.tab)
        
        
        widget.setLayout(layout)
        # Set the central widget of the Window.
             
        
        self.setCentralWidget(widget)
        
    def catch_timer(self, x):
        self.crt.logger.change_state(f"интервал {x+1}")
        self.trigger = True
        print("Trigger взведен!!")
        
    def catch_start(self):
        self.crt.logger.change_state(f"Начало")
        self.crt.logger.change_state(f"интервал 1")
        self.crt.sendToPort("<01>")
        
    def catch_stop(self):
        self.crt.logger.change_state(f"Конец")
        self.crt.sendToPort("<00>")
    
    def catch_pause(self):
        self.crt.logger.change_state(f"Пауза")
        self.crt.sendToPort("<00>")
        
    def catch_resume(self):
        self.crt.logger.change_state(f"Продолжение")
        self.crt.sendToPort("<01>")
        
    def catch_lever_press(self):
        try:
           self.rr.numberIterator._lever_hook()
        except:
            print("Number itrerator ne och")
            
            
        if self.trigger:
           print("Trigger спущен")
           self.ri.riModel.foodGiven()
           self.crt.sendToPort("<12>")
        self.trigger = False
        
    def catch_countdown_ended(self):
           print("Нажатия отработаны!")
           self.crt.sendToPort("<12>")
        
        
        
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

