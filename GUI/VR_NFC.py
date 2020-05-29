#!/usr/bin/env python3

"""TODO:
    X Activate actuators implement all modes for protocol
    - Work on StyleSheets, Different shapes for buttons
    - Adding presets and create custom presets in GUI
    - Implement multi-touch (selecting multiple actuators at the same time)
    - Keep in mind PWM frequency to set intensity of led (Implement setting DC/Freq)
        - Multiple intensities at same time
    - Keep in mind expansion up to 128 actuator arrays
    - Keep in mind thermal actuators
    - Work on deployment (pyqtdeploy, alternatives?) """

import serial
import serial.tools.list_ports
import sys,time,csv

class VR_PRTCL:
    """Library for Haptic VR device NFC communication"""
    UID = ''
    device = None
    current_connection = None
    OP_Mode = '01'
    ACT_Mode = '00'
    ACT_BLKS = '02'
    # ACT_state = [0]*32*ACT_BLKS #may be redundant
    ACT_ON = []
    active = False
    prev_act = []
    MAX_PACKET_SIZE = 64
    nAttempts = 5
    cnt=0
    pulse_mode = 1
    hf_mod = 0
    lf_mod = 0
    t_pulse = 'F4010000'
    T_high = '6400'
    T_low = 'F401'
    DC_high = '3200'
    DC_low = 'FA00'
    append_to_file = False

    def __init__(self):
        # Device initialization here: usb/bluetooth
        self.device = serial.Serial(None,115200,timeout=1,parity=serial.PARITY_NONE,dsrdtr=False)  # open serial port, 115200 baudrate, 1 sec timeout

    def connect(self,port_label,button,UID_label):
        # connect to nfc board (0x10c4,0xea60)
        if self.active:
            self.disconnect(port_label,button,UID_label)
        else:
            # try:
            ports = serial.tools.list_ports.comports()
            # print(ports)
            for p in ports:
                print(p)
                print(p.description)
            self.device.port = 'COM5'
            self.device.open()
            self.active = True
            cmd = '010A0003041001210000' #Register write request
            rep = self.send(cmd)

            cmd = '010C00030410002101060000' #Register write request
            rep = self.send(cmd)

            cmd = '0109000304F0000000' #AGC Toggle
            rep = self.send(cmd)

            cmd = '0109000304F1FF0000' #AM PM Toggle
            rep = self.send(cmd)

            # except:
                # print('NFC board not connected.')


    def disconnect(self,port_label,button,UID_label):
        # disconnect from NFC board
        self.active = False
        self.device.close()
        if self.device.is_open:
            print('Port not closed!!')
        try:
            if not self.preset_file.closed:
                self.preset_file.close()
        except:
            pass
        print('Disconnected')


    def add_to_preset(self,preset_name,append):
        #add check for filename
        if append:
            self.append_to_file = True
            try:
                self.preset_file = open('preset_files/'+preset_name+'.txt','a')
            except FileNotFoundError:
                self.preset_file = open('preset_files/'+preset_name+'.txt','w')
            print(self.preset_file.closed)
        else:
            self.append_to_file = False
            if not self.preset_file.closed:
                self.preset_file.close()


    def get_inventory(self):
        # Get UID
        cmd = '010B000304140601000000' # read uid
        uid = self.send(cmd)
        uid = uid[33:33+16]
        # print(uid)
        # while uid == '':
        #     uid = self.send(cmd)
        self.UID = uid
        temp = ''
        for i in range(0,len(uid),2):
            temp += uid[len(uid)-(i+2)]
            temp += uid[len(uid)-(i+1)]
        self.UID_corrected = temp
        # self.set_Timing()


    def read_RFpower(self): #reading from device?
        # return Watts
        print("RF Power is currently ...")


    def set_RFpower(self,value,text):
        # Set watts
        self.RF_Power = value
        text.setText(("{} Watts").format(value))


    def send(self,cmd):
        self.device.reset_input_buffer()
        self.device.reset_output_buffer()
        for i in range(self.nAttempts):
            print('|Sent>       {}'.format(cmd))
            self.device.write(cmd.encode())
            data = self.device.read(size=self.MAX_PACKET_SIZE).strip().decode()

            if data:
                print('<Recieved|   {}'.format(str(data)))
                return data
            else:
                print('No data recieved')
        print('No data recieved in {} attempts'.format(self.nAttempts))
        return data


    def read(self):
        # assemble and display data returned from device
        pass

    def CRC16(self, msg): #from Nlux code
        crc_poly = int("8408", 16)
        crc = int("FFFF",16)
        for i in msg:
            crc = crc ^ i;
            for j in range(8):
                if(crc & 1):
                    crc = (crc>>1) ^ crc_poly
                else:
                    crc = (crc>>1)
        data = hex(crc)[2:]
        data = "0"*(4-len(data))+data
        data = [int(data[2:],16), int(data[:2],16)]
        msg.extend(data)
        return msg

    def play_preset(self,preset):
        if preset == 'flash all':
            temp = self.OP_Mode
            self.OP_Mode = '80'
            blk0 = self.OP_Mode+self.ACT_Mode+self.ACT_BLKS+'00' #'01000200'
            cmd0 = '01170003041862'+ '21' +self.UID+ '00' + blk0+'0000'
            state = self.send(cmd0)
            self.OP_Mode = temp
        elif preset == 'ABCs':
            with open('preset_files/'+preset+'.txt','r') as read_preset:
                cnt = 0
                for line in read_preset:
                    cmd = line.rstrip()
                    d = self.send(cmd)
                    if cnt == 2:
                        time.sleep(0.5)
                        self.Alloff()
                        time.sleep(0.5)
                        cnt = 0
                    else:
                        cnt += 1
        else:
            with open('preset_files/'+preset+'.txt','r') as read_preset:
                for line in read_preset:
                    cmd = line.rstrip()
                    d = self.send(cmd)

    def set_OP_Mode(self,value,level):
        # Set operating mode (i.e. All off, turn on/off, single pulse, continous)
        if level == 1:
            if value == 1:
                self.pulse_mode = 4
            else:
                self.pulse_mode = 1
        elif level == 2:
            self.hf_mod = value
        elif level == 3:
            self.lf_mod = value
        self.OP_Mode = '%0*X'%(2,self.pulse_mode+self.hf_mod+self.lf_mod)
        # print(self.OP_Mode)

    def set_ACT_Mode(self,mode):
        # Set actuation mode (i.e.Unipolar, bipolar)
        self.ACT_Mode = '%0*X'%(2,mode)

    def set_ACT_Cnt(self):
        # set number of blocks of 32 actuators
        pass

    def set_one_pulse_duration(self,time):
        try:
            time = int(time)
        except ValueError:
            print('Must enter a number')
        t = '%0*X'%(8,time)
        self.t_pulse = t[6:]+t[4:6]+t[2:4]+t[0:2]
        # self.set_Timing()

    def set_pulse_freq(self,freq,mode):
        T = int((1/freq)*1000)
        if mode == 'high':
            t = '%0*X'%(4,T)
            self.T_high = t[2:4]+t[0:2]
        else:
            t = '%0*X'%(4,T)
            self.T_low = t[2:4]+t[0:2]
        # self.set_Timing()

    def set_Timing(self):
        # Set timing for actuation (i.e. single or continous pulse with high and/or low freq modulation)
        # Blk9(0x24) Blk10(0x28) Blk11(0x2C)
        self.Alloff()
        cmd3 = '01170003041862'+ '21' +self.UID+ '09' + self.t_pulse +'0000'
        cmd4 = '01170003041862'+ '21' +self.UID+ '0A' + self.DC_high + self.T_high +'0000'
        cmd5 = '01170003041862'+ '21' +self.UID+ '0B' + self.DC_low + self.T_low +'0000'

        state = self.send(cmd3)
        state = self.send(cmd4)
        state = self.send(cmd5)
        if self.append_to_file:
            self.preset_file.write(cmd3+'\n')
            self.preset_file.write(cmd4+'\n')
            self.preset_file.write(cmd5+'\n')

    def set_ACT_intensity(self,dc,mode):
        # Modulate DC/PWM to adjust inensitiy of actuators
        if mode == 'high':
            t_h = self.T_high[2:4]+self.T_high[0:2] # value is stored reversed, so it needs to be flipped again
            temp = int((dc/100)*int(t_h,16)) # DC percentage times the high freq period
            temp = '%0*X'%(4,temp) # convert to hex string
            self.DC_high = temp[2:4]+temp[0:2] # Store in reverse for sending command
            # print(self.DC_high)
        else:
            t_l = self.T_low[2:4]+self.T_low[0:2]
            temp = int((dc/100.0)*int(t_l,16))
            temp = '%0*X'%(4,temp)
            self.DC_low = temp[2:4]+temp[0:2]
            # print(self.DC_low)
        # self.set_Timing()

    def Alloff(self):
        cmd = '0117000304186221'+self.UID+'00000002000000'
        res = self.send(cmd)
        if self.append_to_file:
            self.preset_file.write(cmd+'\n')
        self.prev_act = self.ACT_ON[:]
        self.ACT_ON = []

    def set_ACT_state(self,act_num):
        # turn on/off actuators. ARGS: act: Button Object for an actuator; num:Actuatior number
        action = False
        self.prev_act = []
        if self.ACT_Mode == '00':
            if act_num in self.ACT_ON: # Button pressed twice in a row
                self.prev_act.append(self.ACT_ON.pop())
            else: # new button pressed
                try:
                    self.prev_act.append(self.ACT_ON.pop())
                except:
                    pass
                self.ACT_ON.append(act_num)
                action = True # turn on new button
        else:
            # multi modal (touch)
            if act_num == 0: # Turns on selected actuators
                action = True
            else:
                if act_num in self.ACT_ON: #Turn off an already pressed button
                    self.ACT_ON.remove(act_num)
                    self.prev_act.append(act_num) # So it gets turned off in the GUI
                else:
                    self.ACT_ON.append(act_num)
            print(self.ACT_ON)

        if action:
                temp_blk = 0
                for act in self.ACT_ON:
                    shift_act = 1 << act-1
                    temp_blk |= shift_act
                temp_blk = '%0*X'%(16,temp_blk)

                # print(temp_blk)
                blk1 = temp_blk[8:]
                blk1 = blk1[6:]+blk1[4:6]+blk1[2:4]+blk1[0:2]
                blk2 = temp_blk[0:8]
                blk2 = blk2[6:]+blk2[4:6]+blk2[2:4]+blk2[0:2]
                # Blk 0
                # print(blk1)
                blk0 = self.OP_Mode + self.ACT_Mode + self.ACT_BLKS + '00'
                cmd0 = '01170003041862'+ '21' +self.UID+ '00' + blk0+'0000'
                        #|nb             |r/w       |UID  |BlkAdr |data |padding
                                            #(9552D9D0F35902E0)
                # Blk 1
                cmd1 = '01170003041862'+ '21' +self.UID+ '01' + blk1 + '0000'
                #Blk 2
                cmd2 = '01170003041862'+ '21' +self.UID+ '02' + blk2 + '0000'

                state = self.send(cmd1)
                state = self.send(cmd2)
                state = self.send(cmd0)
                if self.append_to_file:
                    print('writing')
                    self.preset_file.write(cmd1+'\n')
                    self.preset_file.write(cmd2+'\n')
                    self.preset_file.write(cmd0+'\n')

        else:
            cmd = '0117000304186221'+self.UID+'00000002000000'
            res = self.send(cmd)