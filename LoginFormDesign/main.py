import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from loginForm import Ui_MainWindow
from PyQt5.QtGui import QPixmap


from db import accounts, get_output

class login(QtWidgets.QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Log In') 
        self.ui.sign_in_button.clicked.connect(self.thanks)

    def thanks(self):

        login = self.ui.email_form.text()
        passwd = self.ui.password_form.text()

        output = get_output(login, passwd)

        self.ui.thanks_for_loging.setText(output)

app = QtWidgets.QApplication([])
application = login()
application.show()
 
sys.exit(app.exec())
