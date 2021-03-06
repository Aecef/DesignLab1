import sys
import matplotlib
matplotlib.use('Qt5Agg')
import random
import clientsocket
import twilio_trigger

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout
import device_control_panel

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

        n_data = 300
        self.xdata = list(reversed(range(n_data)))
        self.ydata = [clientsocket.get_temp() for i in range(n_data)]
        self.ydata_f = [device_control_panel.CtoF(clientsocket.get_temp()) for i in range(n_data)]

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
        clientsocket.temp_update()
        print(clientsocket.get_temp())
        twilio_trigger.has_temp_exceeded_limits(clientsocket.get_temp())


        if (device_control_panel.get_celcius()):
            self.canvas.axes.set_ylabel("Temperature (°C)")
            self.canvas.axes.set_ylim(10, 60)

            self.ydata = self.ydata[1:] + [clientsocket.get_temp()]
            self.ydata_f = self.ydata_f[1:] + [device_control_panel.CtoF(clientsocket.get_temp())]

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
        else:
            self.canvas.axes.set_ylabel("Temperature (°F)")
            self.canvas.axes.set_ylim(50, 140)

            self.ydata = self.ydata[1:] + [clientsocket.get_temp()]
            self.ydata_f = self.ydata_f[1:] + [device_control_panel.CtoF(clientsocket.get_temp())]

            # Note: we no longer need to clear the axis.
            if self._plot_ref is None:
                # First time we have no plot reference, so do a normal plot.
                # .plot returns a list of line <reference>s, as we're
                # only getting one we can take the first element.
                plot_refs = self.canvas.axes.plot(self.xdata, self.ydata_f, 'r')
                self._plot_ref = plot_refs[0]
            else:
                # We have a reference, we can use it to update the data for that line.
                self._plot_ref.set_ydata(self.ydata_f)


        # Trigger the canvas to update and redraw.
        self.canvas.draw()


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.set_ylim(10, 60)
        self.axes.set_xlim(300, 0)
        self.axes.set_xlabel("Time (sec)")
        self.axes.set_ylabel("Temperature (°C)")
        super(MplCanvas, self).__init__(fig)
