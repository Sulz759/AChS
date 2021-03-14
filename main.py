import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from GUI import Ui_MainWindow
from calc import *
from mplwidget1 import PlotWidget
from mplwidget2 import PlotWidget_2


class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        self.canva = PlotWidget(self.plotWidget)
        self.canva_2 = PlotWidget_2(self.plotWidget_2)
        self.pushButton.clicked.connect(self.canva.plot)
        self.pushButton_3.clicked.connect(self.canva_2.plot_2)
        self.pushButton_2.clicked.connect(self.calc_params)
    def calc_params(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
            file_path = fname
            self.lineEdit.setText(str(average_calc(file_path)))
            self.lineEdit_2.setText(str(disp_calc(file_path)))
            self.lineEdit_3.setText(str(sko_calc(disp_calc(file_path))))
            self.lineEdit_4.setText(str(max_calc(file_path)))
            self.lineEdit_5.setText(str(apparent_frequency_calc(file_path)))
        except FileNotFoundError:
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = GUI()
    prog.show()
    sys.exit(app.exec_())