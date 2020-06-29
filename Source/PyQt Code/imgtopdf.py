from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import img2pdf
import sys
import os
from pathlib import Path

class imgtopdf(QDialog):

    def __init__(self,parent=None):
        super(imgtopdf,self).__init__(parent)

        self.title = "Image To PDF"
        self.setWindowTitle(self.title)
        #self.setStyleSheet("background-color: blue;")

        self.top = 0
        self.left = 0
        self.width = 800
        self.height = 480
        self.base = ''
        self.imgname = []
        self.f = ''

        self.init_UI()
        self.img_to_pdf_convert()

    def init_UI(self):

        self.setWindowIcon(QtGui.QIcon("SL.png"))
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(800, 480)

        self.labellsb = QLabel("ImageToPdf Converter", self)
        setFnt = QFont("Times", 12, QFont.Bold)
        self.labellsb.setFont(setFnt)
        self.labellsb.setFixedSize(300, 30)
        self.labellsb.move(10, 10)


    def img_to_pdf_convert(self):

        self.open = QPushButton("Open", self)
        self.open.clicked.connect(self.open_file)
        self.open.setFixedSize(70, 30)
        self.open.move(10, 50)

        self.filenamelabel = QLabel("FileName", self)
        setFnt = QFont("Times", 8, QFont.Bold)
        self.filenamelabel.setFont(setFnt)
        self.filenamelabel.setFixedSize(300, 30)
        self.filenamelabel.move(10, 90)

        self.filename = QLineEdit(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.filename.setFont(setFnt)
        self.filename.setAlignment(QtCore.Qt.AlignCenter)
        self.filename.setStyleSheet("color:blue;")
        self.filename.setFixedSize(130, 40)
        self.filename.move(90, 90)

        self.sizelabel = QLabel("Size(Bytes)", self)
        setFnt = QFont("Times", 8, QFont.Bold)
        self.sizelabel.setFont(setFnt)
        self.sizelabel.setFixedSize(300, 30)
        self.sizelabel.move(10, 140)

        self.sizeoutput = QLineEdit(self)
        self.sizeoutput.setFixedSize(130, 30)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.sizeoutput.setFont(setFnt)
        self.sizeoutput.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeoutput.setStyleSheet("color:blue")
        self.sizeoutput.setFixedSize(130, 35)
        self.sizeoutput.move(90, 140)

        self.convert = QPushButton("Convert", self)
        self.convert.clicked.connect(self.Convert_imgtopdf)
        self.convert.setFixedSize(70, 30)
        self.convert.move(10, 190)

        self.progress = QProgressBar(self)
        self.progress.setFixedSize(250, 30)
        self.progress.move(90, 190)

        self.close = QPushButton("Close", self)
        self.close.clicked.connect(self.close_File)
        self.close.setFixedSize(70, 30)
        self.close.move(90, 50)

        self.clr = QPushButton("Clear", self)
        self.clr.clicked.connect(self.clear_window)
        self.clr.setFixedSize(70, 30)
        self.clr.move(170, 50)

        self.tracewindowtext = QLabel("Converter_Trace_Window", self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.tracewindowtext.setFont(setFnt)
        self.tracewindowtext.setFixedSize(300, 30)
        self.tracewindowtext.move(450, 20)

        self.logwindow = QTextEdit(self)
        self.logwindow.verticalScrollBar()
        setFnt = QFont("Times", 12, QFont.Bold)
        self.logwindow.setFont(setFnt)
        self.logwindow.setStyleSheet("color:blue")
        self.logwindow.setFixedSize(320, 350)
        self.logwindow.move(450, 70)


    def open_file(self):

        try:

            filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
            list_filename = str(filename)

            self.base = os.path.basename(str(filename[0]))
            print(self.base)
            self.filename.setText(self.base)

            file_size = os.stat(str(self.base)).st_size
            self.sizeoutput.setText(str(file_size))

            with open(self.base, 'r') as self.f:
                self.logwindow.append(str(self.base)+' File Opened Successfully')


        except (IndexError, TypeError, ValueError, AttributeError, FileNotFoundError, Exception):

            print("Oops!", sys.exc_info()[0], "occured.")


    def Convert_imgtopdf(self):

        # split filename
        self.imgname = str(self.base).split('.')

        #print(self.imgname[0])
        # extract the extension
        print(self.imgname[1])

        format = self.imgname[1]

        if format == "jpg":

            with open(self.imgname[0] + ".pdf", "wb") as f:
                f.write(img2pdf.convert(self.base))
                self.progress.setValue(100)
                self.logwindow.append('\n')
                self.logwindow.append('Conversion Completed')

        if format == "png":

            with open(self.imgname[0] + ".pdf", "wb") as f:
                f.write(img2pdf.convert(self.base))
                self.progress.setValue(100)
                self.logwindow.append('\n')
                self.logwindow.append('Conversion Completed')

    def close_File(self):

        self.f.close()
        self.logwindow.append('\n')
        self.logwindow.append(str(self.base)+' File Closed')

    def clear_window(self):

        self.logwindow.clear()
        self.filename.clear()
        self.sizeoutput.clear()
        self.progress.reset()








