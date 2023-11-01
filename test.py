from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def funkzia():
    secret.setText('Секрет!')
def passs():
    pass
app = QApplication([])
okno = QWidget()
okno.setWindowTitle('Моё второе приложение')
okno.move(500, 100)
okno.resize(1000, 1000)
knopka = QPushButton('Кнопка')
line = QVBoxLayout()
line.addWidget(knopka, alignment = Qt.AlignCenter)
secret = QLabel('')
line.addWidget(secret, alignment = Qt.AlignCenter)
knopka.clicked.connect(funkzia)

okno.setLayout(line)
okno.show()
app.exec_()
