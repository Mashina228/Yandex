import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QListWidgetItem, \
    QListWidget, QTimeEdit, QCalendarWidget, QLabel, QLineEdit, QPushButton

from PyQt5 import QtCore, QtGui, QtWidgets


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Ma'cDonald")

        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(504, 25, 241, 51))
        self.label.setObjectName("label")

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(4, 20, 91, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(4, 60, 91, 20))
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(4, 100, 91, 20))
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(4, 140, 91, 20))
        self.label_5.setObjectName("label_5")

        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(0, 180, 61, 20))
        self.label_6.setObjectName("label_6")

        self.label_7 = QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(4, 230, 91, 20))
        self.label_7.setObjectName("label_7")

        self.pushButton = QPushButton(self)
        self.pushButton.move(120, 10)
        self.pushButton.resize(93, 28)

        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 50, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 90, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 130, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(120, 180, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 230, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 310, 261, 81))
        self.pushButton_7.setObjectName("pushButton_7")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(240, 10, 51, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 50, 51, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 90, 51, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 130, 51, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEdit_5 = QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 180, 51, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 230, 51, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(480, 110, 301, 221))
        self.listWidget.setObjectName("listWidget")

        self.label_8 = QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(320, 10, 81, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(320, 50, 81, 16))
        self.label_9.setObjectName("label_9")

        self.label_10 = QLabel(self)
        self.label_10.setGeometry(QtCore.QRect(320, 90, 71, 16))
        self.label_10.setObjectName("label_10")

        self.label_11 = QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(320, 130, 81, 16))
        self.label_11.setObjectName("label_11")

        self.label_12 = QLabel(self)
        self.label_12.setGeometry(QtCore.QRect(320, 180, 81, 16))
        self.label_12.setObjectName("label_12")

        self.label_13 = QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(320, 230, 101, 16))
        self.label_13.setObjectName("label_13")

        self.label.setText('Чек')
        self.label_2.setText('Биг Мак')
        self.label_3.setText('Картошка Фри')
        self.label_4.setText('Напиток')
        self.label_5.setText('Биг Тести')
        self.label_6.setText('Пирожок')
        self.label_7.setText('Морожное')
        self.label_8.setText("100 рублей")
        self.label_9.setText("200 рублей")
        self.label_10.setText("0 рублей")
        self.label_11.setText("300 рублей")
        self.label_12.setText("30 рублей")
        self.label_13.setText("180 рублей")

        self.pushButton.setText('Добавить')
        self.pushButton_2.setText('Добавить')
        self.pushButton_3.setText('Добавить')
        self.pushButton_4.setText('Добавить')
        self.pushButton_5.setText('Добавить')
        self.pushButton_6.setText('Добавить')
        self.pushButton_7.setText('Сделать Заказ')

        self.pushButton.clicked.connect(self.run_1)
        self.pushButton_2.clicked.connect(self.run_2)
        self.pushButton_3.clicked.connect(self.run_3)
        self.pushButton_4.clicked.connect(self.run_4)
        self.pushButton_5.clicked.connect(self.run_5)
        self.pushButton_6.clicked.connect(self.run_6)
        self.pushButton_7.clicked.connect(self.vs)

        self.lineEdit.setText("0")
        self.lineEdit_2.setText('0')
        self.lineEdit_3.setText("0")
        self.lineEdit_4.setText("0")
        self.lineEdit_5.setText("0")
        self.lineEdit_6.setText("0")

        self.vse = {}
        self.zena = {}

    def run_1(self):
        a = int(self.lineEdit.text())
        self.vse['Биг Мак'] = a
        self.zena['Биг Мак'] = a * 100
        self.pushButton.setText('Добавлено')

    def run_2(self):
        a = int(self.lineEdit_2.text())
        self.vse['Картошка Фри'] = a
        self.zena['Картошка Фри'] = a * 200
        self.pushButton_2.setText('Добавлено')

    def run_3(self):
        a = int(self.lineEdit_3.text())
        self.vse['Напиток'] = a
        self.zena['Напиток'] = a * 0
        self.pushButton_3.setText('Добавлено')

    def run_4(self):
        a = int(self.lineEdit_4.text())
        self.vse['Биг Тести'] = a
        self.zena['Биг Тести'] = a * 300
        self.pushButton_4.setText('Добавлено')

    def run_5(self):
        a = int(self.lineEdit_5.text())
        self.vse['Пирожок'] = a
        self.zena['Пирожок'] = a * 30
        self.pushButton_5.setText('Добавлено')

    def run_6(self):
        a = int(self.lineEdit_6.text())
        self.vse['Мороженое'] = a
        self.pushButton_6.setText('Добавлено')

    def vs(self):
        item = []
        for i in self.vse:
            if self.vse[i] != 0:
                self.listWidget.addItem(i + ' - ' + str(self.vse[i]))
        self.listWidget.addItem(str(sum(self.zena.values())) + ' ' + 'рублей')
        self.listWidget.addItem('------------------------------------------------')
        self.listWidget.show()
        self.pushButton.setText('Добавить')
        self.pushButton_2.setText('Добавить')
        self.pushButton_3.setText('Добавить')
        self.pushButton_4.setText('Добавить')
        self.pushButton_5.setText('Добавить')
        self.pushButton_6.setText('Добавить')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
