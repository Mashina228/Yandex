import sys

from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('Designer-17-k3.ui', self)
        self.pushButton.clicked.connect(self.p)
        self.vivod = ''
        self.show()

    def p(self):
        self.flag = True

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self, qp):
        try:
            if self.radioButton_6.isChecked():
                qp.setBrush(QColor(0, 250, 0))
            elif self.radioButton_7.isChecked():
                qp.setBrush(QColor(250, 0, 0))
            elif self.radioButton_5.isChecked():
                qp.setBrush(QColor(0, 0, 250))
            qp.drawRect(280, 300, 200, 40)
            if self.radioButton_4.isChecked():
                qp.setBrush(QColor(0, 250, 0))
            elif self.radioButton_3.isChecked():
                qp.setBrush(QColor(250, 0, 0))
            elif self.radioButton_1.isChecked():
                qp.setBrush(QColor(0, 0, 250))
            qp.drawRect(280, 340, 200, 40)
            if self.radioButton_8.isChecked():
                qp.setBrush(QColor(0, 250, 0))
            elif self.radioButton_2.isChecked():
                qp.setBrush(QColor(250, 0, 0))
            elif self.radioButton.isChecked():
                qp.setBrush(QColor(0, 0, 250))
            qp.drawRect(280, 380, 200, 40)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
