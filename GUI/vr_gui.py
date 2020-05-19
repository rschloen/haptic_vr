#!/usr/bin/env python3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
from vr_gui_layout import Ui_MainWindow
from VR_NFC import VR_PRTCL

"""QSlider::groove:vertical{
	border: 1px solid black;
	background: white;
	width: 5px;
	border-radius:4px;
}
QSlider::add-page:vertical{
	background: rgb(48, 50, 198);
	border: 1px solid black;
	width: 5px;
	border-radius:4px;
}
QSlider::sub-page:vertical{
	background: white;
	border: 1px solid black;
	width: 5px;
	border-radius:4px;
}
QSlider::handle:vertical{
	height: 10px;
	margin-left:  -6px;
	margin-right: -6px;
	border: 1px solid black;
	border-radius:4px;
	backgound-color: black;

}"""

class MainWindow(QtWidgets.QMainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialization
        self.vr = VR_PRTCL()

        # Settings
        self.ui.connect_button.clicked.connect(lambda:self.vr.connect(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        self.ui.read_uuid.clicked.connect(lambda:self.vr.get_inventory(self.ui.UID))
        self.ui.rf_power.valueChanged.connect(lambda:self.vr.set_RFpower(self.ui.rf_power.value(),self.ui.rf_power_text))

        # Setting Opertating Mode
        self.ui.pulse_mode.valueChanged.connect(lambda:self.vr.set_OP_Mode(self.ui.pulse_mode.value(),1))
        self.ui.hf_mod.toggled.connect(lambda:self.vr.set_OP_Mode(self.ui.hf_mod.isChecked(),2))
        self.ui.lf_mod.toggled.connect(lambda:self.vr.set_OP_Mode(self.ui.lf_mod.isChecked(),3))

        # Setting High(h) and Low(l) Duty Cycle
        self.ui.h_dc.valueChanged.connect(lambda:self.vr.set_ACT_intensity(self.ui.h_dc.value(),'high'))
        self.ui.h_dc.valueChanged.connect(lambda:self.ui.h_dc_text.setText("Intensity: {} %".format(self.ui.h_dc.value())))
        self.ui.l_dc.valueChanged.connect(lambda:self.vr.set_ACT_intensity(self.ui.l_dc.value(),'low'))
        self.ui.l_dc.valueChanged.connect(lambda:self.ui.l_dc_text.setText("Intensity: {} %".format(self.ui.l_dc.value())))

        # Setting High(H) and Low(L) frequency (period)
        self.ui.pulse_Hfreq.valueChanged.connect(lambda:self.vr.set_pulse_freq(self.ui.pulse_Hfreq.value(),'high'))
        self.ui.pulse_Hfreq.valueChanged.connect(lambda:self.ui.pulse_Hfreq_text.setText("Pulsing Frequency: {} units".format(self.ui.pulse_Hfreq.value())))
        self.ui.pulse_Lfreq.valueChanged.connect(lambda:self.vr.set_pulse_freq(self.ui.pulse_Lfreq.value(),'low'))
        self.ui.pulse_Lfreq.valueChanged.connect(lambda:self.ui.pulse_Lfreq_text.setText("Repeated Pulse Frequency: {} units".format(self.ui.pulse_Lfreq.value())))

        # Setting Single pulse duration
        self.ui.single_pulse_dur_text.editingFinished.connect(lambda:self.vr.set_one_pulse_duration(self.ui.single_pulse_dur_text.text()))
        self.ui.pulse_duration.valueChanged.connect(lambda:self.vr.set_one_pulse_duration(self.ui.pulse_duration.value()))
        self.ui.pulse_duration.valueChanged.connect(lambda:self.ui.single_pulse_dur_text.setText("{}".format(self.ui.pulse_duration.value())))


        # Actuators
        self.ui.all_off.clicked.connect(lambda:self.vr.Alloff())
        self.ui.preset_button1.clicked.connect(lambda:self.vr.set_ACT_state(self.ui.Act1,'Preset1'))

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
