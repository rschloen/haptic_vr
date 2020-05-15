#!/usr/bin/env python3


"""TODO:
    - Activate actuators implement all modes for protocol
    - Work on StyleSheets, see what's needed image wise (png,jpeg,size limits)
    - Keep in mind expansion up to 128 actuator arrays
    - Keep in mind thermal actuators
    - Keep in mind PWM frequency to set intensity
    - Work on deployment (pyqtdeploy, alternatives?) """

import serial
import sys,time

class VR_PRTCL:
    """Library for Haptic VR device NFC communication"""
    UID = ''
    device = None
    current_connection = None
    OP_Mode = '80'#'01'
    ACT_Mode = '00'
    ACT_BLKS = '02'
    # ACT_state = [0]*32*ACT_BLKS #may be redundant
    ACT_ON = None
    active = False
    MAX_PACKET_SIZE = 64
    nAttempts = 5

    def __init__(self):
        # Device initialization here: usb/bluetooth
        self.device = serial.Serial(None,115200,timeout=1,parity=serial.PARITY_NONE,dsrdtr=False)  # open serial port, 115200 baudrate, 1 sec timeout

    def connect(self,port_label,button,UID_label):
        # connect to nfc board (0x10c4,0xea60)
        if self.active:
            self.disconnect(port_label,button,UID_label)
        else:
            try:
                self.device.port = '/dev/ttyUSB0'
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

                if self.device.is_open:
                    print('Connected to {}'.format(self.device.name))
                    port_label.setText('Serial Port: {}'.format(self.device.name))
                    button.setText('Disconnect')
                # print(self.device)         # check which port was really used

            except:
                print('NFC board not connected.')


    def disconnect(self,port_label,button,UID_label):
        # disconnect from NFC board,(Adapted from Abraham's Optogenetics example)
        self.active = False
        self.device.close()
        if self.device.is_open:
            print('Port not closed!!')
        button.setText('Connect')
        port_label.setText('Serial Port: ')
        UID_label.setText('UID:  XX XX XX XX XX XX XX XX')
        print('Disconnected')


    def get_inventory(self,UID_label):
        # Get UID
        cmd = '010B000304140601000000' # read uid
        # print(cmd)
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
        UID_label.setText('UID:  {}'.format(self.UID_corrected)) #requires some bit shifting to get in right order


    def read_RFpower(self): #reading from device?
        # return Watts
        print("RF Power is currently ...")


    def set_RFpower(self,value,text):
        # Set watts
        self.RF_Power = value
        text.setText(("{} Watts").format(value))


    def send(self,cmd):
        # self.device.reset_input_buffer()
        self.device.reset_input_buffer()
        self.device.reset_output_buffer()
        for i in range(self.nAttempts):
            print('|Sent>       {}'.format(cmd))
            self.device.write(cmd.encode())
            # time.sleep(.1)
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

    def set_OP_Mode(self):
        # Set operating mode (i.e. All off, turn on/off, single pulse, continous?)
        pass

    def set_ACT_Mode(self):
        # Set actuation mode (i.e.Unipolar, bipolar)
        pass

    def set_ACT_Cnt(self):
        # set number of blocks of 32 actuators
        pass

    def set_Timing(self):
        # Set timing for actuation (i.e. single or continous pulse with high and/or low freq modulation)
        # Blk9(0x24) Blk10(0x28) Blk11(0x2C)
        self.Alloff()

        cmd3 = '01170003041862'+ '21' +self.UID+ '09' + 'D0070000'+'0000'
        cmd4 = '01170003041862'+ '21' +self.UID+ '0A' + '32006400'+'0000'
        cmd5 = '01170003041862'+ '21' +self.UID+ '0B' + 'c800F401'+'0000'

        state = self.send(cmd3)
        state = self.send(cmd4)
        state = self.send(cmd5)

    def set_ACT_intensity(self,value,text):
        # Modulate DC/PWM to adjust inensitiy of actuators
        self.ACT_intensity = value
        text.setText("Haptic Intensity: {} units".format(value))

    def Alloff(self):
        cmd = '0117000304186221'+self.UID+'00000002000000'
        res = self.send(cmd)

    def set_ACT_state(self,act,num):
        # turn on/off actuators. ARGS: act: Button Object for an actuator; num:Actuatior number
        if self.ACT_ON == None: # No buttons pressed
            self.ACT_ON = act
            action = True # Turn on actuator
        else: # Button already pressed
            if self.ACT_ON == act: # Button pressed twice in a row
                act.setChecked(False)
                self.ACT_ON = None
                action = False # Turn off actuator
            else: # new button pressed
                self.ACT_ON.setChecked(False)
                self.ACT_ON = act
                action = True # turn on new button
        if action:
            if num <= 32:
                blk2 = '%0*X'%(8,0)
                blk1 = 1 << num-1
                blk1 = '%0*X'%(8,blk1)
                blk1 = blk1[6:]+blk1[4:6]+blk1[2:4]+blk1[0:2]
            else:
                blk1 = '%0*X'%(8,0)
                blk2 = 1 << num-33
                blk2 = '%0*X'%(8,blk2)
                blk2 = blk2[6:]+blk2[4:6]+blk2[2:4]+blk2[0:2]

            # Blk 0
            self.OP_Mode = '06'
            blk0 = self.OP_Mode+self.ACT_Mode+self.ACT_BLKS+'00' #'01000200'
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


        else:
            self.Alloff()
