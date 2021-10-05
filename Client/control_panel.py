from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from title_bar import TitleBar
from content_widget import ContentWidget

class ControlPanel(QWidget):
    def __init__(self):
        super(ControlPanel, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addWidget(TitleBar(self))
        self.layout.addWidget(ContentWidget(self))
        self.setLayout(self.layout)

        self.setMinimumSize(1200,720)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.pressing = False