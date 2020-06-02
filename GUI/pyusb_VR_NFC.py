#!/usr/bin/env python3

import usb
# import serial
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
        # pass
        # Device initialization here: usb/bluetooth
        ## pyusb code
        dev = usb.core.find(find_all=True)
        for cfg in dev:
            # print(cfg.idVendor)
            if cfg.idVendor == 2737:
                self.device = [cfg.idVendor, cfg.idProduct]
        # print(self.device)

    def connect(self):#,port_label):
        # connect to nfc board (0x10c4,0xea60) (Adapted from Abraham's Optogenetics example)
        ### pyusb code
        # try:
        self.current_connection = usb.core.find(idVendor=self.device[0],idProduct=self.device[1])
        usb.util.dispose_resources(self.current_connection)

        self.current_connection.reset()
        if self.current_connection == None:
            print('Device not connected')
        for cfg in self.current_connection:
            # print(cfg)
            for i in range(cfg.bNumInterfaces):
                print(cfg[(i,0)][0])
                if self.current_connection.is_kernel_driver_active(i):
                    self.current_connection.detach_kernel_driver(i)
                    # usb.util.claim_interface(self.current_connection, i)
        print('Device Connected')
        self.current_connection.set_configuration()
        self.current_connection.baudrate = 115200
        # print(self.current_connection)
        self.current_connection.default_timeout = 5
        self.active_flag = True
        return True
        # except:
            # print('Connection failed')
            # return False

    def disconnect(self):#,port_label,UID_label):
        # disconnect from NFC board,(Adapted from Abraham's Optogenetics example)
        self.active_flag = False
        if self.current_connection is not None:
            usb.util.dispose_resources(self.current_connection)
        self.current_connection = None
        print('Disconnected')

    def get_inventory(self):
        # Get UID
        cmd = b'\x01\x0B\x00\x03\x04\x14\x06\x01\x00\x00\x00' # read uid
        msg = '010B000304142601000000' # read uid
        msg = [2,0,9,255,176,1,0]

        uid = self.send(msg)
        print(uid)
        # uid = uid[::-1]
        # UID_label.setText('UID:  {}'.format(uid[13:29])) #requires some bit shifting to get in right order


    def read_RFpower(self): #reading from device?
        # return Watts
        print("RF Power is currently ...")


    def set_RFpower(self,value,text):
        # Set watts
        self.RF_Power = value
        text.setText(("{} Watts").format(value))



    # def send(self,cmd):
    #     ### pyusb code
    #     cmd = self.CRC16(cmd)
    #     print(cmd)
    #     # msg = 'test'
    #     print('Writing...')
    #     # msg = [1, 11, 0, 3, 4, 20, 38, 1, 0, 0, 0]
    #     # msg = '010B000304180220020000' #read blk
    #     self.current_connection.write(0x2,cmd)
    #     time.sleep(0.25)
    #     # assert len(self.current_connection.write(0x2,cmd.encode(), 100)) == len(cmd)
    #     print('Reading...')
    #     data = self.current_connection.read(0x81, 64,1000)
    #     print(data)
    #     return data
    def send(self, msg):
        msg = self.CRC16(msg)
        msg0 = ''
        if msg == []:
            return None
        msg0 = '|>>>: '
        for i in msg:
            strtmp = str(hex(i))[2:]
            if len(strtmp) == 1:
                msg0 += '0' + str(hex(i))[2:] + ' '
            if len(strtmp) == 2:
                msg0 += str(hex(i))[2:] + ' '

        data = None
        print(msg0)
        msgx = msg
        if self.active_flag:
            count = 0
            while 1:
    ##            data = self.current_connection.read(129, 128)
                self.current_connection.write(2,msgx)
                self.recieving_flag = True
                time.sleep(0.25)     # Update with time hold on
                data = self.current_connection.read(129, 128)

                while len(data) < 0:
                    data = self.current_connection.read(129, 128)

                msg = data
                msg0 = '<<<|: '
                for i in msg:
                    strtmp = str(hex(i))[2:]
                    if len(strtmp) == 1:
                        msg0 += '0' + str(hex(i))[2:] + ' '
                    if len(strtmp) == 2:
                        msg0 += str(hex(i))[2:] + ' '
                count += 1
                # check for errors in the response, probably not devices in the antenna
                # or the error with the antenna tunning
                if data[2] == 8 or data[2] == 9:
                    if data[5] == 132:
                        print(msg0 + ' | Antenna warning!')
                        return []
                    if data[5] == 1:
                        print(msg0 + ' | No devices found, ' + str(count) + ' out of ' + str(self.com_attempts))
                        data = []
                else:
                    print(msg0)
                    return data
                if count == self.com_attempts: return[]
                time.sleep(0.5)
            return data
        return []


    def read(self):
        # assemble and display data returned from device
        pass

    def CRC16(self, msg): #from Nlux code
        crc_poly = int("8408", 16)
        crc = int("FFFF",16)
        print(crc)
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


if __name__ == '__main__':
    vr = VR_PRTCL()
    vr.connect()
    if vr.active_flag:
        vr.get_inventory()

    vr.disconnect()
