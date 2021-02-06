# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 666)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 140, 241, 61))
        self.label.setStyleSheet("QLabel {\n"
"  qproperty-alignment: \'AlignVCenter | AlignRight\';\n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"background-color : white;")
        self.label.setObjectName("label")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(200, 200, 61, 61))
        self.pushButton_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_clear.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bebebe​, stop: 1 #d7d7d7​);\n"
"}")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_plusMinus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plusMinus.setGeometry(QtCore.QRect(260, 200, 61, 61))
        self.pushButton_plusMinus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_plusMinus.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bebebe​, stop: 1 #d7d7d7​);\n"
"}")
        self.pushButton_plusMinus.setObjectName("pushButton_plusMinus")
        self.pushButton_divice = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divice.setGeometry(QtCore.QRect(380, 200, 61, 61))
        self.pushButton_divice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_divice.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff7832​, stop: 1 #ff9739​);\n"
"}")
        self.pushButton_divice.setObjectName("pushButton_divice")
        self.pushButton_percent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_percent.setGeometry(QtCore.QRect(320, 200, 61, 61))
        self.pushButton_percent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_percent.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bebebe​, stop: 1 #d7d7d7​);\n"
"}")
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(200, 260, 61, 61))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(320, 260, 61, 61))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(380, 260, 61, 61))
        self.pushButton_multiply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_multiply.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff7832​, stop: 1 #ff9739​);\n"
"}")
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(260, 260, 61, 61))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 320, 61, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(320, 320, 61, 61))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_subtract.setGeometry(QtCore.QRect(380, 320, 61, 61))
        self.pushButton_subtract.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_subtract.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff7832​, stop: 1 #ff9739​);\n"
"}")
        self.pushButton_subtract.setObjectName("pushButton_subtract")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(260, 320, 61, 61))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(200, 380, 61, 61))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 380, 61, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(380, 380, 61, 61))
        self.pushButton_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_add.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff7832​, stop: 1 #ff9739​);\n"
"}")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 380, 61, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_decimal.setGeometry(QtCore.QRect(320, 440, 61, 61))
        self.pushButton_decimal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_decimal.setStyleSheet("QPushButton {\n"
"  background-color: rgb(215, 215, 215);\n"
"  border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bebebe​, stop: 1 #d7d7d7​);\n"
"}")
        self.pushButton_decimal.setObjectName("pushButton_decimal")
        self.pushButton_equals = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equals.setGeometry(QtCore.QRect(380, 440, 61, 61))
        self.pushButton_equals.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_equals.setStyleSheet("QPushButton {\n"
"  background-color: rgb(255, 151, 57);\n"
"  color: white; \n"
"  border: 1px solid gray;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ff7832​, stop: 1 #ff9739​);\n"
"}")
        self.pushButton_equals.setObjectName("pushButton_equals")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(200, 440, 121, 61))
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet("QPushButton {\n"
"   border: 1px solid gray;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #dadbde​, stop: 1 #f6f7fa​);\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "           0"))
        self.pushButton_clear.setText(_translate("MainWindow", "C"))
        self.pushButton_plusMinus.setText(_translate("MainWindow", "+/-"))
        self.pushButton_divice.setText(_translate("MainWindow", "/"))
        self.pushButton_percent.setText(_translate("MainWindow", "%"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_multiply.setText(_translate("MainWindow", "X"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_subtract.setText(_translate("MainWindow", "-"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_decimal.setText(_translate("MainWindow", "."))
        self.pushButton_equals.setText(_translate("MainWindow", "="))
        self.pushButton_0.setText(_translate("MainWindow", "0"))