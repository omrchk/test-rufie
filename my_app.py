from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        hello = QLabel(txt_hello)
        instruction = QLabel(txt_instruction)
        self.b_next = QPushButton(txt_next)
        vline1 = QVBoxLayout()
        vline1.addWidget(hello, alignment = Qt.AlignLeft)
        vline1.addWidget(instruction, alignment = Qt.AlignLeft)
        vline1.addWidget(self.b_next, alignment = Qt.AlignCenter)
        self.setLayout(vline1)
    def connects(self):
        self.b_next.clicked.connect(self.funkzia)
    def funkzia(self):
        self.hide()
        self.Win2 = SecWin()
    
app = QApplication([])
okno = MainWin()
app.exec_()