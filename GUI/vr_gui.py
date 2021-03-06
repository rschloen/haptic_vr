#!/usr/bin/env python3
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys, os, threading, ast
import time
from vr_gui_layout import Ui_MainWindow
from actuator_layout import Actuator_Block
from VR_NFC import VR_PRTCL
from pyusb_VR_NFC import USB_VR_PRTCL

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
}

QGesture Class: detecting gestures"""

class MainWindow(QtWidgets.QMainWindow):
    prev_active_ACT = []
    last = 0
    button_list = []
    blk_option = []
    manual_blk = 0
    off_style_sheet = """QPushButton{background-color: white;border:1px solid black}"""
    on_style_sheet = """QPushButton{background-color: rgb(48, 50, 198);border: 1px soild black;}"""
    def __init__(self,screen):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Initialization
        # self.vr = USB_VR_PRTCL()
        self.vr = VR_PRTCL()
        self.screen_height = screen.size().height()
        self.screen_width = screen.size().width()
        self.win_height = self.size().height()
        self.win_width = self.size().width()

        # Add any existing presets as a new tab with correct block orientation
        self.tab_blk1 = Actuator_Block(self,self.screen_width,'vertical',self.ui.tab_1)
        self.tab_blk2 = Actuator_Block(self,self.screen_width,'horizontal',self.ui.tab_2)
        self.tab_blk3 = Actuator_Block(self,self.screen_width,'horizontal',self.ui.tab_3)
        self.preset_list = self.check_for_presets()
        hard_presets = [['flash_all','vertical'],['sweep','horizontal'],['2i_blk','horizontal']]
        self.preset_list = hard_presets+self.preset_list
        print(self.preset_list)
        self.preset_tabs = [QtWidgets.QWidget() for i in range(len(self.preset_list))]
        self.tab_cnt = 4 # Already 3 hardcoded presets
        self.preset_blks = [self.tab_blk1,self.tab_blk2,self.tab_blk3]
        for i in range(3,len(self.preset_list)): #loop through existing presets
            # Initialize basic widget parameters
            self.preset_tabs[i].setStyleSheet("")
            self.preset_tabs[i].setObjectName("tab_"+str(self.tab_cnt))
            self.tab_cnt+=1
            # Add widget as a new tab and set text per file name
            self.ui.tab_position.addTab(self.preset_tabs[i], "")
            self.ui.tab_position.setTabText(self.ui.tab_position.indexOf(self.preset_tabs[i]),self.preset_list[i][0])
            # Add actuator block of correct orientation
            self.preset_blks.append(Actuator_Block(self,self.screen_width,self.preset_list[i][1],self.preset_tabs[i]))
        print(self.preset_blks)



        self.blk_vert_manual = QWidget()
        self.blk_horz_manual = QWidget()
        self.manual_vert_blk = Actuator_Block(self,self.screen_width,'vertical',self.blk_vert_manual)
        self.manual_horz_blk = Actuator_Block(self,self.screen_width,'horizontal',self.blk_horz_manual)
        self.blk_option.append(self.manual_horz_blk)
        self.blk_option.append(self.manual_vert_blk)

        self.ui.act_blocks.insertWidget(0,self.blk_horz_manual)
        self.ui.act_blocks.insertWidget(1,self.blk_vert_manual)

        self.ui.Manual.setLayout(self.ui.horizontalLayout_10)
        self.ui.block_options.setCurrentRow(0)
        self.ui.act_blocks.setCurrentIndex(0)
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
        # self.blk_option[self.manual_blk].act_blk.buttonClicked.connect(self.handle_button)
        self.handle_actuator_blk(self.manual_blk)
        # MainWindow.setAttribute(QtCore.Qt.WA_AcceptTouchEvents,True)
        # self.ui.setAttribute(QtCore.Qt.WA_AcceptTouchEvents,True)

        self.installEventFilter(self)
        self.ui.tabWidget.setAttribute(QtCore.Qt.WA_AcceptTouchEvents,True)
        self.ui.PORT.setText('No device')
        self.ui.UID.setText('UID:  XX XX XX XX XX XX XX XX')


        # Settings
        self.ui.connect_button.clicked.connect(lambda:self.handle_connect_device(self.ui.PORT,self.ui.connect_button,self.ui.UID))
        self.ui.read_uuid.clicked.connect(lambda:self.vr.get_inventory())
        self.ui.read_uuid.clicked.connect(lambda:self.ui.UID.setText('UID:  {}'.format(self.vr.UID_corrected))) #pyserial
        # self.ui.read_uuid.clicked.connect(lambda:self.ui.UID.setText('UID:  {}'.format(self.vr.UID))) #pyusb


        self.ui.rf_power.valueChanged.connect(lambda:self.handle_rf_power(self.ui.rf_power.value(),self.ui.rf_power_text))

        # Setting Opertating Mode
        self.ui.single_pulse_mode.clicked.connect(lambda:self.vr.set_OP_Mode(1,1))
        self.ui.cont_pulse_mode.clicked.connect(lambda:self.vr.set_OP_Mode(0,1))
        # self.ui.pulse_mode.valueChanged.connect(lambda:self.vr.set_OP_Mode(self.ui.pulse_mode.value(),1))
        self.ui.hf_mod.toggled.connect(lambda:self.vr.set_OP_Mode(self.ui.hf_mod.isChecked(),2))
        self.ui.lf_mod.toggled.connect(lambda:self.vr.set_OP_Mode(self.ui.lf_mod.isChecked(),3))

        # Setting Actuator Mode
        # self.ui.multi_modal.valueChanged.connect(lambda:self.vr.set_ACT_Mode(self.ui.multi_modal.value()))
        self.ui.multi_modal.toggled.connect(lambda:self.handle_multi_modal(self.ui.multi_modal.isChecked()))
        self.ui.active_selected.clicked.connect(lambda:self.handle_selection())

        # Setting High(h) and Low(l) Duty Cycle
        self.ui.h_dc.valueChanged.connect(lambda:self.handle_timing('intensity',self.ui.h_dc.value(),'high',self.ui.h_dc_text))
        self.ui.l_dc.valueChanged.connect(lambda:self.handle_timing('intensity',self.ui.l_dc.value(),'low',self.ui.l_dc_text))
            # Used for preset timing control
        # self.ui.sweep_intensity.editingFinished.connect(lambda:self.handle_timing('intensity',self.ui.sweep_intensity.text(),'high',None))
        # self.ui.i2_intensity.editingFinished.connect(lambda:self.handle_timing('intensity',self.ui.i2_intensity.text(),'high',None))

        # Setting High(H) and Low(L) frequency (period)
        self.ui.pulse_Hfreq.valueChanged.connect(lambda:self.handle_timing('freq',self.ui.pulse_Hfreq.value(),'high',self.ui.pulse_Hfreq_text))
        self.ui.pulse_Lfreq.valueChanged.connect(lambda:self.handle_timing('freq',self.ui.pulse_Lfreq.value(),'low',self.ui.pulse_Lfreq_text))

        # Setting Single pulse duration
        self.ui.single_pulse_dur_text.editingFinished.connect(lambda:self.handle_timing('pulse',self.ui.single_pulse_dur_text.text(),'on',self.ui.single_pulse_dur_text))
        self.ui.pulse_duration.valueChanged.connect(lambda:self.handle_timing('pulse',self.ui.pulse_duration.value(),'on',self.ui.single_pulse_dur_text))

            # Used for preset timing control
        # self.ui.sweep_pulseTime.editingFinished.connect(lambda:self.handle_timing('pulse',self.ui.sweep_pulseTime.text(),'on',None))
        # self.ui.sweep_pauseTime.editingFinished.connect(lambda:self.handle_timing('pulse',self.ui.sweep_pauseTime.text(),'off',None))
        # self.ui.i2_pulseTime.editingFinished.connect(lambda:self.handle_timing('pulse',self.ui.i2_pulseTime.text(),'on',None))
        # self.ui.i2_pauseTime.editingFinished.connect(lambda:self.handle_timing('pulse',self.ui.i2_pauseTime.text(),'off',None))

        self.ui.set_time.clicked.connect(lambda:self.vr.set_Timing())
        self.ui.set_time.clicked.connect(lambda:self.display_ACT())
            # Used for preset timing control
        # self.ui.sweep_set_time.clicked.connect(lambda:self.vr.set_Timing())
        # self.ui.sweep_set_time.clicked.connect(lambda:self.display_ACT())
        # self.ui.i2_set_time.clicked.connect(lambda:self.vr.set_Timing())
        # self.ui.i2_set_time.clicked.connect(lambda:self.display_ACT())
        # Presets
        self.ui.append_preset.toggled.connect(lambda:self.handle_append_preset())
        self.ui.del_preset.clicked.connect(lambda:self.handle_delete_preset())
        self.ui.preset_button.clicked.connect(lambda:self.handle_preset(self.ui.tab_position.currentIndex()))


        # Actuators
        self.ui.all_off.clicked.connect(self.handle_Alloff)
        self.ui.block_options.currentRowChanged.connect(self.handle_actuator_blk)
        gesture_list = [Qt.SwipeGesture, Qt.PanGesture, Qt.PinchGesture,Qt.TapGesture,Qt.TapAndHoldGesture]
        for gesture in gesture_list:
            self.ui.centralwidget.grabGesture(gesture)
        self.px_begin = []
        self.px_end = []
        self.py_begin = []
        self.py_end = []

    def eventFilter(self,obj,event):
        if self.ui.tabWidget.currentIndex() == 0:
            if event.type() == QEvent.TouchBegin:
                return True
            elif event.type() == QEvent.TouchEnd:
                num1 = 0
                for i in range(len(self.button_list)):
                    for button in self.button_list[i]:
                        print('1:{} ,2:{}'.format(num1,self.blk_option[self.manual_blk].act_blk.id(button)))
                        if self.blk_option[self.manual_blk].act_blk.id(button) != num1:
                            print('Emit to:{}'.format(self.blk_option[self.manual_blk].act_blk.id(button)))
                            self.blk_option[self.manual_blk].act_blk.buttonClicked.emit(button)
                            num1 = self.blk_option[self.manual_blk].act_blk.id(button)
                        else:
                            print('skip')
                self.button_list = []
                return True
            elif event.type() == QEvent.TouchUpdate:
                points = event.touchPoints()
                button = self.blk_option[self.manual_blk].act_blk.buttons()
                h = button[0].size().height()
                w = button[0].size().width()
                for button in self.blk_option[self.manual_blk].act_blk.buttons():
                    if button == 0: continue
                    for i in range(len(points)):
                        self.button_list.append([])
                        px = points[i].screenPos().x()
                        py = points[i].screenPos().y()
                        if px >= button.mapToGlobal(QPoint(0,0)).x() and px <= button.mapToGlobal(QPoint(0,0)).x()+w and py >= button.mapToGlobal(QPoint(0,0)).y() and py <= button.mapToGlobal(QPoint(0,0)).y()+h:
                            # self.last = self.blk_option[self.manual_blk].act_blk.id(button)
                            self.button_list[i].append(button)
                return True
        else:
            if event.type() == QEvent.Gesture or event.type() == QEvent.GestureOverride:
                print('Gesture Event')
                return True
            elif event.type() == QEvent.TouchBegin:
                points = event.touchPoints()
                # print(points)
                for i in range(len(points)): # make px/py a list for multiple touchpoints
                    self.px_begin = points[i].screenPos().x()
                    self.py_begin = points[i].screenPos().y()
                print(self.px_begin)
                return True
            # elif event.type() == QEvent.TouchUpdate:
            #     points = event.touchPoints()
            #     # print(points)
            #     for i in range(len(points)): # make px/py a list for multiple touchpoints
            #         self.px_begin.append(points[i].screenPos().x())
            #         self.py_begin.append(points[i].screenPos().y())
            #     print(self.px_begin)

            elif event.type() == QEvent.TouchEnd:
                points = event.touchPoints()
                print(points)
                # print(self.px_begin)
                # self.px_begin = self.px_begin[:2]
                # self.py_begin = self.py_begin[:2]
                # print(self.px_begin)
                for i in range(len(points)):
                    self.px_end = points[i].screenPos().x()
                    self.py_end = points[i].screenPos().y()
                self.get_gesture()
        return super(MainWindow,self).eventFilter(obj,event)

    def get_gesture(self):
        dx = []
        dy = []
        # dx1 = 0
        # dy1 = 0
        # print(self.px_begin)
        # for i in range(len(self.px_begin)):
        print('Start:{} End:{}'.format(self.px_begin,self.px_end))
        dx = self.px_end - self.px_begin #negative is LR, positive is RL
        dy = self.py_end - self.py_begin #negative is TB, positive is BT
        print('dx:{} dy:{}'.format(dx,dy))
        index = self.ui.tab_position.currentIndex()
        # self.px_begin = []
        # self.px_end = []
        # self.py_begin = []
        # self.py_end = []
        # dx = dx[0]
        # dy = dy[0]
        # if len(dx) > 1:
        #     dx1 = dx[1]
        #     dy1 = dy[1]
        if index == 1:
            self.vr.set_one_pulse_duration(300,'on') #Move timing to be set when selecting a preset tab
            self.vr.set_Timing()
            if dx > 0 and abs(dy) < 75:
                print('LR')
                option = 0
            elif dx < 0 and abs(dy) < 75:
                print('RL')
                option = 1
            elif dy > 0 and abs(dx) < 75:
                print('TB')
                option = 2
            elif dy < 0 and abs(dx) < 75:
                print('BT')
                option = 3
            elif dx > 0 and dy < 0:
                print('+45BT')
                option = 4
            elif dx < 0 and dy > 0:
                print('+45TB')
                option = 5
            elif dx < 0 and dy < 0:
                print('-45BT')
                option = 6
            elif dx > 0 and dy > 0:
                print('-45TB')
                option = 7

            thread = threading.Thread(target=self.display_preset,args=(index,option))
            thread.start()
            self.vr.play_preset('sweep',option)


    def handle_connect_device(self,port_label,button,UID_label):
        self.vr.connect()
        # '''pyusb'''
        # if self.vr.active_flag:
        #     print('Connected to idVendor:{},idProduct:{}'.format(self.vr.device[0],self.vr.device[1]))
        #     port_label.setText('idVendor:{},idProduct:{}'.format(self.vr.device[0],self.vr.device[1]))
        '''pyserial'''
        if self.vr.device.is_open:
            print('Connected to {}'.format(self.vr.device.name))
            port_label.setText('Serial Port: {}'.format(self.vr.device.name))

            button.setText('Disconnect')
        else:
            button.setText('Connect')
            port_label.setText('No device')
            UID_label.setText('UID:  XX XX XX XX XX XX XX XX')


    def handle_rf_power(self,power,text):
        self.vr.set_RFpower(power)
        text.setText(("{} Watts").format(power))


    def handle_multi_modal(self,value):
        self.vr.set_ACT_Mode(value)
        if value == 0:
            self.ui.active_selected.setEnabled(False)
        else:
            self.ui.active_selected.setEnabled(True)

    def handle_selection(self):
        self.vr.set_ACT_state(0)
        print(self.vr.t_pulse)
        print(int(self.vr.t_pulse[2:]+self.vr.t_pulse[0:2],16)/1000)
        if int(self.vr.OP_Mode) >= 4:
            time.sleep(int(self.vr.t_pulse[2:]+self.vr.t_pulse[0:2],16)/1000)
            for p in self.vr.ACT_ON:
                self.blk_option[self.manual_blk].act_blk.button(p).setStyleSheet(self.off_style_sheet)
            self.vr.ACT_ON = []


    def handle_timing(self,mode,value,level,text):
        print(mode)
        if mode == 'pulse':
            print('pulse')
            print(value)
            print(level)
            self.vr.set_one_pulse_duration(value,level)
            self.ui.pulse_duration.setValue(int(value))
            if text != None:
                text.setText("{}".format(value))
        if mode == 'intensity':
            print('intensity')
            print(value)
            print(level)
            self.vr.set_ACT_intensity(value,level)
            if text != None:
                text.setText("Intensity: {} %".format(value))
        if mode == 'freq':
            print('freq')
            print(value)
            print(level)
            self.vr.set_pulse_freq(value,level)
            if text != None:
                if level == 'high':
                    text.setText("Pulsing Frequency:\n {} Hz".format(value))
                else:
                    text.setText("Repeated Pulse\nFrequency: {} Hz".format(value))


    def handle_append_preset(self):
        name = self.ui.append_preset_name.text()
        orientation = self.blk_option[self.manual_blk].orientation
        new_preset = True
        for preset in self.preset_list:
            if name == preset[0]:
                new_preset = False
        if self.ui.append_preset.isChecked():
            if new_preset:
                append = 'new'
            else:
                append = 'append'
        else:
            append = 'close'
        self.vr.add_to_preset(name,append,orientation)
        print(new_preset)
        if new_preset:
            print('Adding new preset')
            self.preset_tabs.append(QtWidgets.QWidget())
            self.preset_tabs[-1].setStyleSheet("")
            self.preset_tabs[-1].setObjectName("tab_"+str(self.tab_cnt))
            self.tab_cnt+=1
            # Add widget as a new tab and set text per file name
            self.ui.tab_position.addTab(self.preset_tabs[-1], "")
            self.ui.tab_position.setTabText(self.ui.tab_position.indexOf(self.preset_tabs[-1]),name)
            # Add actuator block of correct orientation
            self.preset_blks.append(Actuator_Block(self,self.screen_width,orientation,self.preset_tabs[-1]))
            self.preset_list.append([name,orientation])


    def handle_delete_preset(self):
        name = self.ui.append_preset_name.text()
        orientation = self.blk_option[self.manual_blk].orientation
        if os.path.exists('preset_files_usb/'+name+'.txt'):
            os.remove('preset_files_usb/'+name+'.txt')
        else:
            print('File does not exsist')
        if os.path.exists('preset_display_usb/display_'+name+'.txt'):
            os.remove('preset_display_usb/display_'+name+'.txt')
        else:
            print('File does not exsist')
        if os.path.exists('preset_files_serial/'+name+'.txt'):
            os.remove('preset_files_serial/'+name+'.txt')
        else:
            print('File does not exsist')
        if os.path.exists('preset_display_serial/display_'+name+'.txt'):
            os.remove('preset_display_serial/display_'+name+'.txt')
        else:
            print('File does not exsist')
        try:
            self.preset_list.remove([name,orientation])
        except:
            print('Not in list')
        print(self.preset_list)


    def handle_preset(self,index,):
        '''NOTICE!! Updating GUI display should not be in another thread(it will crash after a while)! Either move actuator activation to another thread
        (has caused problems with updaing GUI) or find legal way to update widgets in a thread (Qimage?)'''
        name = self.preset_list[index][0]
        option = 0
        if index == 0:
            self.vr.set_one_pulse_duration(1000,'on')
            self.vr.set_Timing()
            thread = threading.Thread(target=self.display_preset,args=(index,option))
            # thread = threading.Thread(target=self.vr.play_preset(name))
            thread.start()
            # elf.display_preset(index,option)
            self.vr.play_preset(name)
        elif index == 1:
            self.vr.set_one_pulse_duration(300,'on')
            self.vr.set_Timing()
            option = self.ui.sweep_type.currentIndex()
            thread = threading.Thread(target=self.display_preset,args=(index,option))
            # thread = threading.Thread(target=self.vr.play_preset(name,self.ui.sweep_type.currentIndex()))
            thread.start()
            # self.display_preset(index,option)
            self.vr.play_preset(name,self.ui.sweep_type.currentIndex())
        elif index == 2:
            self.vr.set_one_pulse_duration(500,'on')
            self.vr.set_one_pulse_duration(1000,'off')
            self.vr.set_Timing()
            option = self.ui.sweep_type.currentIndex()
            # thread = threading.Thread(target=self.vr.play_preset(name,self.ui.two_int_blk.currentIndex()))
            thread = threading.Thread(target=self.display_preset,args=(index,option))
            thread.start()
            # self.display_preset(index,option)
            self.vr.play_preset(name,self.ui.two_int_blk.currentIndex())
        else:
            thread = threading.Thread(target=self.display_preset,args=(index,option))
            # thread = threading.Thread(target=self.vr.play_preset(name))
            thread.start()
        # self.display_preset(index,option)
            self.vr.play_preset(name)


    def display_preset(self,index,option):
        name = self.preset_list[index][0]
        # with open('preset_display_usb/display_'+name+'.txt','r') as display_file:
        with open('preset_display_serial/display_'+name+'.txt','r') as display_file:

            # try:
            act_dict = ast.literal_eval(display_file.read())
            for act_list in act_dict[option]:
                for act in act_list:
                    self.preset_blks[index].act_blk.button(act).setStyleSheet(self.on_style_sheet)
                    self.preset_blks[index].act_blk.button(act).repaint()
                time.sleep(int(self.vr.t_pulse[2:]+self.vr.t_pulse[0:2],16)/1000)
                for act in act_list:
                    self.preset_blks[index].act_blk.button(act).setStyleSheet(self.off_style_sheet)
                    self.preset_blks[index].act_blk.button(act).repaint()
                time.sleep(int(self.vr.t_pause[2:]+self.vr.t_pause[0:2],16)/1000)
            # except:
            #    print("Error reading display txt")


    def handle_button(self,button):
        num = self.blk_option[self.manual_blk].act_blk.id(button)
        print(num)
        self.vr.set_ACT_state(num)
        self.display_ACT()


    def handle_actuator_blk(self,index):
        # print(index)
        self.handle_Alloff() # turn off actuators for other array (may not be desired)
        self.ui.act_blocks.setCurrentIndex(index) # switch to selected block of actuators
        try:
            self.blk_option[self.manual_blk].act_blk.buttonClicked.disconnect(self.handle_button) # disconnect current button signals
        except:
            print('Error')
        self.manual_blk = index # update to reflrect selected block
        self.blk_option[self.manual_blk].act_blk.buttonClicked.connect(self.handle_button) # connect signals for newly selected block
        print(self.manual_blk)


    def handle_Alloff(self):
        self.vr.Alloff()
        try:
            for button in self.blk_option[self.manual_blk].act_blk.buttons():
                button.setStyleSheet(self.off_style_sheet)
        except:
            print('No block')


    def display_ACT(self):
        # Controls color of buttons in GUI based on if turn on or not
        # ARGS: act is int for button id
        # print(act)
        if int(self.vr.OP_Mode) < 4 or int(self.vr.ACT_Mode) != 0: # Not single pulse'
            print(self.vr.ACT_ON)
            for p in self.vr.prev_act: #remove old button(s)
                self.blk_option[self.manual_blk].act_blk.button(p).setStyleSheet(self.off_style_sheet)
                # turn on new button
            for p in self.vr.ACT_ON:
                self.blk_option[self.manual_blk].act_blk.button(p).setStyleSheet(self.on_style_sheet)
        # Single pulse mode
        else:
            print(self.vr.prev_act)
            if self.vr.prev_act:
                self.blk_option[self.manual_blk].act_blk.button(self.vr.prev_act[0]).setStyleSheet(self.on_style_sheet)
                time.sleep(.5)
                self.blk_option[self.manual_blk].act_blk.button(self.vr.prev_act[0]).setStyleSheet(self.off_style_sheet)


    def check_for_presets(self):
        presets = []
        # for file in os.listdir("preset_files_usb"):
        for file in os.listdir("preset_files_serial"):
            if file.endswith(".txt"):
                # with open('preset_files_usb/'+file,'r') as open_preset:
                with open('preset_files_serial/'+file,'r') as open_preset:
                    line = open_preset.readline().rstrip()
                presets.append([file.replace('.txt',''),line[3:]])
                # print(file)
        return presets

    # def hex_button(self):
    #     for button in self.all_ACT:
    #         if button == 0:
    #             continue
    #         button.setFixedSize(QSize(50,50))
    #         size = button.width()
    #         # size = button.height()
    #         # size = 100
    #         # x = (3**.5 / 2)
    #         x = .9
    #         # print(x)
    #         # points = [QPoint(size/4,0),QPoint(size/4+size/2,0),QPoint(size,size*.5*x),QPoint(size/4+size/2,size*x),QPoint(size/4,size*x),QPoint(0,size*.5*x)] # points at the side
    #         points = [QPoint(0,size/4),QPoint(0,size/4+size/2),QPoint(size*.5*x,size),QPoint(size*x,size/4+size/2),QPoint(size*x,size/4),QPoint(size*.5*x,0)] # points at the top
    #         button.setMask(QRegion(QPolygon(points)))
    #         # break



if __name__ == '__main__':
    QtWidgets.QApplication.setStyle("fusion")
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    gui = MainWindow(screen)
    gui.showMaximized()
    sys.exit(app.exec_())
