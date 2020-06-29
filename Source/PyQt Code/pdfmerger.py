from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import time
import binascii
from codecs import encode
from binascii import hexlify
from PyPDF2 import PdfFileMerger
from pathlib import Path

class pdfmerger(QDialog):

    def __init__(self,parent=None):
        super(pdfmerger,self).__init__(parent)

        self.title = "PDF Merger"
        self.setWindowTitle(self.title)
        #self.setStyleSheet("background-color: blue;")

        self.top = 0
        self.left = 0
        self.width = 800
        self.height = 480

        self.init_UI()
        self.pdf_merger()

    def init_UI(self):
        self.setWindowIcon(QtGui.QIcon("SL.png"))
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setFixedSize(800, 480)

        self.label = QLabel("PDF Merge", self)
        setFnt = QFont("Times", 12, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(10, 10)

        self.pdf_location = ''

    def pdf_merger(self):

        self.open = QPushButton("PDF Location", self)
        self.open.clicked.connect(self.open_file_location)
        self.open.setFixedSize(90, 45)
        self.open.move(10, 50)

        self.location = QLineEdit(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.location.setFont(setFnt)
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setStyleSheet("color:blue;")
        self.location.setFixedSize(230, 40)
        self.location.move(110, 50)

        self.merge = QPushButton("Merge", self)
        self.merge.clicked.connect(self.merge_pdf_files)
        self.merge.setFixedSize(90, 45)
        self.merge.move(10, 100)

        self.progress = QProgressBar(self)
        self.progress.setFixedSize(260, 40)
        self.progress.move(110, 100)

        self.openfolder = QPushButton("Open_File", self)
        self.openfolder.clicked.connect(self.open_pdf_file)
        self.openfolder.setFixedSize(120, 45)
        self.openfolder.move(10, 150)

        self.clr = QPushButton("Clear", self)
        self.clr.clicked.connect(self.clear_all)
        self.clr.setFixedSize(120, 45)
        self.clr.move(140, 150)

        self.merge = QPushButton("Merge", self)
        self.merge.clicked.connect(self.merge_pdf_files)
        self.merge.setFixedSize(90, 45)
        self.merge.move(10, 100)

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


    def open_file_location(self):

        try:

            filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
            list_filename = str(filename)

            print(filename)

        except (IndexError, TypeError, ValueError, AttributeError, FileNotFoundError, Exception):

            print("Oops!", sys.exc_info()[0], "occured.")

    def merge_pdf_files(self):

        try:

            self.logwindow.append('\n')
            self.logwindow.append("Merging PDF files in" + self.location.text())

            self.pdf_location = self.location.text()

            self.pdf_location = str(self.pdf_location)

            self.pdf_location = self.pdf_location.replace("\\","/")

            self.pdf_location = self.pdf_location + "/"

            if os.path.exists(self.pdf_location):
                os.remove("merged.pdf")
            else:
                print("The file does not exist")

            pdf_files = [str(self.pdf_location) + k.name for k in Path(str(self.pdf_location)).rglob(
                '*.pdf')]  # pdf files in the current directory is stored in a list.

            merger = PdfFileMerger()

            for pdf in pdf_files:
                merger.append(pdf)

            merger.write("./merged.pdf")
            merger.close()

            self.logwindow.append('\n')
            self.logwindow.append("Merge_completed")

            self.progress.setValue(100)

        except (IndexError, TypeError, ValueError, AttributeError, FileNotFoundError, Exception):

            print("Oops!", sys.exc_info()[0], "occured.")


    def open_pdf_file(self):

        # print(self.pdf_location+"merged.pdf")
        os.startfile(self.pdf_location+"merged.pdf")
        # print("file opened")

        self.logwindow.append('\n')
        self.logwindow.append("merged.pdf Opened Successfully")

    def clear_all(self):

        self.logwindow.clear()
        self.progress.reset()



