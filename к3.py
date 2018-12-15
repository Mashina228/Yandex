from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Designer-17-k3.ui', self)
        self.pushButton.clicked.connect(self.hello)
        self.vivod = ''

    def hello(self):
        try:
            if self.radioButton_5.isChecked():
                self.vivod += 'Синий'
            elif self.radioButton_6.isChecked():
                self.vivod += 'Зёленый
            elif self.radioButton_7.isChecked():
                self.vivod += 'Красный'
            self.vivod += '\n'
            if self.radioButton_1.isChecked():
                self.vivod += 'Синий'
            elif self.radioButton_4.isChecked():
                self.vivod += 'Зёленый'
            elif self.radioButton_3.isChecked():
                self.vivod += 'Красный'
            self.vivod += '\n'
            if self.radioButton.isChecked():
                self.vivod += 'Синий'
            elif self.radioButton_8.isChecked():
                self.vivod += 'Зёленый'
            elif self.radioButton_2.isChecked():
                self.vivod += 'Красный'
            self.label_4.setText(''.join(self.vivod))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
