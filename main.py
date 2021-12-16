import sys

from extends import *

from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget

from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("PyQt5 Guide")

        self.title = Title('PyQt5 Guide', self)
        self.title.move(285, 20)

        self.qlabel = Button('QLabel', 20, 100, self)
        self.qlabel.clicked.connect(partial(self.connect_to, self.qlabel.text()))

        self.qpushbutton = Button('QPushButton', 140, 100, self)
        self.qpushbutton.clicked.connect(partial(self.connect_to, self.qpushbutton.text()))


    def connect_to(self, text):
        self.wind = GuideWidget(text)
        self.wind.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()