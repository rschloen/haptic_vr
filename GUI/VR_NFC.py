#!/usr/bin/env python3

# import usb
import serial
import sys,time

class VR_PRTCL:
    """Library for Haptic VR device NFC communication"""
    UUID = []
    device = None
    current_connection = None
    OP_Mode = 0x00
    ACT_Mode = 0x00
    ACT_BLKS = 1
    ACT_state = [0]*32*ACT_BLKS
    active = 0


    def __init__(self):
        pass
        # Device initialization here: usb/bluetooth
        # try:
        #     ser = serial.Serial('/dev/ttyUSB0')  # open serial port
        #     print(ser.name)         # check which port was really used
        #     # ser.close()             #
        # except:
        #     print('NFC board not plugged in.')

        ### pyusb code
        # dev = usb.core.find(find_all=True)
        # for cfg in dev:
        #     if cfg.idVendor == 4292:
        #         self.device = [cfg.idVendor, cfg.idProduct]
        # print(self.device)

    def connect(self):
        # connect to nfc board (0x10c4,0xea60) (Adapted from Abraham's Optogenetics example)
        try:
            self.device = serial.Serial('/dev/ttyUSB0')  # open serial port
            print(self.device.name)         # check which port was really used
            self.device.baudrate = 115200
            self.active_flag = True
            print('Connected to {}'.format(self.device.name))
        except:
            print('NFC board not connected.')


        ### pyusb code
        # try:
        #     self.current_connection = usb.core.find(idVendor=self.device[0],idProduct=self.device[1])
        #     self.current_connection.reset()
        #     if self.current_connection == None:
        #         print('Device not connected')
        #     for cfg in self.current_connection:
        #         print(cfg)
        #         for i in range(cfg.bNumInterfaces):
        #             if self.current_connection.is_kernel_driver_active(i):
        #                 self.current_connection.detach_kernel_driver(i)
        #                 usb.util.claim_interface(self.current_connection, i)
        #     print('Device Connected')
        #     self.current_connection.set_configuration()
        #     self.current_connection.baudrate = 115200
        #     print(self.current_connection)
        #     # self.current_connection.default_timeout = 100
        #     self.active_flag = True
        #     return True
        # except:
        #     print('Connection failed')
        #     return False

    def disconnect(self):
        # disconnect from NFC board,(Adapted from Abraham's Optogenetics example)
        self.active_flag = False
        self.device.close()
        if self.device.is_open:
            print('Port not closed!!')
        print('Disconnected')
        # self.active_flag = False
        # if self.current_connection is not None:
        #     usb.util.dispose_resources(self.current_connection)
        # self.current_connection = None
        # print('Disconnected')

    def get_inventory(self):
        # Get UID
        cmd = b'\x01\x0B\x00\x03\x04\x14\x26\x01\x00\x00\x00' # read uid
        self.send(cmd)

    def read_RFpower(self): #reading from device?
        # return Watts
        print("RF Power is currently ...")


    def set_RFpower(self,value,text):
        # Set watts
        self.RF_Power = value
        text.setText(("{} Watts").format(value))



    def send(self,cmd):
        self.device.write(cmd)
        time.sleep(.5)
        data = self.device.read(64).decode('ascii')
        print(data)



        ### pyusb code
        # msg = 'test'
        # print('Writing...')
        # msg = [1, 11, 0, 3, 4, 20, 38, 1, 0, 0, 0]
        # msg = '010B000304180220020000' #read blk
        # msg = '010B000304142601000000' # read uid
        # self.current_connection.write(1, msg)
        # print('Reading...')
        # assert len(self.current_connection.write(1, msg, 100)) == len(msg)

        # data = self.current_connection.read(0x81, 64,1000)
        # print(data)

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

    def set_ACT_state(self,act):
        # turn on/off actuators. ARGS: act:pair/list of pairs of actiuator(s) and state to set them to
        pass
