#!/usr/bin/env python3

import usb

class VR_PRTCL:
    """Library for Haptic VR device NFC communication"""
    UUID = []
    devices = []
    OP_Mode = 0x00
    ACT_Mode = 0x00
    ACT_BLKS = 1
    ACT_state = [0]*32*ACT_BLKS


    def __init__(self):
        # Device initialization here: usb/bluetooth
        dev = usb.core.find(find_all=True)
        # print(dev)
        for cfg in dev:
            # print(cfg)
            self.devices.append(hex(cfg.idVendor) + "," + hex(cfg.idProduct))
        print(self.devices)

    def connect(self):
        # connect to RF device (0x1781,0xc9f)
        pass

    def disconnect(self):
        # disconnect from RF device
        pass

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
