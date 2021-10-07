import sys
import socket
from PyQt5 import QtWidgets
from control_panel import ControlPanel
from clientsocket import set_sock
from twilio.rest import Client
import twilio_trigger


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.20.10.12", 1242))
    set_sock(s)

    
    account_sid = 'ACa62404846b80019bfc75dc5c3503db23'
    auth_token = '73a1a917e8b0592710ea2fa7e9c58f2e'

    client = Client(account_sid, auth_token)
    twilio_trigger.setClient(client)

    app = QtWidgets.QApplication(sys.argv)
    gui = ControlPanel()
    gui.show()
    sys.exit(app.exec_())