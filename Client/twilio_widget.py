from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class TwilioWidget(QFrame):
    def __init__(self, parent):
        super(TwilioWidget, self).__init__()
        self.parent = parent
        self.setFixedSize(250,400)
        self.setStyleSheet(
            "   background-color: rgb(46, 60, 80);"
        )

        self.layout = QGridLayout()

        self.phone_number_label = QLabel("Phone Number:")
        self.phone_number_label.setAlignment(Qt.AlignCenter)
        self.phone_number_label.setFixedSize(200, 30)
        self.phone_number_label.setStyleSheet(
            "font: 87 13pt \"Segoe UI Black\";"
            "color: rgb(246, 246, 246);"
        )

        self.phone_number = QLineEdit("1-800-888-8888")
        self.phone_number.setAlignment(Qt.AlignCenter)
        self.phone_number.setFixedSize(200, 30)
        self.phone_number.setStyleSheet(
            "background-color: rgb(246, 246, 246);"
            "color: rgb(30, 34, 36);"
            "border: 2px solid rgb(30, 34, 36);"
            "border-radius: 2px;"
            "font: 12pt \"Segoe UI Symbol\""
        )

        self.temp_high_label = QLabel("Maximum Temperature\n(°C):")
        self.temp_high_label.setAlignment(Qt.AlignCenter)
        self.temp_high_label.setFixedSize(200, 45)
        self.temp_high_label.setStyleSheet(
            "font: 87 13pt \"Segoe UI Black\";"
            "color: rgb(246, 246, 246);"
        )

        self.temp_high = QLineEdit("100")
        self.temp_high.setAlignment(Qt.AlignCenter)
        self.temp_high.setFixedSize(200, 30)
        self.temp_high.setStyleSheet(
            "background-color: rgb(246, 246, 246);"
            "color: rgb(30, 34, 36);"
            "border: 2px solid rgb(30, 34, 36);"
            "border-radius: 2px;"
            "font: 12pt \"Segoe UI Symbol\""
        )

        self.temp_low_label = QLabel("Minimum Temperature\n(°C)")
        self.temp_low_label.setAlignment(Qt.AlignCenter)
        self.temp_low_label.setFixedSize(200, 45)
        self.temp_low_label.setStyleSheet(
            "font: 87 13pt \"Segoe UI Black\";"
            "color: rgb(246, 246, 246);"
        )

        self.temp_low = QLineEdit("32")
        self.temp_low.setAlignment(Qt.AlignCenter)
        self.temp_low.setFixedSize(200, 30)
        self.temp_low.setStyleSheet(
            "background-color: rgb(246, 246, 246);"
            "color: rgb(30, 34, 36);"
            "border: 2px solid rgb(30, 34, 36);"
            "border-radius: 2px;"
            "font: 12pt \"Segoe UI Symbol\""
        )

        self.apply_btn = QPushButton('Apply')
        self.apply_btn.setFixedSize(175, 40)
        self.apply_btn.clicked.connect(self.apply_btn_press)
        self.apply_btn.setStyleSheet(
            "QPushButton{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(255, 255, 255);"
            "   background-color: rgb(30, 34, 36);"
            "   border-radius: 5px;"
            "   border: 2px solid rgb(30, 34, 36);"  
            "}"
            "QPushButton:hover{"
            "   font: bold 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(246, 246, 246);"
            "   border-radius: 5px;"
            "   border: 2px solid rgb(30, 34, 36);"  
            "}"
            "QPushButton:pressed{"
            "   font: bold 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(153, 170, 181);"
            "   border-radius: 5px;"
            "   border: 2px solid rgb(30, 34, 36);"  
            "}"
        )

        self.layout.addWidget(self.phone_number_label, 1, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.phone_number, 2, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.temp_high_label, 3, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.temp_high, 4, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.temp_low_label, 5, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.temp_low, 6, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.apply_btn, 7, 0, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def apply_btn_press(self):
        print("Apply")
