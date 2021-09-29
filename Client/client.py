import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
from Client.control_panel import control_panel

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = control_panel()
    gui.show()
    sys.exit(app.exec_())