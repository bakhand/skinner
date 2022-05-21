# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manual_regimeqYKvHD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(965, 549)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 724, 461))
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.comboBoxPort = QComboBox(self.layoutWidget)
        self.comboBoxPort.setObjectName(u"comboBoxPort")

        self.horizontalLayout.addWidget(self.comboBoxPort)

        self.pushButtonConnect = QPushButton(self.layoutWidget)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")

        self.horizontalLayout.addWidget(self.pushButtonConnect)

        self.pushButtonLever = QPushButton(self.layoutWidget)
        self.pushButtonLever.setObjectName(u"pushButtonLever")

        self.horizontalLayout.addWidget(self.pushButtonLever)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.pushButtonMotorOn = QPushButton(self.layoutWidget)
        self.pushButtonMotorOn.setObjectName(u"pushButtonMotorOn")

        self.horizontalLayout.addWidget(self.pushButtonMotorOn)

        self.pushButtonMotorOff = QPushButton(self.layoutWidget)
        self.pushButtonMotorOff.setObjectName(u"pushButtonMotorOff")

        self.horizontalLayout.addWidget(self.pushButtonMotorOff)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.layoutWidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 200):
            self.tableWidget.setRowCount(200)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(450, 16777215))
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setRowCount(200)
        self.tableWidget.setColumnCount(4)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 32, 241, 271))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelState = QLabel(self.layoutWidget1)
        self.labelState.setObjectName(u"labelState")
        font = QFont()
        font.setPointSize(11)
        self.labelState.setFont(font)

        self.verticalLayout_4.addWidget(self.labelState)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButtonLog = QPushButton(self.layoutWidget1)
        self.pushButtonLog.setObjectName(u"pushButtonLog")

        self.verticalLayout_4.addWidget(self.pushButtonLog)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.lcdNumberFood = QLCDNumber(self.layoutWidget)
        self.lcdNumberFood.setObjectName(u"lcdNumberFood")
        self.lcdNumberFood.setMinimumSize(QSize(0, 50))
        self.lcdNumberFood.setDigitCount(3)
        self.lcdNumberFood.setMode(QLCDNumber.Dec)

        self.horizontalLayout_5.addWidget(self.lcdNumberFood)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_3)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lcdNumberNosePoke = QLCDNumber(self.layoutWidget)
        self.lcdNumberNosePoke.setObjectName(u"lcdNumberNosePoke")
        self.lcdNumberNosePoke.setDigitCount(3)
        self.lcdNumberNosePoke.setMode(QLCDNumber.Dec)

        self.horizontalLayout_5.addWidget(self.lcdNumberNosePoke)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_4)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.lcdNumberLever = QLCDNumber(self.layoutWidget)
        self.lcdNumberLever.setObjectName(u"lcdNumberLever")
        self.lcdNumberLever.setDigitCount(3)
        self.lcdNumberLever.setMode(QLCDNumber.Dec)

        self.horizontalLayout_5.addWidget(self.lcdNumberLever)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonSaveAs = QPushButton(self.layoutWidget)
        self.pushButtonSaveAs.setObjectName(u"pushButtonSaveAs")

        self.verticalLayout_3.addWidget(self.pushButtonSaveAs)

        self.pushButtonSave = QPushButton(self.layoutWidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.verticalLayout_3.addWidget(self.pushButtonSave)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.line_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonAuto = QPushButton(self.layoutWidget)
        self.pushButtonAuto.setObjectName(u"pushButtonAuto")

        self.horizontalLayout_6.addWidget(self.pushButtonAuto)

        self.pushButtonOnePellet = QPushButton(self.layoutWidget)
        self.pushButtonOnePellet.setObjectName(u"pushButtonOnePellet")

        self.horizontalLayout_6.addWidget(self.pushButtonOnePellet)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0440\u0442", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.pushButtonLever.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0434\u0432\u0438\u043d\u0443\u0442\u044c \u043f\u0435\u0434\u0430\u043b\u044c", None))
        self.pushButtonMotorOn.setText(QCoreApplication.translate("Form", u"\u043c\u043e\u0442\u043e\u0440 ON", None))
        self.pushButtonMotorOff.setText(QCoreApplication.translate("Form", u"\u043c\u043e\u0442\u043e\u0440 OFF", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"type", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"time", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"ard_time", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"comment", None));
        self.labelState.setText(QCoreApplication.translate("Form", u"\u0421\u041e\u0421\u0422\u041e\u042f\u041d\u0418\u0415: NO", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0433\u0440\u0443\u043c\u0438\u043d\u0433: 5", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0430\u043a\u0442\u0438\u0432\u043d\u043e\u0435: 4", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u043f\u0430\u0441\u0441\u0438\u0432\u043d\u043e\u0435: 6", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0441\u0442\u043e\u0439\u043a\u0430: 8", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u043c\u0435\u0442\u043a\u0430 \u043e\u0448\u0438\u0431\u043a\u0438: 0", None))
        self.pushButtonLog.setText(QCoreApplication.translate("Form", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u044b", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0434\u0430\u043d\u043e \u043f\u0435\u043b\u043b\u0435\u0442", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043e\u043a \u043a\u043e\u0440\u043c\u0443\u0448\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0436\u0430\u0442\u0438\u0439 \u043d\u0430 \u043f\u0435\u0434\u0430\u043b\u044c", None))
        self.pushButtonSaveAs.setText(QCoreApplication.translate("Form", u"Save As", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Form", u"Save", None))
        self.pushButtonAuto.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0436\u0438\u043c \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0432\u044b\u0434\u0430\u0447\u0438 \u043f\u0435\u043b\u043b\u0435\u0442\u044b", None))
        self.pushButtonOnePellet.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u044c \u043e\u0434\u043d\u0443 \u043f\u0435\u043b\u043b\u0435\u0442\u0443", None))
    # retranslateUi

