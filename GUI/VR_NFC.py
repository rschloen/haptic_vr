#!/usr/bin/env python3

import usb

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
        # Device initialization here: usb/bluetooth
        dev = usb.core.find(find_all=True)
        for cfg in dev:
            if cfg.idVendor == 4292:
                self.device = [cfg.idVendor, cfg.idProduct]
        # print(self.device)

    def connect(self):
        # connect to nfc board (0x10c4,0xea60) (Adapted from Abraham's Optogenetics example)
        if self.active:
            self.current_connection.close()
        try:
            self.current_connection = usb.core.find(idVendor=self.device[0],idProduct=self.device[1])
            self.current_connection.reset()
            if self.current_connection == None:
                print('Device not connected')
            for cfg in self.current_connection:
                for i in range(cfg.bNumInterfaces):
                    if self.current_connection.is_kernel_driver_active(i):
                        reattach = True
                        self.current_connection.detach_kernel_driver(i)
            print('Device Connected')
            self.current_connection.set_configuration()
            self.current_connection.baudrate = 115200
            self.current_connection.default_timeout = 1
            self.active_flag = True
            return True
        except:
            print('Connection failed')
            return False

    def disconnect(self):
        # disconnect from NFC board,(Adapted from Abraham's Optogenetics example)
        self.active_flag = False
        if self.current_connection is not None:
            usb.util.dispose_resources(self.current_connection)
        self.current_connection = None
        print('Disconnected')

    def get_inventory(self):
        # Run for anticollision protocol?
        pass

    def read_RFpower(self): #reading from device?
        # return Watts
        print("RF Power is currently ...")


    def set_RFpower(self,value,text):
        # Set watts
        self.RF_Power = value
        text.setText(("{} Watts").format(value))



    def send(self):
        # assemble and transmit data packet to device
        pass

    def read(self):
        # assemble and display data returned from device
        pass

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
