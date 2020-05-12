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
    UID = []
    device = None
    current_connection = None
    OP_Mode = 0x00
    ACT_Mode = 0x00
    ACT_BLKS = 1
    ACT_state = [0]*32*ACT_BLKS
    active = 0
    MAX_PACKET_SIZE = 64
    nAttempts = 5

    def __init__(self):
        # Device initialization here: usb/bluetooth
        self.device = serial.Serial(None,115200,timeout=1,parity=serial.PARITY_NONE,dsrdtr=False)  # open serial port, 115200 baudrate, 1 sec timeout

    def connect(self,port_label):
        # connect to nfc board (0x10c4,0xea60)
        try:
            self.device.port = '/dev/ttyUSB0'
            self.device.open()
            self.active_flag = True
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
                port_label.setText('{}'.format(self.device.name))
            # print(self.device)         # check which port was really used

        except:
            print('NFC board not connected.')


    def disconnect(self,port_label,UID_label):
        # disconnect from NFC board,(Adapted from Abraham's Optogenetics example)
        self.active_flag = False
        self.device.close()
        if self.device.is_open:
            print('Port not closed!!')
        port_label.setText(' ')
        UID_label.setText('UID:  XX XX XX XX XX XX XX XX')
        print('Disconnected')


    def get_inventory(self,UID_label):
        # Get UID
        # cmd = b'\x01\x0B\x00\x03\x04\x14\x06\x01\x00\x00\x00' # read uid
        cmd = '010B000304140601000000' # read uid
        # cmd = bytes(bytearray.fromhex(cmd))
        # print(cmd)
        uid = self.send(cmd)
        uid = uid[13:29]
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
        for i in range(self.nAttempts):
            # self.device.reset_output_buffer()
            print('|Sent>       {}'.format(cmd))
            self.device.write(cmd.encode())
            time.sleep(.5)
            data = self.device.read(size=self.MAX_PACKET_SIZE).strip().decode()
            self.device.reset_input_buffer()
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
        pass

    def set_ACT_intensity(self,value,text):
        # Modulate DC/PWM to adjust inensitiy of actuators
        self.ACT_intensity = value
        text.setText("Haptic Intensity: {} units".format(value))

    def set_ACT_state(self):
        # turn on/off actuators. ARGS: act:pair/list of pairs of actiuator(s) and state to set them to
        cmd = '01170003041862219552D9D0F35902E000010002000000'
        cmd = bytes(bytearray.fromhex(cmd))
        print(cmd)
        # cmd = b'\x01\x0B\x00\x03\x04\x18\x02\x20\x02\x00\x00'
        state = self.send(cmd)
        print(state)
