import sys
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from Client.control_panel import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    flags = QtCore.Qt.FramelessWindowHint
    MainWindow.setWindowFlag(flags)
    MainWindow.show()
    sys.exit(app.exec_())



