import sys
from PyQt5 import QtWidgets
from Client.control_panel import ControlPanel

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = ControlPanel()
    gui.show()
    sys.exit(app.exec_())