from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from title_bar import TitleBar

class ControlPanel(QWidget):
    def __init__(self):
        super(ControlPanel, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(TitleBar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setMinimumSize(1200,720)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(153, 170, 181, 255), stop:0.431818 rgba(153, 170, 181, 255), stop:0.727273 rgba(100, 110, 117, 255), stop:0.965909 rgba(44, 47, 51, 255), stop:1 rgba(35, 39, 42, 255));")
        self.pressing = False