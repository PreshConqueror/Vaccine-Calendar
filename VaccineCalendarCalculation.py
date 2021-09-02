# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VaccineCalendarCalculation.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(647, 590)
        self.calendarWidget_current = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget_current.setGeometry(QtCore.QRect(110, 70, 431, 183))
        self.calendarWidget_current.setObjectName("calendarWidget_current")
        self.calendarWidget_future = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget_future.setGeometry(QtCore.QRect(110, 290, 421, 183))
        self.calendarWidget_future.setObjectName("calendarWidget_future")
        self.label_CurrentCal = QtWidgets.QLabel(Dialog)
        self.label_CurrentCal.setGeometry(QtCore.QRect(280, 50, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_CurrentCal.setFont(font)
        self.label_CurrentCal.setObjectName("label_CurrentCal")
        self.label_FutureCal = QtWidgets.QLabel(Dialog)
        self.label_FutureCal.setGeometry(QtCore.QRect(190, 260, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_FutureCal.setFont(font)
        self.label_FutureCal.setObjectName("label_FutureCal")
        self.label_NumberOfDays = QtWidgets.QLabel(Dialog)
        self.label_NumberOfDays.setGeometry(QtCore.QRect(70, 530, 511, 21))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_NumberOfDays.setFont(font)
        self.label_NumberOfDays.setText("")
        self.label_NumberOfDays.setObjectName("label_NumberOfDays")
        self.pushButtonCalculate = QtWidgets.QPushButton(Dialog)
        self.pushButtonCalculate.setGeometry(QtCore.QRect(250, 490, 141, 23))
        self.pushButtonCalculate.setObjectName("pushButtonCalculate")
        self.label_VaccineCalc = QtWidgets.QLabel(Dialog)
        self.label_VaccineCalc.setGeometry(QtCore.QRect(90, 10, 481, 31))
        font = QtGui.QFont()
        font.setFamily("Engravers MT")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_VaccineCalc.setFont(font)
        self.label_VaccineCalc.setTextFormat(QtCore.Qt.RichText)
        self.label_VaccineCalc.setObjectName("label_VaccineCalc")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(25, 11, 601, 551))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.calendarWidget_current.raise_()
        self.calendarWidget_future.raise_()
        self.label_CurrentCal.raise_()
        self.label_FutureCal.raise_()
        self.label_NumberOfDays.raise_()
        self.pushButtonCalculate.raise_()
        self.label_VaccineCalc.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_CurrentCal.setText(_translate("Dialog", "Today\'s date is:"))
        self.label_FutureCal.setText(_translate("Dialog", "Date on which to receive vaccination :"))
        self.pushButtonCalculate.setText(_translate("Dialog", "Calculate"))
        self.label_VaccineCalc.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#eb1506;\">VACCINATION date CALCULATION</span></p></body></html>"))

