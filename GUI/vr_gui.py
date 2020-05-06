#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
from vr_gui_layout import Ui_MainWindow
from VR_NFC import VR_PRTCL

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 267px;}")
        self.ui.tab_position.setStyleSheet("QTabBar::tab { height: 100px; width: 100px;}")

        self.vr = VR_PRTCL()
        self.ui.rf_power.valueChanged.connect(lambda:self.vr.set_RFpower(self.ui.rf_power.value(),self.ui.rf_power_text))
        self.ui.haptic_intensity.valueChanged.connect(lambda:self.vr.set_ACT_intensity(self.ui.haptic_intensity.value(),self.ui.haptic_int_text))
        self.ui.pulse_freq.valueChanged.connect(lambda:self.ui.pulse_freq_text.setText("Pulse Frequency: {} units".format(self.ui.pulse_freq.value())))
        self.ui.pulse_sensitivity.valueChanged.connect(lambda:self.ui.pulse_sens_text.setText("Pulse Sensitivity: {} units".format(self.ui.pulse_sensitivity.value())))
        self.ui.connect_button.clicked.connect(lambda:self.vr.connect())
        self.ui.disconnect.clicked.connect(lambda:self.vr.disconnect())



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
