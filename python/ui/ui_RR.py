# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RRmenTYo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_RR(object):
    def setupUi(self, RR):
        if not RR.objectName():
            RR.setObjectName(u"RR")
        RR.resize(517, 350)
        self.verticalLayout = QVBoxLayout(RR)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.stopTimeSpinBox = QSpinBox(RR)
        self.stopTimeSpinBox.setObjectName(u"stopTimeSpinBox")

        self.gridLayout.addWidget(self.stopTimeSpinBox, 0, 4, 1, 1)

        self.label = QLabel(RR)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.mplWidget = QWidget(RR)
        self.mplWidget.setObjectName(u"mplWidget")
        self.mplWidget.setMinimumSize(QSize(200, 100))

        self.gridLayout.addWidget(self.mplWidget, 3, 0, 4, 5)

        self.label_3 = QLabel(RR)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.stopPushButton = QPushButton(RR)
        self.stopPushButton.setObjectName(u"stopPushButton")

        self.gridLayout.addWidget(self.stopPushButton, 7, 4, 1, 1)

        self.pausePushButton = QPushButton(RR)
        self.pausePushButton.setObjectName(u"pausePushButton")

        self.gridLayout.addWidget(self.pausePushButton, 7, 3, 1, 1)

        self.startPushButton = QPushButton(RR)
        self.startPushButton.setObjectName(u"startPushButton")

        self.gridLayout.addWidget(self.startPushButton, 7, 0, 1, 2)

        self.generatePushButton = QPushButton(RR)
        self.generatePushButton.setObjectName(u"generatePushButton")

        self.gridLayout.addWidget(self.generatePushButton, 2, 3, 1, 2)

        self.pDoubleSpinBox = QDoubleSpinBox(RR)
        self.pDoubleSpinBox.setObjectName(u"pDoubleSpinBox")

        self.gridLayout.addWidget(self.pDoubleSpinBox, 0, 1, 1, 1)

        self.label_6 = QLabel(RR)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.nMaxSpinBox = QSpinBox(RR)
        self.nMaxSpinBox.setObjectName(u"nMaxSpinBox")

        self.gridLayout.addWidget(self.nMaxSpinBox, 1, 1, 1, 1)

        self.listView = QListView(RR)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 0, 5, 8, 1, Qt.AlignHCenter)

        self.line = QFrame(RR)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 2, 1)

        self.label_4 = QLabel(RR)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.riLabel = QLabel(RR)
        self.riLabel.setObjectName(u"riLabel")

        self.gridLayout.addWidget(self.riLabel, 2, 1, 1, 1)

        self.label_2 = QLabel(RR)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.stopTrialSpinBox = QSpinBox(RR)
        self.stopTrialSpinBox.setObjectName(u"stopTrialSpinBox")

        self.gridLayout.addWidget(self.stopTrialSpinBox, 1, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(RR)

        QMetaObject.connectSlotsByName(RR)
    # setupUi

    def retranslateUi(self, RR):
        RR.setWindowTitle(QCoreApplication.translate("RR", u"Form", None))
        self.label.setText(QCoreApplication.translate("RR", u"p", None))
        self.label_3.setText(QCoreApplication.translate("RR", u"Nmax ", None))
        self.stopPushButton.setText(QCoreApplication.translate("RR", u"Stop", None))
        self.pausePushButton.setText(QCoreApplication.translate("RR", u"Pause", None))
        self.startPushButton.setText(QCoreApplication.translate("RR", u"Start", None))
        self.generatePushButton.setText(QCoreApplication.translate("RR", u"Generate", None))
        self.label_6.setText(QCoreApplication.translate("RR", u"Stop time (min)", None))
        self.label_4.setText(QCoreApplication.translate("RR", u"RR", None))
        self.riLabel.setText(QCoreApplication.translate("RR", u"60", None))
        self.label_2.setText(QCoreApplication.translate("RR", u"Stop trial", None))
    # retranslateUi

