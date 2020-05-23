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

}
QTabBar::tab:last {
	border-image: url(/home/rschloen/haptic_vr/GUI/preset_chest.png);
}"""

class MainWindow(QtWidgets.QMainWindow):
    prev_active_ACT = []

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialization
        self.vr = VR_PRTCL()
        self.all_ACT = [0,self.ui.Act1,self.ui.Act2,self.ui.Act3,self.ui.Act4,self.ui.Act5,self.ui.Act6,self.ui.Act7,self.ui.Act8,self.ui.Act9,self.ui.Act10,self.ui.Act11
        ,self.ui.Act12,self.ui.Act13,self.ui.Act14,self.ui.Act15,self.ui.Act16,self.ui.Act17,self.ui.Act18,self.ui.Act19,self.ui.Act20,self.ui.Act21,self.ui.Act22,self.ui.Act23
        ,self.ui.Act24,self.ui.Act25,self.ui.Act26,self.ui.Act27,self.ui.Act28,self.ui.Act29,self.ui.Act30,self.ui.Act31,self.ui.Act32,self.ui.Act33,self.ui.Act34,self.ui.Act35,self.ui.Act36]
        self.hex_button()
        # Settings
        self.ui.connect_button.clicked.connect(lambda:self.vr.connect(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        self.ui.connect_button.clicked.connect(lambda:self.connect_device(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        self.ui.read_uuid.clicked.connect(lambda:self.vr.get_inventory())
        self.ui.read_uuid.clicked.connect(lambda:self.ui.UID_label.setText('UID:  {}'.format(self.vr.UID_corrected)))

        self.ui.rf_power.valueChanged.connect(lambda:self.vr.set_RFpower(self.ui.rf_power.value(),self.ui.rf_power_text))

        # Setting Opertating Mode
        self.ui.pulse_mode.valueChanged.connect(lambda:self.vr.set_OP_Mode(self.ui.pulse_mode.value(),1))
        self.ui.hf_mod.toggled.connect(lambda:self.vr.set_OP_Mode(self.ui.hf_mod.isChecked(),2))
        self.ui.lf_mod.toggled.connect(lambda:self.vr.set_OP_Mode(self.ui.lf_mod.isChecked(),3))

        # Setting Actuator Mode
        # self.ui.multi_modal.valueChanged.connect(lambda:self.vr.set_ACT_Mode(self.ui.multi_modal.value()))
        self.ui.multi_modal.valueChanged.connect(lambda:self.set_multi_modal(self.ui.multi_modal.value()))
        self.ui.active_selected.clicked.connect(lambda:self.vr.set_ACT_state(0))

        # Setting High(h) and Low(l) Duty Cycle
        self.ui.h_dc.valueChanged.connect(lambda:self.vr.set_ACT_intensity(self.ui.h_dc.value(),'high'))
        self.ui.h_dc.valueChanged.connect(lambda:self.ui.h_dc_text.setText("Intensity: {} %".format(self.ui.h_dc.value())))
        self.ui.l_dc.valueChanged.connect(lambda:self.vr.set_ACT_intensity(self.ui.l_dc.value(),'low'))
        self.ui.l_dc.valueChanged.connect(lambda:self.ui.l_dc_text.setText("Intensity: {} %".format(self.ui.l_dc.value())))

        # Setting High(H) and Low(L) frequency (period)
        self.ui.pulse_Hfreq.valueChanged.connect(lambda:self.vr.set_pulse_freq(self.ui.pulse_Hfreq.value(),'high'))
        self.ui.pulse_Hfreq.valueChanged.connect(lambda:self.ui.pulse_Hfreq_text.setText("Pulsing Frequency: {} Hz".format(self.ui.pulse_Hfreq.value())))
        self.ui.pulse_Lfreq.valueChanged.connect(lambda:self.vr.set_pulse_freq(self.ui.pulse_Lfreq.value(),'low'))
        self.ui.pulse_Lfreq.valueChanged.connect(lambda:self.ui.pulse_Lfreq_text.setText("Repeated Pulse Frequency: {} Hz".format(self.ui.pulse_Lfreq.value())))

        # Setting Single pulse duration
        self.ui.single_pulse_dur_text.editingFinished.connect(lambda:self.vr.set_one_pulse_duration(self.ui.single_pulse_dur_text.text()))
        self.ui.pulse_duration.valueChanged.connect(lambda:self.vr.set_one_pulse_duration(self.ui.pulse_duration.value()))
        self.ui.pulse_duration.valueChanged.connect(lambda:self.ui.single_pulse_dur_text.setText("{}".format(self.ui.pulse_duration.value())))

        self.ui.set_time.clicked.connect(lambda:self.vr.set_Timing())
        self.ui.set_time.clicked.connect(lambda:self.display_ACT('alloff'))

        # Presets
        self.ui.append_preset.toggled.connect(lambda:self.vr.add_to_preset(self.ui.append_preset_name.text(),self.ui.append_preset.isChecked()))
        # self.ui.tab_position.currentChanged(lambda:self.set_preset(self.ui.tab_position.currentIndex))
        self.ui.preset_button.clicked.connect(lambda:self.set_preset(self.ui.tab_position.currentIndex()))

        # Actuators
        self.ui.all_off.clicked.connect(lambda:self.vr.Alloff())
        self.ui.all_off.clicked.connect(lambda:self.display_ACT('alloff'))

        self.ui.Act1.clicked.connect(lambda:self.vr.set_ACT_state(1))
        self.ui.Act1.clicked.connect(lambda:self.display_ACT(self.ui.Act1))
        self.ui.Act2.clicked.connect(lambda:self.vr.set_ACT_state(2))
        self.ui.Act2.clicked.connect(lambda:self.display_ACT(self.ui.Act2))
        self.ui.Act3.clicked.connect(lambda:self.vr.set_ACT_state(3))
        self.ui.Act3.clicked.connect(lambda:self.display_ACT(self.ui.Act3))
        self.ui.Act4.clicked.connect(lambda:self.vr.set_ACT_state(4))
        self.ui.Act4.clicked.connect(lambda:self.display_ACT(self.ui.Act4))
        self.ui.Act5.clicked.connect(lambda:self.vr.set_ACT_state(5))
        self.ui.Act5.clicked.connect(lambda:self.display_ACT(self.ui.Act5))
        self.ui.Act6.clicked.connect(lambda:self.vr.set_ACT_state(6))
        self.ui.Act6.clicked.connect(lambda:self.display_ACT(self.ui.Act6))
        self.ui.Act7.clicked.connect(lambda:self.vr.set_ACT_state(7))
        self.ui.Act7.clicked.connect(lambda:self.display_ACT(self.ui.Act7))
        self.ui.Act8.clicked.connect(lambda:self.vr.set_ACT_state(8))
        self.ui.Act8.clicked.connect(lambda:self.display_ACT(self.ui.Act8))
        self.ui.Act9.clicked.connect(lambda:self.vr.set_ACT_state(9))
        self.ui.Act9.clicked.connect(lambda:self.display_ACT(self.ui.Act9))
        self.ui.Act10.clicked.connect(lambda:self.vr.set_ACT_state(10))
        self.ui.Act10.clicked.connect(lambda:self.display_ACT(self.ui.Act10))
        self.ui.Act11.clicked.connect(lambda:self.vr.set_ACT_state(11))
        self.ui.Act11.clicked.connect(lambda:self.display_ACT(self.ui.Act11))
        self.ui.Act12.clicked.connect(lambda:self.vr.set_ACT_state(12))
        self.ui.Act12.clicked.connect(lambda:self.display_ACT(self.ui.Act12))
        self.ui.Act13.clicked.connect(lambda:self.vr.set_ACT_state(13))
        self.ui.Act13.clicked.connect(lambda:self.display_ACT(self.ui.Act13))
        self.ui.Act14.clicked.connect(lambda:self.vr.set_ACT_state(14))
        self.ui.Act14.clicked.connect(lambda:self.display_ACT(self.ui.Act14))
        self.ui.Act15.clicked.connect(lambda:self.vr.set_ACT_state(15))
        self.ui.Act15.clicked.connect(lambda:self.display_ACT(self.ui.Act15))
        self.ui.Act16.clicked.connect(lambda:self.vr.set_ACT_state(16))
        self.ui.Act16.clicked.connect(lambda:self.display_ACT(self.ui.Act16))
        self.ui.Act17.clicked.connect(lambda:self.vr.set_ACT_state(17))
        self.ui.Act17.clicked.connect(lambda:self.display_ACT(self.ui.Act17))
        self.ui.Act18.clicked.connect(lambda:self.vr.set_ACT_state(18))
        self.ui.Act18.clicked.connect(lambda:self.display_ACT(self.ui.Act18))
        self.ui.Act19.clicked.connect(lambda:self.vr.set_ACT_state(19))
        self.ui.Act19.clicked.connect(lambda:self.display_ACT(self.ui.Act19))
        self.ui.Act20.clicked.connect(lambda:self.vr.set_ACT_state(20))
        self.ui.Act20.clicked.connect(lambda:self.display_ACT(self.ui.Act20))
        self.ui.Act21.clicked.connect(lambda:self.vr.set_ACT_state(21))
        self.ui.Act21.clicked.connect(lambda:self.display_ACT(self.ui.Act21))
        self.ui.Act22.clicked.connect(lambda:self.vr.set_ACT_state(22))
        self.ui.Act22.clicked.connect(lambda:self.display_ACT(self.ui.Act22))
        self.ui.Act23.clicked.connect(lambda:self.vr.set_ACT_state(23))
        self.ui.Act23.clicked.connect(lambda:self.display_ACT(self.ui.Act23))
        self.ui.Act24.clicked.connect(lambda:self.vr.set_ACT_state(24))
        self.ui.Act24.clicked.connect(lambda:self.display_ACT(self.ui.Act24))
        self.ui.Act25.clicked.connect(lambda:self.vr.set_ACT_state(25))
        self.ui.Act25.clicked.connect(lambda:self.display_ACT(self.ui.Act25))
        self.ui.Act26.clicked.connect(lambda:self.vr.set_ACT_state(26))
        self.ui.Act26.clicked.connect(lambda:self.display_ACT(self.ui.Act26))
        self.ui.Act27.clicked.connect(lambda:self.vr.set_ACT_state(27))
        self.ui.Act27.clicked.connect(lambda:self.display_ACT(self.ui.Act27))
        self.ui.Act28.clicked.connect(lambda:self.vr.set_ACT_state(28))
        self.ui.Act28.clicked.connect(lambda:self.display_ACT(self.ui.Act28))
        self.ui.Act29.clicked.connect(lambda:self.vr.set_ACT_state(29))
        self.ui.Act29.clicked.connect(lambda:self.display_ACT(self.ui.Act29))
        self.ui.Act30.clicked.connect(lambda:self.vr.set_ACT_state(30))
        self.ui.Act30.clicked.connect(lambda:self.display_ACT(self.ui.Act30))
        self.ui.Act31.clicked.connect(lambda:self.vr.set_ACT_state(31))
        self.ui.Act31.clicked.connect(lambda:self.display_ACT(self.ui.Act31))
        self.ui.Act32.clicked.connect(lambda:self.vr.set_ACT_state(32))
        self.ui.Act32.clicked.connect(lambda:self.display_ACT(self.ui.Act32))
        self.ui.Act33.clicked.connect(lambda:self.vr.set_ACT_state(33))
        self.ui.Act33.clicked.connect(lambda:self.display_ACT(self.ui.Act33))
        self.ui.Act34.clicked.connect(lambda:self.vr.set_ACT_state(34))
        self.ui.Act34.clicked.connect(lambda:self.display_ACT(self.ui.Act34))
        self.ui.Act35.clicked.connect(lambda:self.vr.set_ACT_state(35))
        self.ui.Act35.clicked.connect(lambda:self.display_ACT(self.ui.Act35))
        self.ui.Act36.clicked.connect(lambda:self.vr.set_ACT_state(36))
        self.ui.Act36.clicked.connect(lambda:self.display_ACT(self.ui.Act36))


    def display_ACT(self,act):
        # Controls color of buttons  in GUI based on if turn on or not
        if act == 'alloff':
            for p in self.vr.prev_act:
                # print(p)
                self.all_ACT[p].setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")
            # for ele in self.vr.ACT_ON:
                # self.all_ACT[ele].setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")
        else:
            act.setStyleSheet("""QPushButton{background-color: rgb(48, 50, 198);border: 1px soild black;}""")
            # if self.vr.ACT_Mode == '00': #single modal
            for p in self.vr.prev_act:
                # print(p)
                self.all_ACT[p].setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")

    def connect_device(self,port_label,button,UID_label):
        if self.vr.device.is_open:
            print('Connected to {}'.format(self.device.name))
            port_label.setText('Serial Port: {}'.format(self.device.name))
            button.setText('Disconnect')
        else:
            button.setText('Connect')
            port_label.setText('Serial Port: ')
            UID_label.setText('UID:  XX XX XX XX XX XX XX XX')

    def set_multi_modal(self,value):
        self.vr.set_ACT_Mode(value)
        if value == 0:
            self.ui.active_selected.setEnabled(False)
        else:
            self.ui.active_selected.setEnabled(True)

    def set_preset(self,index):
        print(index)
        if index == 0:
            self.vr.play_preset('flash all')
        elif index == 1:
            self.vr.play_preset('back_slide')
        elif index == 2:
            self.vr.play_preset('ABCs')

    def hex_button(self):
        for button in self.all_ACT:
            if button == 0:
                continue
            button.setFixedSize(QSize(50,50))
            size = button.width()
            # size = button.height()
            # size = 100
            # x = (3**.5 / 2)
            x = .9
            # print(x)
            # points = [QPoint(size/4,0),QPoint(size/4+size/2,0),QPoint(size,size*.5*x),QPoint(size/4+size/2,size*x),QPoint(size/4,size*x),QPoint(0,size*.5*x)] # points at the side
            points = [QPoint(0,size/4),QPoint(0,size/4+size/2),QPoint(size*.5*x,size),QPoint(size*x,size/4+size/2),QPoint(size*x,size/4),QPoint(size*.5*x,0)] # points at the top
            button.setMask(QRegion(QPolygon(points)))
            # break



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec_())
