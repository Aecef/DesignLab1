import sys
import socket
from PyQt5 import QtWidgets
from control_panel import ControlPanel
from clientsocket import set_sock

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("172.20.10.12", 1242))
    set_sock(s)

    app = QtWidgets.QApplication(sys.argv)
    gui = ControlPanel()
    gui.show()
    sys.exit(app.exec_())