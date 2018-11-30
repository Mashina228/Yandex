import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QLabel
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.fin = []

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('MackDonald')

        cb = QCheckBox('Big Mack', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeMack)

        cb = QCheckBox('Potato', self)
        cb.move(30, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changePot)

        cb = QCheckBox('Co-Ca-Cola', self)
        cb.move(40, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeCO)

        a, b = 100, 100

        for i in self.fin:
            self.url = QLabel(self)
            self.url.setText(i)
            self.url.move(a, b)
            b += 20

        self.show()

    def changeMack(self, state):
        if state == Qt.Checked:
            self.fin.append('Big Mack')

    def changePot(self, state):
        if state == Qt.Checked:
            self.fin.append('Potato')

    def changeCO(self, state):
        if state == Qt.Checked:
            self.fin.append('Co-Ca-Cola')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
