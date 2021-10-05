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
from clientsocket import get_temp,temp_update

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

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]

        self._plot_ref = None
        self.update_plot()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def update_plot(self):
        # Updates Temp
        #temp_update()

        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [get_temp()]

        # Note: we no longer need to clear the axis.
        if self._plot_ref is None:
            # First time we have no plot reference, so do a normal plot.
            # .plot returns a list of line <reference>s, as we're
            # only getting one we can take the first element.
            plot_refs = self.canvas.axes.plot(self.xdata, self.ydata, 'r')
            self._plot_ref = plot_refs[0]
        else:
            # We have a reference, we can use it to update the data for that line.
            self._plot_ref.set_ydata(self.ydata)

        # Trigger the canvas to update and redraw.
        self.canvas.draw()


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_xlabel("Time (sec)")
        self.axes.set_ylabel("Temperature (°C)")
        super(MplCanvas, self).__init__(fig)
