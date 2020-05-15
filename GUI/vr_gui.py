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
        # print(MainWindow.geometry().width())
        # self.ui.tabWidget.setStyleSheet("QTabBar::tab { height: 30px; width: 267px;}")
        # self.ui.tab_position.setStyleSheet("QTabBar::tab { height: 100px; width: 100px;}")

        self.vr = VR_PRTCL()
        self.ui.rf_power.valueChanged.connect(lambda:self.vr.set_RFpower(self.ui.rf_power.value(),self.ui.rf_power_text))
        self.ui.haptic_intensity.valueChanged.connect(lambda:self.vr.set_ACT_intensity(self.ui.haptic_intensity.value(),self.ui.haptic_int_text))
        self.ui.pulse_freq.valueChanged.connect(lambda:self.ui.pulse_freq_text.setText("Pulse Frequency: {} units".format(self.ui.pulse_freq.value())))
        self.ui.pulse_sensitivity.valueChanged.connect(lambda:self.ui.pulse_sens_text.setText("Pulse Sensitivity: {} units".format(self.ui.pulse_sensitivity.value())))
        self.ui.connect_button.clicked.connect(lambda:self.vr.connect(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        # self.ui.disconnect.clicked.connect(lambda:self.vr.disconnect(self.ui.PORT,self.ui.UID))
        self.ui.read_uuid.clicked.connect(lambda:self.vr.get_inventory(self.ui.UID))
        self.ui.all_off.clicked.connect(lambda:self.vr.Alloff())

        # Actuators
        self.ui.Act1.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act1,1))
        self.ui.Act2.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act2,2))
        self.ui.Act3.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act3,3))
        self.ui.Act4.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act4,4))
        self.ui.Act5.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act5,5))
        self.ui.Act6.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act6,6))
        self.ui.Act7.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act7,7))
        self.ui.Act8.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act8,8))
        self.ui.Act9.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act9,9))
        self.ui.Act10.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act10,10))
        self.ui.Act11.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act11,11))
        self.ui.Act12.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act12,12))
        self.ui.Act13.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act13,13))
        self.ui.Act14.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act14,14))
        self.ui.Act15.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act15,15))
        self.ui.Act16.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act16,16))
        self.ui.Act17.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act17,17))
        self.ui.Act18.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act18,18))
        self.ui.Act19.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act19,19))
        self.ui.Act20.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act20,20))
        self.ui.Act21.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act21,21))
        self.ui.Act22.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act22,22))
        self.ui.Act23.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act23,23))
        self.ui.Act24.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act24,24))
        self.ui.Act25.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act25,25))
        self.ui.Act26.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act26,26))
        self.ui.Act27.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act27,27))
        self.ui.Act28.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act28,28))
        self.ui.Act29.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act29,29))
        self.ui.Act30.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act30,30))
        self.ui.Act31.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act31,31))
        self.ui.Act32.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act32,32))
        self.ui.Act33.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act33,33))
        self.ui.Act34.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act34,34))
        self.ui.Act35.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act35,35))
        self.ui.Act36.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act36,36))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    # print(gui.geometry().width())
    gui.show()
    sys.exit(app.exec_())
