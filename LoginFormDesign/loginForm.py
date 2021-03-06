# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 695)
        MainWindow.setStyleSheet("background: #f2f2f2;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 120, 421, 450))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background: #fcfcfc;\n"
"\n"
"border: 1px solid #d9d9d9;\n"
"border-radius: 26px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.sing_in_label = QtWidgets.QLabel(self.frame)
        self.sing_in_label.setGeometry(QtCore.QRect(50, 30, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.sing_in_label.setFont(font)
        self.sing_in_label.setStyleSheet("color: #0072de;\n"
"\n"
"border: none;")
        self.sing_in_label.setObjectName("sing_in_label")
        self.email_form = QtWidgets.QLineEdit(self.frame)
        self.email_form.setGeometry(QtCore.QRect(60, 150, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.email_form.setFont(font)
        self.email_form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.email_form.setStyleSheet("QLineEdit{\n"
"     border: none;\n"
"    border-bottom: 1px solid #8c8c8c;\n"
"\n"
"    color: #909090;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom: 2px solid #0072de;\n"
"    color: #0072de;\n"
"}\n"
"\n"
"")
        self.email_form.setText("")
        self.email_form.setClearButtonEnabled(False)
        self.email_form.setObjectName("email_form")
        self.password_form = QtWidgets.QLineEdit(self.frame)
        self.password_form.setGeometry(QtCore.QRect(60, 200, 300, 35))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password_form.setFont(font)
        self.password_form.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_form.setStyleSheet("QLineEdit{\n"
"     border: none;\n"
"    border-bottom: 1px solid #8c8c8c;\n"
"\n"
"    color: #909090;\n"
"}\n"
"QLineEdit:focus{\n"
"    border-bottom: 2px solid #0072de;\n"
"    color: #0072de;\n"
"}\n"
"")
        self.password_form.setObjectName("password_form")
        self.sign_in_button = QtWidgets.QPushButton(self.frame)
        self.sign_in_button.setGeometry(QtCore.QRect(60, 300, 280, 44))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sign_in_button.setFont(font)
        self.sign_in_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sign_in_button.setStyleSheet("QPushButton{\n"
"    border: 1px solid #ededed;\n"
"    border-radius: 22px;\n"
"\n"
"    background: #ededed;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border: 2px solid #0072de;\n"
"}")
        self.sign_in_button.setObjectName("sign_in_button")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #909090;\n"
"\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.create_account = QtWidgets.QCommandLinkButton(self.frame)
        self.create_account.setGeometry(QtCore.QRect(60, 370, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.create_account.setFont(font)
        self.create_account.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_account.setStyleSheet("border: none;\n"
"text-decoration: underline #505050;\n"
"color: #505050;")
        icon = QtGui.QIcon.fromTheme("none")
        self.create_account.setIcon(icon)
        self.create_account.setObjectName("create_account")
        self.thanks_for_loging = QtWidgets.QLabel(self.frame)
        self.thanks_for_loging.setGeometry(QtCore.QRect(60, 250, 211, 31))
        self.thanks_for_loging.setStyleSheet("border: none;")
        self.thanks_for_loging.setText("")
        self.thanks_for_loging.setObjectName("thanks_for_loging")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sing_in_label.setText(_translate("MainWindow", "Sign in to your account"))
        self.sign_in_button.setText(_translate("MainWindow", "Sign in"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.create_account.setText(_translate("MainWindow", "Create Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
