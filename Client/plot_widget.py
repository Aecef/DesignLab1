import sys
import matplotlib
matplotlib.use('Qt5Agg')
import random

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout


class PlotWidget(QFrame):
    def __init__(self, parent):
        super(PlotWidget, self).__init__()
        self.parent = parent
        self.setFixedSize(700, 600)
        self.setStyleSheet(
            "   background-color: rgb(46, 60, 80);"
        )

        self.layout = QVBoxLayout()

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
