from PyQt5.QtGui import QPixmap, QTransform
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QRadioButton, QHBoxLayout, \
    QLabel, QApplication
from PyQt5.QtCore import QRect
from PIL import Image


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Редактор картинки')

        self.btn = QPushButton('показать', self)
        self.btn.resize(100, 20)
        self.btn.move(220, 50)
        self.btn.clicked.connect(self.hello)

        self.btn_1 = QPushButton('Повернуть на 90 градусов и показать', self)
        self.btn_1.resize(240, 20)
        self.btn_1.move(150, 100)
        self.btn_1.clicked.connect(self.hell)

        self.url = QLabel(self)
        self.url.setText('Что изменить:')
        self.url.move(200, 250)

        self.url_s = QLineEdit(self)
        self.url_s.move(300, 250)

        self.radioButton = QRadioButton(self)
        self.radioButton.setGeometry(QRect(45, 220, 100, 20))
        self.radioButton.setText("Всё в синий")

        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setGeometry(QRect(45, 260, 110, 20))
        self.radioButton_2.setText("Всё в красный")

        self.radioButton_3 = QRadioButton(self)
        self.radioButton_3.setGeometry(QRect(45, 300, 110, 20))
        self.radioButton_3.setText("Всё в зелёный")

        self.lbl = QLabel(self)
        self.lbl.resize(300, 300)

        self.lbl.move(400, 300)


    def hello(self):
        try:
            a = str(self.url_s.text())
            im = Image.open(a)
            pixels = im.load()
            x, y = im.size
            if self.radioButton.isChecked():
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 0, 0, 255
            elif self.radioButton_2.isChecked():
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 255, 0, 0
            elif self.radioButton_3.isChecked():
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 0, 255, 0
            im.save(a)
            pixmap = QPixmap(a)
            self.lbl.setPixmap(pixmap)
            self.lbl.show()
        except Exception as e:
            print(e)

    def hell(self):
        try:
            a = str(self.url_s.text())
            im = Image.open(a)
            pixels = im.load()
            x, y = im.size
            if self.radioButton.isChecked():
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 0, 0, 255
            elif self.radioButton_2.isChecked():
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 255, 0, 0
            elif self.radioButton_3.isChecked():
                for i in range(x):
                    for j in range(y):
                        pixels[i, j] = 0, 255, 0
            im.save()
            pixmap = QPixmap(a)
            t = QTransform().rotate(45)

            self.lbl.setPixmap(pixmap.transformed(t))

            self.lbl.show()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
