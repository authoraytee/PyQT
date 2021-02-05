import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from anime import Ui_MainWindow

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtGui import QPixmap
import sys


class main(QtWidgets.QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Anime') 
 
        self.pushButton = QPushButton("Start", self)
        self.pushButton.move(30, 30)
        self.pushButton.clicked.connect(self.doAnimation)
 
        self.jojo_2 = ui.label()
        self.jojo_2.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.jojo_2.setGeometry(100, 100, 0, 0)

        self.show()
 




    def doAnimation(self):
        self.anim = QPropertyAnimation(self.jojo_2, b"geometry")
        self.anim.setDuration(135)
        self.anim.setLoopCount(10)
        self.anim.setStartValue(QRect(100, 100, 100, 100))
        self.anim.setEndValue(QRect(150, 150, 100, 100))
        self.anim.start()

app = QtWidgets.QApplication([])
application = main()
application.show()
 
sys.exit(app.exec())
