from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

    def initUI(self):
       self.text_index = QLabel(txt_index)
       self.text_workheart= QLabel(txt_workheart)

       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.text_index, alignment = Qt.AlignCenter)
       self.layout_line.addWidget(self.text_workheart, alignment = Qt.AlignCenter)
       self.setLayout(self.layout_line)