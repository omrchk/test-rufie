from instr import *
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import *
from final_win import *
from PyQt5.QtGui import QFont

class SecWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle('Текст')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        vline2 = QVBoxLayout()
        vline3 = QVBoxLayout()
        hline1 = QHBoxLayout()
        label1 = QLabel(txt_name)
        label2 = QLabel(txt_age)
        label3 = QLabel(txt_test1)
        label4 = QLabel(txt_test2)
        label5 = QLabel(txt_test3)
        self.text_timer = QLabel('')
        self.pbutton1 = QPushButton(txt_starttest1)
        self.pbutton2 = QPushButton(txt_starttest2)
        self.pbutton3 = QPushButton(txt_starttest3)
        self.pbutton4 = QPushButton(txt_sendresults)
        self.linedit1 = QLineEdit(txt_hintname)
        self.linedit2 = QLineEdit(txt_hintage)
        self.linedit3 = QLineEdit(txt_hinttest1)
        self.linedit4 = QLineEdit(txt_hinttest2)
        self.linedit5 = QLineEdit(txt_hinttest3)
        vline2.addWidget(label1, alignment=Qt.AlignLeft)
        vline2.addWidget(self.linedit1, alignment=Qt.AlignLeft)
        vline2.addWidget(label2, alignment=Qt.AlignLeft)
        vline2.addWidget(self.linedit2, alignment=Qt.AlignLeft)
        vline2.addWidget(label3, alignment=Qt.AlignLeft)
        vline2.addWidget(self.pbutton1, alignment=Qt.AlignLeft)
        vline2.addWidget(self.linedit3, alignment=Qt.AlignLeft)
        vline2.addWidget(label4, alignment=Qt.AlignLeft)
        vline2.addWidget(self.pbutton2, alignment=Qt.AlignLeft)
        vline2.addWidget(label5, alignment=Qt.AlignLeft)
        vline2.addWidget(self.pbutton3, alignment=Qt.AlignLeft)
        vline2.addWidget(self.linedit4, alignment=Qt.AlignLeft)
        vline2.addWidget(self.linedit5, alignment=Qt.AlignLeft)
        vline2.addWidget(self.pbutton4, alignment=Qt.AlignCenter)
        vline3.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        hline1.addLayout(vline2)
        hline1.addLayout(vline3)
        self.setLayout(hline1)
    def connects(self):
        self.pbutton4.clicked.connect(self.neWin)
        self.pbutton1.clicked.connect(self.startimer1)
        self.pbutton2.clicked.connect(self.startimer2)
        self.pbutton3.clicked.connect(self.startimer3)
    def startimer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent1)
        self.timer.start(1000)
    def timerEvent1(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Calibri', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 100)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def startimer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent2)
        self.timer.start(1500)
    def timerEvent2(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QFont('Calibri', 48, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 100)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def startimer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent3)
        self.timer.start(1000)
    def timerEvent3(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QFont('Calibri', 36, QFont.Bold))
        if int(time.toString('hh:mm:ss')[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        elif int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0, 0, 100)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def neWin(self):
        self.hide()
        self.exp = Expiriment(self.linedit1.text(),
                              self.linedit2.text(),
                              self.linedit3.text(),
                              self.linedit4.text(),
                              self.linedit5.text())
        self.Win3 = FinWin(self.exp)
class Expiriment():
    def __init__(self, name, age, test1, test2, test3):
        self.name = name
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

