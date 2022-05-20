# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RIHSaGmc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_RI(object):
    def setupUi(self, RI):
        if not RI.objectName():
            RI.setObjectName(u"RI")
        RI.resize(517, 350)
        self.verticalLayout = QVBoxLayout(RI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pDoubleSpinBox = QDoubleSpinBox(RI)
        self.pDoubleSpinBox.setObjectName(u"pDoubleSpinBox")

        self.gridLayout.addWidget(self.pDoubleSpinBox, 0, 1, 1, 1)

        self.tSpinBox = QSpinBox(RI)
        self.tSpinBox.setObjectName(u"tSpinBox")

        self.gridLayout.addWidget(self.tSpinBox, 1, 1, 1, 1)

        self.label_6 = QLabel(RI)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.stopTimeSpinBox = QSpinBox(RI)
        self.stopTimeSpinBox.setObjectName(u"stopTimeSpinBox")

        self.gridLayout.addWidget(self.stopTimeSpinBox, 0, 4, 1, 1)

        self.stopPushButton = QPushButton(RI)
        self.stopPushButton.setObjectName(u"stopPushButton")

        self.gridLayout.addWidget(self.stopPushButton, 7, 4, 1, 1)

        self.label_7 = QLabel(RI)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 3, 1, 1)

        self.label_3 = QLabel(RI)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.stopRewardSpinBox = QSpinBox(RI)
        self.stopRewardSpinBox.setObjectName(u"stopRewardSpinBox")

        self.gridLayout.addWidget(self.stopRewardSpinBox, 2, 4, 1, 1)

        self.line = QFrame(RI)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 3, 1)

        self.tMaxSpinBox = QSpinBox(RI)
        self.tMaxSpinBox.setObjectName(u"tMaxSpinBox")

        self.gridLayout.addWidget(self.tMaxSpinBox, 2, 1, 1, 1)

        self.label_2 = QLabel(RI)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(RI)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.startPushButton = QPushButton(RI)
        self.startPushButton.setObjectName(u"startPushButton")

        self.gridLayout.addWidget(self.startPushButton, 7, 0, 1, 2)

        self.label_8 = QLabel(RI)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1)

        self.pausePushButton = QPushButton(RI)
        self.pausePushButton.setObjectName(u"pausePushButton")

        self.gridLayout.addWidget(self.pausePushButton, 7, 3, 1, 1)

        self.stopTrialSpinBox = QSpinBox(RI)
        self.stopTrialSpinBox.setObjectName(u"stopTrialSpinBox")

        self.gridLayout.addWidget(self.stopTrialSpinBox, 1, 4, 1, 1)

        self.label_4 = QLabel(RI)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.riLabel = QLabel(RI)
        self.riLabel.setObjectName(u"riLabel")

        self.gridLayout.addWidget(self.riLabel, 3, 1, 1, 1)

        self.generatePushButton = QPushButton(RI)
        self.generatePushButton.setObjectName(u"generatePushButton")

        self.gridLayout.addWidget(self.generatePushButton, 3, 3, 1, 2)

        self.listView = QListView(RI)
        self.listView.setObjectName(u"listView")

        self.gridLayout.addWidget(self.listView, 0, 5, 8, 1, Qt.AlignHCenter)

        self.mplWidget = QWidget(RI)
        self.mplWidget.setObjectName(u"mplWidget")
        self.mplWidget.setMinimumSize(QSize(200, 100))

        self.gridLayout.addWidget(self.mplWidget, 4, 0, 3, 5)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(RI)

        QMetaObject.connectSlotsByName(RI)
    # setupUi

    def retranslateUi(self, RI):
        RI.setWindowTitle(QCoreApplication.translate("RI", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("RI", u"Stop time (min)", None))
        self.stopPushButton.setText(QCoreApplication.translate("RI", u"Stop", None))
        self.label_7.setText(QCoreApplication.translate("RI", u"Stop trial", None))
        self.label_3.setText(QCoreApplication.translate("RI", u"Tmax (sec)", None))
        self.label_2.setText(QCoreApplication.translate("RI", u"T (sec)", None))
        self.label.setText(QCoreApplication.translate("RI", u"p", None))
        self.startPushButton.setText(QCoreApplication.translate("RI", u"Start", None))
        self.label_8.setText(QCoreApplication.translate("RI", u"Stop reward", None))
        self.pausePushButton.setText(QCoreApplication.translate("RI", u"Pause", None))
        self.label_4.setText(QCoreApplication.translate("RI", u"RI (sec)", None))
        self.riLabel.setText(QCoreApplication.translate("RI", u"60", None))
        self.generatePushButton.setText(QCoreApplication.translate("RI", u"Generate", None))
    # retranslateUi

