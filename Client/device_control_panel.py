from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import clientsocket

celcius = True

class DeviceControlPanel(QFrame):
    def __init__(self, parent):
        super(DeviceControlPanel, self).__init__()
        self.parent = parent
        self.setFixedSize(250,400)

        self.display_status = False

        self.layout = QVBoxLayout()

        self.temperature_select_lbl = QLabel("Toggle Temperature")
        self.temperature_select_lbl.setAlignment(Qt.AlignCenter)
        self.temperature_select_lbl.setFixedSize(200, 30)
        self.temperature_select_lbl.setStyleSheet(
            "font: 87 13pt \"Segoe UI Black\";"
            "color: rgb(246, 246, 246);"
        )

        self.temperature_select_btn = QPushButton('°C')
        self.temperature_select_btn.setFixedSize(50, 50)
        self.temperature_select_btn.clicked.connect(self.temperature_btn_press)
        self.temperature_select_btn.setStyleSheet(
            "QPushButton{"
            "   font: 14pt \"Segoe UI Symbol\";"
            "   color: rgb(255, 255, 255);"
            "   background-color: rgb(30, 34, 36);"
            "   border-radius: 25px;"
            "   border: 3px solid rgb(30, 34, 36);"
            "}"
            "QPushButton:hover{"
            "   font: bold 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(246, 246, 246);"
            "   border-radius: 25px;"
            "   border: 3px solid rgb(30, 34, 36);"
            "}"
            "QPushButton:pressed{"
            "   font: bold 14pt \"Segoe UI Symbol\";"
            "   color: rgb(30,34,36);"
            "   background-color: rgb(153, 170, 181);"
            "   border-radius: 25px;"
            "   border: 3px solid rgb(30, 34, 36);"
            "}"
        )

        self.status_lbl = QLabel("Temperature Status\n(°C)")
        self.status_lbl.setAlignment(Qt.AlignCenter)
        self.status_lbl.setFixedSize(200,42)
        self.status_lbl.setStyleSheet(
            "font: 87 13pt \"Segoe UI Black\";"
            "color: rgb(246, 246, 246);"
        )

        self.status = QLineEdit()
        self.status.setText(str("{:.1f}".format(clientsocket.get_temp())))
        self.status.setReadOnly(True)
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setFixedSize(110, 40)
        self.status.setStyleSheet(
            "background-color: rgb(246, 246, 246);"
            "color: red;"
            "border: 2px solid rgb(30, 34, 36);"
            "font: 87 18pt \"Segoe UI Black\";"
        )
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.status_update)
        self.timer.start()

        self.layout.addWidget(self.temperature_select_lbl, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.temperature_select_btn, alignment=Qt.AlignCenter)
        self.layout.addStretch(0)
        self.layout.addWidget(self.status_lbl, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.status, alignment=Qt.AlignCenter)
        self.layout.addStretch(0)
        self.setLayout(self.layout)

    def display_btn_press(self):
        if self.display_status == False:
            self.display_toggle_btn.setStyleSheet(
                "QPushButton{"
                "   font: 14pt \"Segoe UI Symbol\";"
                "   color: rgb(255, 255, 255);"
                "   background-color: green;"
                "   border-radius: 25px;"
                "   border: 3px solid rgb(30, 34, 36);"
                "}"
                "QPushButton:hover{"
                "   font: bold 14pt \"Segoe UI Symbol\";"
                "   color: rgb(30,34,36);"
                "   background-color: rgb(77, 166, 77);"
                "   border-radius: 25px;"
                "   border: 3px solid rgb(30, 34, 36);"
                "}"
                "QPushButton:pressed{"
                "   font: bold 14pt \"Segoe UI Symbol\";"
                "   color: rgb(30,34,36);"
                "   background-color: rgb(26, 141, 26);"
                "   border-radius: 25px;"
                "   border: 3px solid rgb(30, 34, 36);"
                "}"
            )
            self.display_status = True
        else:
            self.display_toggle_btn.setStyleSheet(
                "QPushButton{"
                "   font: 14pt \"Segoe UI Symbol\";"
                "   color: rgb(255, 255, 255);"
                "   background-color: red;"
                "   border-radius: 25px;"
                "   border: 3px solid rgb(30, 34, 36);"
                "}"
                "QPushButton:hover{"
                "   font: bold 14pt \"Segoe UI Symbol\";"
                "   color: rgb(30,34,36);"
                "   background-color: rgb(255, 104, 106);"
                "   border-radius: 25px;"
                "   border: 3px solid rgb(30, 34, 36);"
                "}"
                "QPushButton:pressed{"
                "   font: bold 14pt \"Segoe UI Symbol\";"
                "   color: rgb(30,34,36);"
                "   background-color: rgb(255, 61, 63);"
                "   border-radius: 25px;"
                "   border: 3px solid rgb(30, 34, 36);"
                "}"
            )
            self.display_status = False

    def temperature_btn_press(self):
        if self.temperature_select_btn.text() == '°C':
            self.temperature_select_btn.setText('°F')
            self.status_lbl.setText('Temperature Status\n(°F)')
            set_celcius(False)
        else:
            self.temperature_select_btn.setText('°C')
            self.status_lbl.setText('Temperature Status\n(°C)')
            set_celcius(True)

    def status_update(self):

        celsius = clientsocket.get_temp()
        fahrenheit = CtoF(celsius)
        if (clientsocket.get_temp() == -1000):
            self.status.setText("ERROR")
        else:
            if(get_celcius()):
                self.status.setText(str("{:.1f}".format(celsius)))
            else:
                self.status.setText(str("{:.1f}".format(fahrenheit)))


def set_celcius(bool):
    global celcius
    celcius = bool

def get_celcius():
    return celcius
def CtoF(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit