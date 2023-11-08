from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from final_win import *
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
        label6 = QLabel('')
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
        vline3.addWidget(label6, alignment=Qt.AlignCenter)
        hline1.addLayout(vline2)
        hline1.addLayout(vline3)
        self.setLayout(hline1)
    def connects(self):
        self.pbutton4.clicked.connect(self.neWin)
    def neWin(self):
        self.hide()
        self.Win3 = FinWin()


