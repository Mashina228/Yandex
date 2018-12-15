import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        self.month = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
        super().__init__()
        self.vse = []
        self.flag = False
        self.zamet = {}
        uic.loadUi('DEsigner-17.ui', self)
        self.pushButton.clicked.connect(self.hello)

    def hello(self):
        try:
            self.listWidget.clear()
            now = self.dateTimeEdit.dateTime()
            now = now.toString()
            year = int(now.split()[-1])
            chisl = int(now.split()[2])
            mon = int(self.month.index(now.split()[1])) + 1
            hour = int(now.split()[3].split(':')[0])
            minu = int(now.split()[3].split(':')[1])
            sec = int(now.split()[3].split(':')[2])
            note = [year, mon, chisl, hour, minu, sec]
            self.zamet[str(note)] = str(self.lineEdit.text())
            if not self.flag:
                self.vse.append(note)
                self.flag = True
            else:
                for i in range(len(self.vse)):
                    if note[0] < self.vse[i][0]:
                        self.vse.insert(i, note)
                        break
                    elif note[1] < self.vse[i][1]:
                        self.vse.insert(i, note)
                        break
                    elif note[2] < self.vse[i][2]:
                        self.vse.insert(i, note)
                        break
                    elif note[3] < self.vse[i][3]:
                        self.vse.insert(i, note)
                        break
                    elif note[4] < self.vse[i][4]:
                        self.vse.insert(i, note)
                        break
                    elif note[5] < self.vse[i][5]:
                        self.vse.insert(i, note)
                        break
                else:
                    self.vse.append(note)
            for i in self.vse:
                self.listWidget.addItem('{}.{}.{} {}:{}:{} --- {}'.format(i[2], i[1], i[0], i[3], i[4], i[5], self.zamet[str(i)]))
            self.listWidget.show()
            self.lineEdit.clear()
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
ex = MyWidget()
ex.showNormal()
sys.exit(app.exec_())
