import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
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


def mousePressEvent(self, e):
    self.previous_pos = e.globalPos()


def mouseMoveEvent(self, e):
    delta = e.globalPos() - self.previous_pos
    self.move(self.x() + delta.x(), self.y()+delta.y())
    self.previous_pos = e.globalPos()

    self._drag_active = True


def mouseReleaseEvent(self, e):
    if self._drag_active:
        self.save()
        self._drag_active = False
