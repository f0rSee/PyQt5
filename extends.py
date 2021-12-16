from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
import json

with open("data.json", "r") as file:
    DATA = json.load(file)


class Button(QPushButton):
    def __init__(self, text, x, y, parent=None):
        super(QPushButton, self).__init__(parent)
        self.setText(text)
        self.move(x, y)
        self.resize(100, 40)


class Title(QLabel):
    def __init__(self, text, parent=None):
        super(Title, self).__init__(parent)
        self.setText(text)
        self.resize(300, 50)
        self.setFont(QtGui.QFont("Arial", 28, QtGui.QFont.Black))


class GuideWidget(QWidget):
    def __init__(self, text, parent=None):
        super(GuideWidget, self).__init__(parent)
        self.initUI(text)

    def initUI(self, text):
        self.setFixedSize(800, 600)
        self.setWindowTitle(f'all bout {text}')
        self.layout = QVBoxLayout(self)
        self.title = Title(text, self)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.layout.addWidget(self.title)

        self.desc = QLabel(f'{DATA[text]["description"]}', self)
        self.desc.move(20, 100)
        self.desc.resize(750, 50)