from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget
import requests
from bs4 import BeautifulSoup


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
        self.response = requests.get(f"https://doc.qt.io/qt-5/{text.lower()}.html")
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.div = self.soup.find('div', class_='descr')
        self.ps = self.div.find_all('p')
        self.res = []
        for i in self.ps:
            self.res.append(i.text)
        self.finalString = '\n'.join(self.res)
        self.initUI(text, self.finalString)

    def initUI(self, text, final):
        self.setFixedSize(800, 600)
        self.setWindowTitle(f'all bout {text}')
        self.layout = QVBoxLayout(self)
        self.title = Title(text, self)
        self.title.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.layout.addWidget(self.title)

        self.result = QLabel(self)
        self.result.setFixedSize(780, 500)
        self.result.move(10, 0)
        self.result.setText(final)
