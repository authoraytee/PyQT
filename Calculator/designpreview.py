from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame
from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtGui import QPixmap
import sys
 
size = 650
height = 500
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(
            "background: #fff;\n"
            )

        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
 
 
        self.InitWindow()
 
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
 
        self.button = QPushButton("Start", self)
        self.button.move(30, 30)
        self.button.clicked.connect(self.doAnimation)
 

        #self.frame = QFrame(self)setStyleSheet("background-image: url(/home/authoraytee/Documents/PyQT/anime/jojo_1);")
                #self.email_form.setStyleSheet("border-bottom: 2px solid #0072de;\n")
        self.frame1 = QFrame(self)
        self.frame1.setStyleSheet(
            "background-image: url(/home/authoraytee/Documents/PyQT/anime/jojo_6);\n"
            "border: none;\n"
            )
        self.frame1.setFrameStyle(QFrame.Panel | QFrame.Raised)


        self.frame1.setGeometry(size, size, -50, -50)

 
        self.show()
 
    def doAnimation(self):
        self.anim = QPropertyAnimation(self.frame1, b"geometry")
        self.anim.setDuration(100)
        self.anim.setLoopCount(10)
        self.anim.setStartValue(QRect(-100, -100, size, size))
        self.anim.setEndValue(QRect(0, 0, size, size))
        self.anim.start()
 
 
 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())