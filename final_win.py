from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class FinWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def initUI(self):
        vline4 = QVBoxLayout()
        label7 = QLabel(txt_index)
        label8 = QLabel(txt_workheart)
        vline4.addWidget(label7, alignment=Qt.AlignCenter)
        vline4.addWidget(label8, alignment=Qt.AlignCenter)
        self.setLayout(vline4)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)