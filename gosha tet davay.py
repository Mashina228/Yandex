import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('показ картинки')

        self.btn = QPushButton('показать', self)
        self.btn.resize(100, 50)
        self.btn.move(250, 50)
        self.btn.clicked.connect(self.hello)

        self.url = QLabel(self)
        self.url.setText('Первое число:')
        self.url.move(250, 250)

        self.url_s = QLineEdit(self)
        self.url_s.move(300, 250)

    def hello(self):
        a = str(self.url_s.text())
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(a)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        hbox.addWidget(lbl)
        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())