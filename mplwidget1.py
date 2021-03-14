# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt
from dataread import data_read


class PlotWidget(QWidget):

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent)  # Инициализируем экземпляр

        self.initUi()  # Строим интерфейс

    def initUi(self):
        self.mainLayout = QVBoxLayout(self)

        fig, self.axes = plt.subplots(figsize=(13.5,6),nrows=1, ncols=1, dpi=65, facecolor = 'white', frameon = True)
        self.canvas = FigureCanvas(fig)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            file_path = fname
            self.axes.clear()
            znone_zntwo = data_read(file_path)
            # рисование точек
            self.axes.scatter(znone_zntwo[0], znone_zntwo[1], marker='o', s=30, edgecolor='#268559', facecolor='black')
            # верхний заголовок
            # self.axes.set_title('Первый = второй', fontsize=14)
            # подпись оси Х
            self.axes.set_xlabel('Время, с', fontsize=14)
            # подпись оси У
            self.axes.set_ylabel('Lam(t)', fontsize=14)
            # размер оси х
            # self.axes.set_xlim(0, 830)
            # # размер оси y
            # self.axes.set_ylim(-300, 300)
            # вид графика (логарифмический для этого случая)
            # self.axes.set_yscale('log')
            # сетка
            self.axes.grid(True, c='lightgrey', alpha=0.5)
            # легенда графика (табличка с информацией)
            graph_legend = ['Привязка ко времени']
            self.axes.legend(graph_legend, loc='best', fontsize=10)
            self.canvas.draw()
        except FileNotFoundError:
            return


