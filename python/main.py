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


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

