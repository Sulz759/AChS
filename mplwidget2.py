# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt

from ACS import calc_A


class PlotWidget_2(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget_2, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        fig, self.axes = plt.subplots(figsize=(13.5,6),nrows=1, ncols=1, dpi=65, facecolor = 'white', frameon = True)
        self.canvas = FigureCanvas(fig)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot_2(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            file_path = fname
            self.axes.clear()
            t,A = calc_A(file_path)
            self.axes.plot(t, A)
            self.axes.set_xlabel('Время, с', fontsize=14)
            self.axes.set_ylabel('Амплитуда, В', fontsize=14)
            self.axes.grid(True, c='lightgrey', alpha=0.5)
            graph_legend = ['АЧС']
            self.axes.legend(graph_legend, loc='best', fontsize=10)
            self.canvas.draw()
        except FileNotFoundError:
            return
