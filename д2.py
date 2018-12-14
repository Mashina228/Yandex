import sys

from PyQt5.QtWidgets import QApplication, QRadioButton, QWidget, QPushButton, QLabel
from PyQt5.QtCore import QRect


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.pole = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.flag = True
        self.setGeometry(0, 0, 548, 570)
        self.setWindowTitle("Game")

        self.radioButton = QRadioButton(self)
        self.radioButton.setGeometry(QRect(10, 10, 201, 21))

        self.radioButton_2 = QRadioButton(self)
        self.radioButton_2.setGeometry(QRect(10, 40, 171, 31))

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(100, 140, 81, 61))
        self.pushButton.setText("")

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(QRect(100, 220, 81, 61))
        self.pushButton_2.setText("")

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(QRect(100, 300, 81, 61))
        self.pushButton_3.setText("")

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setGeometry(QRect(210, 140, 81, 61))
        self.pushButton_4.setText("")

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setGeometry(QRect(210, 220, 81, 61))
        self.pushButton_5.setText("")

        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setGeometry(QRect(210, 300, 81, 61))
        self.pushButton_6.setText("")

        self.pushButton_7 = QPushButton(self)
        self.pushButton_7.setGeometry(QRect(310, 140, 81, 61))
        self.pushButton_7.setText("")

        self.pushButton_8 = QPushButton(self)
        self.pushButton_8.setGeometry(QRect(310, 220, 81, 61))
        self.pushButton_8.setText("")

        self.pushButton_9 = QPushButton(self)
        self.pushButton_9.setGeometry(QRect(310, 300, 81, 61))
        self.pushButton_9.setText("")

        self.label = QLabel(self)
        self.label.setGeometry(QRect(210, 10, 261, 81))
        self.label.setText("")

        self.pushButton_10 = QPushButton(self)
        self.pushButton_10.setGeometry(QRect(170, 410, 161, 81))

        self.pushButton_10.setObjectName("pushButton_10")
        self.radioButton.setText("Первый игрок ходит - x")
        self.radioButton_2.setText("Второй игрок ходит - o")
        self.pushButton_10.setText("Новая игра")

        self.pushButton_10.clicked.connect(self.clearing)
        self.pushButton.clicked.connect(self.znak_1)
        self.pushButton_2.clicked.connect(self.znak_2)
        self.pushButton_3.clicked.connect(self.znak_3)
        self.pushButton_4.clicked.connect(self.znak_4)
        self.pushButton_5.clicked.connect(self.znak_5)
        self.pushButton_6.clicked.connect(self.znak_6)
        self.pushButton_7.clicked.connect(self.znak_7)
        self.pushButton_8.clicked.connect(self.znak_8)
        self.pushButton_9.clicked.connect(self.znak_9)
        self.show()

    def vivod(self, who):
        if who == 'x':
            self.label.setText('Выиграли крестики')
        else:
            self.label.setText('Выиграли нолики')

    def clearing(self):
        self.label.clear()
        self.pushButton.setText('')
        self.pushButton_2.setText('')
        self.pushButton_3.setText('')
        self.pushButton_4.setText('')
        self.pushButton_5.setText('')
        self.pushButton_6.setText('')
        self.pushButton_7.setText('')
        self.pushButton_8.setText('')
        self.pushButton_9.setText('')
        self.flag = True
        self.pole = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def check(self):
        if self.pole[0][0] == self.pole[0][1] == self.pole[0][2]:
            self.vivod(self.pole[0][0])
        elif self.pole[1][0] == self.pole[1][1] == self.pole[1][2]:
            self.vivod(self.pole[1][0])
        elif self.pole[2][0] == self.pole[2][1] == self.pole[2][2]:
            self.vivod(self.pole[2][0])
        elif self.pole[0][0] == self.pole[1][0] == self.pole[2][0]:
            self.vivod(self.pole[0][0])
        elif self.pole[0][1] == self.pole[1][1] == self.pole[2][1]:
            self.vivod(self.pole[0][1])
        elif self.pole[0][2] == self.pole[1][2] == self.pole[2][2]:
            self.vivod(self.pole[0][2])
        elif self.pole[0][0] == self.pole[1][1] == self.pole[2][2]:
            self.vivod(self.pole[0][0])
        elif self.pole[0][2] == self.pole[1][1] == self.pole[2][0]:
            self.vivod(self.pole[0][2])

    def znak_1(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton.setText('X')
            self.flag = False
            self.pole[0][0] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton.setText('O')
            self.flag = True
            self.pole[0][0] = 'o'
            self.check()

    def znak_2(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_2.setText('X')
            self.flag = False
            self.pole[0][1] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_2.setText('O')
            self.flag = True
            self.pole[0][1] = '0'
            self.check()

    def znak_3(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_3.setText('X')
            self.flag = False
            self.pole[0][2] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_3.setText('O')
            self.flag = True
            self.pole[0][2] = 'o'
            self.check()

    def znak_4(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_4.setText('X')
            self.flag = False
            self.pole[1][0] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_4.setText('O')
            self.flag = True
            self.pole[1][0] = 'o'
            self.check()

    def znak_5(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_5.setText('X')
            self.flag = False
            self.pole[1][1] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_5.setText('O')
            self.flag = True
            self.pole[1][1] = 'o'
            self.check()

    def znak_6(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_6.setText('X')
            self.flag = False
            self.pole[1][2] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_6.setText('O')
            self.flag = True
            self.pole[1][2] = 'o'
            self.check()

    def znak_7(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_7.setText('X')
            self.flag = False
            self.pole[2][0] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_7.setText('O')
            self.flag = True
            self.pole[2][0] = 'o'
            self.check()

    def znak_8(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_8.setText('X')
            self.flag = False
            self.pole[2][1] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_8.setText('O')
            self.flag = True
            self.pole[2][1] = 'o'
            self.check()

    def znak_9(self):
        if self.radioButton.isChecked() and self.flag:
            self.pushButton_9.setText('X')
            self.flag = False
            self.pole[2][2] = 'x'
            self.check()
        elif self.radioButton_2.isChecked() and not self.flag:
            self.pushButton_9.setText('O')
            self.flag = True
            self.pole[2][2] = 'o'
            self.check()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
