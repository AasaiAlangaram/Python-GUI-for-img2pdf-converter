import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import imgtopdf
import pdfmerger

class MainApp(QMainWindow):
    def __init__(self,parent = None):
        super(MainApp,self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QtGui.QIcon("SL.png"))
        self.main_widget = App(self)
        self.setCentralWidget(self.main_widget)
        self.setStyleSheet("background-color: pale green;")
        self.setWindowTitle("SL Image to Pdf Converter")
        #self.setGeometry(0,0,800,480)

        # set geometry to 5'inch
        self.setFixedSize(800,480)
        # set fixed location in window
        self.move(0,0)
        self.show()


class App(QWidget):
    def __init__(self,parent):
        super(App,self).__init__(parent)
        self.parent = parent
        self.init_UI()

    def init_UI(self):
        self.BtnWidth = 350
        self.BtnHeight = 250
        self.x =210
        self.y =72

        self.qBox = imgtopdf.imgtopdf()
        self.qBox1= pdfmerger.pdfmerger()

        BtnImgtoPdf = QPushButton("Image to PDF Converter",self)
        setFnt = QFont("Times", 14, QFont.Bold)
        BtnImgtoPdf.setFont(setFnt)
        BtnImgtoPdf.setToolTip("Click this button to convert list of JPG files to single PDF")
        BtnImgtoPdf.clicked.connect(self.open1)
        BtnImgtoPdf.setFixedSize(self.BtnWidth,60)
        BtnImgtoPdf.move(self.x,60)

        BtnPdfmerger = QPushButton("PDF Merger", self)
        setFnt = QFont("Times", 14, QFont.Bold)
        BtnPdfmerger.setFont(setFnt)
        BtnPdfmerger.setToolTip("Click this button to Merge list of pdf files to single pdf")
        BtnPdfmerger.clicked.connect(self.open2)
        BtnPdfmerger.setFixedSize(self.BtnWidth, 60)
        BtnPdfmerger.move(self.x,self.y *1+60)

    def open1(self):
        self.qBox.show()

    def open2(self):
        self.qBox1.show()


app = QApplication(sys.argv)

win = MainApp()
win.show()

sys.exit(app.exec_())
