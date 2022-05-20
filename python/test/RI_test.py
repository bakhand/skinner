from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

from ui.ui_RI import Ui_RI


class TestUiRi(QtWidgets.QWidget, Ui_RI):
    def __init__(self, parent=None):
        super(TestUiRi, self).__init__(parent)
        self.setupUi(self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("22"))
        self.mplWidget.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    form = TestUiRi()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
