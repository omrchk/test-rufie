from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

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
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()
        label5 = QLabel()
        label6 = QLabel()
        self.pbutton1 = QPushButton()
        self.pbutton2 = QPushButton()
        self.pbutton3 = QPushButton()
        self.pbutton4 = QPushButton()
        self.linedit1 = QLineEdit()
        self.linedit2 = QLineEdit()
        self.linedit3 = QLineEdit()
        self.linedit4 = QLineEdit()
        self.linedit5 = QLineEdit()