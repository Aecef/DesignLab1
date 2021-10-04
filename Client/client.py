import sys
from PyQt5 import QtWidgets
from Client.control_panel import control_panel

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = control_panel()
    gui.show()
    sys.exit(app.exec_())