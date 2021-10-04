from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

class TitleBar(QWidget):
    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)

        self.title = QLabel("Temperature Control Panel")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedSize(260, 30)
        self.title.setStyleSheet(
            "font: 87 14pt \"Segoe UI Black\";"
            "color: rgb(255, 255, 255);"
            "background-color: rgb(30, 34, 36);"
        )

        btn_size = 30

        self.btn_close = QPushButton("✖")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setStyleSheet("")
        self.btn_close.setStyleSheet(
            "QPushButton{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(255, 255, 255);"
            "   background-color: rgb(30, 34, 36);"
            "   border-style: outset;"
            "}"
            "QPushButton:hover{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(246, 246, 246);"
            "   border-style: solid;"
            "   border-width: 3px;"
            "   border-color: rgb(30, 34, 36);"
            "}"
            "QPushButton:pressed{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(153, 170, 181);"
            "   border-style: solid;"
            "   border-width: 3px;"
            "   border-color: rgb(30, 34, 36);"
            "}"
        )

        self.btn_min = QPushButton("🗕")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet(
            "QPushButton{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(255, 255, 255);"
            "   background-color: rgb(30, 34, 36);"
            "   border-style: outset;"
            "}"
            "QPushButton:hover{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(246, 246, 246);"
            "   border-style: solid;"
            "   border-width: 3px;"
            "   border-color: rgb(30, 34, 36);"
            "}"
            "QPushButton:pressed{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(153, 170, 181);"
            "   border-style: solid;"
            "   border-width: 3px;"
            "   border-color: rgb(30, 34, 36);"
            "}"
        )

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_close)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(TitleBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_min_clicked(self):
        self.parent.showMinimized()