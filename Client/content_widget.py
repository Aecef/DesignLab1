from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from twilio_widget import TwilioWidget
from plot_widget import PlotWidget
from device_control_panel import DeviceControlPanel

class ContentWidget(QWidget):
    def __init__(self, parent):
        super(ContentWidget, self).__init__()
        self.parent = parent
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setFixedSize(1200,690)
        self.setStyleSheet(
            "QWidget{"
            "   background-color: rgb(46, 60, 80);"
            "}"
        )

        self.layout.addWidget(TwilioWidget(self))
        self.layout.addWidget(PlotWidget(self))
        self.layout.addWidget(DeviceControlPanel(self))
        self.layout.addStretch()
        self.setLayout(self.layout)

        self.pressing = False