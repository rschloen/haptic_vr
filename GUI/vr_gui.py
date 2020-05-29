#!/usr/bin/env python3
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
from vr_gui_layout import Ui_MainWindow
from actuator_layout import Actuator_Block
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
    last = 0
    button_list = []

    def __init__(self,screen):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.widget_list = [self.ui.label,self.ui.label_3,self.ui.multi_modal,self.ui.threeD_touch,self.ui.label_2,self.ui.single_pulse_dur_label,self.ui.single_pulse_dur_text,
        # self.ui.pulse_mode,self.ui.pulse_duration,self.ui.label_4,self.ui.hf_mod,self.ui.h_dc_text,self.ui.h_dc,self.ui.pulse_Hfreq_text,self.ui.pulse_Hfreq,self.ui.lf_mod,
        # self.ui.l_dc_text,self.ui.l_dc,self.ui.pulse_Lfreq_text,self.ui.pulse_Lfreq,self.ui.all_off,self.ui.active_selected,self.ui.set_time,self.ui.append_preset_name,self.ui.append_preset]

        self.screen_height = screen.size().height()
        self.screen_width = screen.size().width()
        self.win_height = self.size().height()
        self.win_width = self.size().width()
        # for ele in self.widget_list:
        #     ele.resize(int(.5*self.screen_width),int(.5*self.screen_height))
        self.blk1 = Actuator_Block(self,self.screen_width,'vertical',self.ui.tab_1)
        self.blk2 = Actuator_Block(self,self.screen_width,'horizontal',self.ui.tab_2)
        self.blk3 = Actuator_Block(self,self.screen_width,'horizontal',self.ui.tab_3)
        self.manual_blk = Actuator_Block(self,self.screen_width,'vertical')
        self.ui.horizontalLayout_10.addLayout(self.manual_blk.verticalLayout_3)
        self.ui.Manual.setLayout(self.ui.horizontalLayout_10)
        self.ui.tabWidget.setStyleSheet("""QTabBar::tab {{border: 2px solid black;
                                            height: {}px;
                                            width: {}px;
                                            background-color: rgb(149, 27, 218);
                                            margin: 2px;
                                            font-size:18pt}}
                                            QTabBar::tab:selected{{
                                            background-color: rgb(218, 58, 245);
                                            margin: 2px;}}
                                            QTabWidget{{
                                            background-color: rgb(149, 27, 218);}}""".format(int(.08*self.screen_height),int(self.screen_width*.326)))
        self.ui.tab_position.setStyleSheet("""QTabBar::tab {{border: 2px solid black;
                                            height: {}px;
                                            width: {}px;
                                            background-color: rgb(149, 27, 218);
                                            margin: 2px;
                                            font-size:16pt}}
                                            QTabBar::tab:selected{{
                                            background-color: rgb(218, 58, 245);
                                            margin: 2px;}}
                                            QTabWidget{{
                                            background-color: rgb(149, 27, 218);}}""".format(int(.2*self.screen_height),int(.2*self.screen_height)))
        self.manual_blk.act_blk.buttonClicked.connect(self.handle_button)
        # MainWindow.setAttribute(QtCore.Qt.WA_AcceptTouchEvents,True)
        self.installEventFilter(self)
        self.ui.tabWidget.setAttribute(QtCore.Qt.WA_AcceptTouchEvents,True)
        # Initialization
        self.vr = VR_PRTCL()
        # self.all_ACT = [0,self.ui.Act1,self.ui.Act2,self.ui.Act3,self.ui.Act4,self.ui.Act5,self.ui.Act6,self.ui.Act7,self.ui.Act8,self.ui.Act9,self.ui.Act10,self.ui.Act11
        # ,self.ui.Act12,self.ui.Act13,self.ui.Act14,self.ui.Act15,self.ui.Act16,self.ui.Act17,self.ui.Act18,self.ui.Act19,self.ui.Act20,self.ui.Act21,self.ui.Act22,self.ui.Act23
        # ,self.ui.Act24,self.ui.Act25,self.ui.Act26,self.ui.Act27,self.ui.Act28,self.ui.Act29,self.ui.Act30,self.ui.Act31,self.ui.Act32,self.ui.Act33,self.ui.Act34,self.ui.Act35,self.ui.Act36]
        # self.hex_button()
        # Settings
        self.ui.connect_button.clicked.connect(lambda:self.vr.connect(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        self.ui.connect_button.clicked.connect(lambda:self.connect_device(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        self.ui.read_uuid.clicked.connect(lambda:self.vr.get_inventory())
        self.ui.read_uuid.clicked.connect(lambda:self.ui.UID.setText('UID:  {}'.format(self.vr.UID_corrected)))

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


    def eventFilter(self,obj,event):
        if event.type() == QEvent.TouchBegin:
            return True
        elif event.type() == QEvent.TouchEnd:
            num1 = 0
            for button in self.button_list:
                print('1:{} ,2:{}'.format(num1,self.manual_blk.act_blk.id(button)))
                if self.manual_blk.act_blk.id(button) != num1:
                    print('Emit to:{}'.format(self.manual_blk.act_blk.id(button)))
                    self.manual_blk.act_blk.buttonClicked.emit(button)
                    num1 = self.manual_blk.act_blk.id(button)
                else:
                    print('skip')

            self.button_list = []
            return True
        elif event.type() == QEvent.TouchUpdate:
            points = event.touchPoints()
            button = self.manual_blk.act_blk.buttons()
            h = button[0].size().height()
            w = button[0].size().width()
            for button in self.manual_blk.act_blk.buttons():
                if button == 0: continue
                for i in range(len(points)):
                    px = points[i].screenPos().x()
                    py = points[i].screenPos().y()
                    if px >= button.mapToGlobal(QPoint(0,0)).x() and px <= button.mapToGlobal(QPoint(0,0)).x()+w and py >= button.mapToGlobal(QPoint(0,0)).y() and py <= button.mapToGlobal(QPoint(0,0)).y()+h:
                        # self.last = self.manual_blk.act_blk.id(button)
                        self.button_list.append(button)

            return True
        return super(MainWindow,self).eventFilter(obj,event)

    def handle_button(self,button):
        num = self.manual_blk.act_blk.id(button)
        # print(num)
        self.vr.set_ACT_state(num)
        self.display_ACT(num)


    def display_ACT(self,act):
        # Controls color of buttons in GUI based on if turn on or not
        # ARGS: act is int for button id
        if act == 'alloff':
            for button in self.manual_blk.act_blk.buttons():
                button.setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")
        else:
            print(act)
            if int(self.vr.OP_Mode) < 4: # Not single pulse'
                # print(self.prev_active_ACT)
                print(self.vr.ACT_ON)
                # if self.vr.ACT_Mode == '00': # if one touch
                    # if act not in self.prev_active_ACT: # if new button
                for p in self.vr.prev_act: #remove old button(s)
                    self.manual_blk.act_blk.button(p).setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")

                    #     try:
                    #     p = self.prev_active_ACT.pop()
                    #     self.manual_blk.act_blk.button(p).setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")
                    # except:
                        # print('First button')
                    # turn on new button
                for p in self.vr.ACT_ON:
                    self.manual_blk.act_blk.button(p).setStyleSheet("""QPushButton{background-color: rgb(48, 50, 198);border: 1px soild black;}""")
                    # self.prev_active_ACT.append(act)
                # else:
                #     for p in self.vr.ACT_ON:
                #         self.manual_blk.act_blk.button(p).setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")
                            # self.vr.ACT_ON.remove(p)
                        # self.manual_blk.act_blk.button(act).setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")
                        # self.prev_active_ACT.remove(act)
                # else:


            else:
                self.manual_blk.act_blk.button(act).setStyleSheet("""QPushButton{background-color: rgb(48, 50, 198);border: 1px soild black;}""")
                time.sleep(.5)
                self.manual_blk.act_blk.button(act).setStyleSheet("""QPushButton{background-color: white;border:1px solid black}""")

    def connect_device(self,port_label,button,UID_label):
        if self.vr.device.is_open:
            print('Connected to {}'.format(self.vr.device.name))
            port_label.setText('Serial Port: {}'.format(self.vr.device.name))
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
    QtWidgets.QApplication.setStyle("fusion")
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    gui = MainWindow(screen)
    gui.showMaximized()
    sys.exit(app.exec_())
