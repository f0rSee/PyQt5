import sys
from extends import *
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 600)
        self.setWindowTitle("PyQt5 Guide")

        self.title = Title('PyQt5 Guide', self)
        self.title.move(285, 20)

        self.inputline = QLineEdit(self)
        self.inputline.move(320, 200)
        self.inputline.setFixedWidth(150)

        self.searchBtn = Button('Search', 346, 250, self)
        self.searchBtn.clicked.connect(self.connect_to)

    def connect_to(self):
        self.text = self.inputline.text()
        self.wind = GuideWidget(self.text)
        self.wind.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
    