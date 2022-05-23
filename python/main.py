from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from RI_test import TestUiRi
from manual_form import TestForm





# Subclass QMainWindow to customize your application's main window
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.trigger = False

        self.setWindowTitle("Manual + Auto + RI")
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        self.crt = TestForm()
        self.ri = TestUiRi()
        
        layout.addWidget(self.crt)
        layout.addWidget(self.ri)
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
        if self.trigger:
           print("Trigger спущен")
           self.ri.riModel.foodGiven()
           self.crt.sendToPort("<12>")
        self.trigger = False
        
        
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

