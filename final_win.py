from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class FinWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
    def initUI(self):
        vline4 = QVBoxLayout()
        label8 = QLabel(self.exp.name + ', ' + txt_workheart + self.results())
        label7 = QLabel(txt_index + str(self.index))
        vline4.addWidget(label7, alignment=Qt.AlignCenter)
        vline4.addWidget(label8, alignment=Qt.AlignCenter)
        self.setLayout(vline4)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def results(self):
        self.index = (4*(int(self.exp.test1)+ int(self.exp.test2)+ int(self.exp.test3))- 200)/10
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index < 15 and self.index >= 11:
                return txt_res2
            elif self.index >= 6 and self.index <11:
                return txt_res3
            elif self.index >= 0.5 and self.index <6:
                return txt_res4
            elif self.index <= 0.4:
                return txt_res5
        if int(self.exp.age) >=13 and int(self.exp.age) <=14:
            if self.index >= 16.5:
                return txt_res1
            elif self.index < 16.4 and self.index >= 12.5:
                return txt_res2
            elif self.index >= 7.5 and self.index <12.4:
                return txt_res3
            elif self.index >= 2 and self.index <7.4:
                return txt_res4
            elif self.index <= 1.9:
                return txt_res5
        if int(self.exp.age) >= 11 and int(self.exp.age) <= 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 17.9 and self.index >= 14:
                return txt_res2
            elif self.index >= 9 and self.index <13.9:
                return txt_res3
            elif self.index >= 3.5 and self.index <8.9:
                return txt_res4
            elif self.index <= 3.4:
                return txt_res5
        if int(self.exp.age) >= 9 and int(self.exp.age)<= 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.4 and self.index >= 15.5:
                return txt_res2
            elif self.index >= 10.5 and self.index <15.4:
                return txt_res3
            elif self.index >= 5 and self.index <10.4:
                return txt_res4
            elif self.index <= 4.9:
                return txt_res5
        if int(self.exp.age)>= 7 and int(self.exp.age)<=8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 20.9 and self.index >= 17:
                return txt_res2
            elif self.index >= 12 and self.index <16.9:
                return txt_res3
            elif self.index >= 6.5 and self.index <11.9:
                return txt_res4
            elif self.index <= 6.4:
                return txt_res5