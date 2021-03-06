#!/usr/bin/env python3
# import os
# os.environ['PYUSB_DEBUG'] = 'debug'
import usb
import sys,time, os
'''Mybe try booting linux from usb on tablet-can't get touch screen to work without different kernel(alternatives?)'''
'''Gesture sweeps send op mode(86..af), update timing when switching to preset'''

"""TODO:
    X FIX DELAY! (Hardware)
    X Adding presets and create custom presets in GUI and Saving/Loading Profiles
    - Finsh gesture support for presets
    X Activate actuators implement all modes for protocol
    X Work on StyleSheets, Different shapes for buttons
    X Implement multi-touch (selecting multiple actuators at the same time)
    X Keep in mind PWM frequency to set intensity of led (Implement setting DC/Freq)
        - Multiple intensities at same time (Firmware update)
    - Keep in mind expansion up to 128 actuator arrays
    - Add thermal actuator tab
    - Work on deployment (pyqtdeploy, alternatives?) """

class USB_VR_PRTCL:
    """Library for Haptic VR device NFC communication"""
    UID = ''
    device = None
    current_connection = None
    active_flag = False
    com_attempts = 5
    OP_Mode = '01'
    ACT_Mode = '00'
    ACT_BLKS = '02'
    ACT_ON = []
    active = False
    prev_act = []
    MAX_PACKET_SIZE = 64
    nAttempts = 5
    cnt=0
    pulse_mode = 1
    hf_mod = 0
    lf_mod = 0
    t_pulse = 'F401'
    t_pause = '0000'
    T_high = '6400'
    T_low = 'F401'
    DC_high = '3200'
    DC_low = 'FA00'
    append_to_file = False
    data_w_header = [2,0,24,255,176,36,1]
    data_r_header = [2,0,19,255,176,35,1]


    def __init__(self):
        # Device initialization here: usb/bluetooth
        dev = usb.core.find(find_all=True)
        for cfg in dev:
            if cfg.idVendor == 2737:
                self.device = [cfg.idVendor, cfg.idProduct]
                return
        print('NFC Box Not Found')


    def connect(self):
        # Connect to nfc board (0x0ab1,0x2)
        if self.active_flag:
            self.disconnect()
        else:
            try:
                self.current_connection = usb.core.find(idVendor=self.device[0],idProduct=self.device[1])
                usb.util.dispose_resources(self.current_connection)

                self.current_connection.reset()
                if self.current_connection == None:
                    print('Device not connected')
                for cfg in self.current_connection:
                    for i in range(cfg.bNumInterfaces):
                        if self.current_connection.is_kernel_driver_active(i):
                            self.current_connection.detach_kernel_driver(i)
                            # usb.util.claim_interface(self.current_connection, i)
                print('Device Connected')
                self.current_connection.set_configuration()
                self.current_connection.baudrate = 115200
                self.current_connection.default_timeout = 5
                self.active_flag = True
                return True
            except:
                print('Connection failed')
                return False


    def disconnect(self):
        # Disconnect from NFC board. Close open files
        self.active_flag = False
        if self.current_connection is not None:
            usb.util.dispose_resources(self.current_connection)
        self.current_connection = None
        try:
            if not self.preset_file.closed:
                self.preset_file.close()
            if not self.display_preset.closed:
                self.display_preset.close()
        except:
            pass
        print('Disconnected')


    def get_inventory(self):
        # Get UID for devices in range
        msg = [2,0,9,255,176,1,0]
        self.UID = ''
        uid = self.send(msg)
        uid = uid[9:17]
        for ele in uid:
            self.UID += '%0*X'%(2,ele)


    def read_RFpower(self): #reading from device
        # return Watts
        print("RF Power is currently ...")


    def set_RFpower(self,pow):
        # Set watts
        self.RF_Power = pow
        msg = [2,0,44,255,139,2,1,1,1,30,0,3,0,8,pow,128,0,0,0,0,0,0,0,0,0,128,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        res = self.send(msg)
        print(res)


    def send(self, msg):
        '''Send passed command to connected board and read what is returned.
        ARGS: msg: array of decimals to be sent to board'''
        # From OptogenNFC provided by Abraham
        msg = self.CRC16(msg)
        msg0 = ''
        if msg == []:
            return None
        msg0 = '|>>>: '
        for i in msg:
            msg0 += '%0*X'%(2,i)
        data = None
        print(msg0)
        msgx = msg
        count = 0
        if self.active_flag:
            while 1:
                self.current_connection.write(2,msgx)
                self.recieving_flag = True
                time.sleep(.25)
                data = self.current_connection.read(129, 128)
                msg = data
                msg0 = '<<<|: '
                for i in msg:
                    msg0 += '%0*X'%(2,i)
                count += 1
                print(msg0)
                # check for errors in the response, probably not devices in the antenna
                # or the error with the antenna tunning
                if data[2] == 8 or data[2] == 9:
                    if data[5] == 132:
                        print(msg0 + ' | Antenna warning!')
                        return []
                    elif data[5] == 1:
                        print(msg0 + ' | No devices found, ' + str(count) + ' out of ' + str(self.com_attempts))
                        data = []
                    elif data[5] == 0:
                        return data
                    else:
                        print(data)
                else:
                    return data
                if count == self.com_attempts: return[]
            return data
        return []


    def add_to_preset(self,preset_name,append,orientation):
        '''Open/close file or check for file matching passed name to append to.
        ARGS: preset_name: (str) name of file to open/close/create
              append: (str) check if closing, appending, creating file
              orientation: (str) orientation of actuator block'''
        if append != 'close':
            if preset_name == '':
                print('Need File name')
                return
            self.append_to_file = True
            if append == 'append':
                try:
                    self.preset_file = open('preset_files_usb/'+preset_name+'.txt','a')
                    self.display_preset = open('preset_display_usb/display_'+preset_name+'.txt','a')
                    print('Appending')
                except FileNotFoundError:
                    print('File not found')
                    self.preset_file = open('preset_files_usb/'+preset_name+'.txt','w')
                    self.display_preset = open('preset_display_usb/display_'+preset_name+'.txt','w')
                    self.preset_file.write('o: '+orientation+'\n')
                    self.display_preset.write('{0:[')
            else:
                print('New file')
                self.preset_file = open('preset_files_usb/'+preset_name+'.txt','w')
                self.display_preset = open('preset_display_usb/display_'+preset_name+'.txt','w')
                self.preset_file.write('o: '+orientation+'\n')
                self.display_preset.write('{0:[')
        else:
            self.display_preset.write(']}')
            self.append_to_file = False
            if not self.preset_file.closed:
                self.preset_file.close()
            if not self.display_preset.closed:
                self.display_preset.close()


    def play_preset(self,preset,index=None):
        '''Set OP mode or opens files to read commands from to play a preset
        ARGS: preset:(str) name or preset(file)
              index:(str) if preset has multiple options (think sweep directions), holds index of value that is converted into OP mode'''

        # if type(preset) == int:
        #     preset = self.preset_num2name(preset,index)
        if preset == 'flash_all':
            temp = self.OP_Mode
            self.OP_Mode = '80'
        elif preset == '2i_blk':
            temp = self.OP_Mode
            self.OP_Mode = 'A'+str(hex(index))[2]
            # print(self.OP_Mode)
        elif preset == 'sweep':
            temp = self.OP_Mode
            self.OP_Mode = '8'+str(hex(index+6))[2]
            # print(self.OP_Mode)
        else:
            with open('preset_files_usb/'+preset+'.txt','r') as read_preset:
                time.sleep(.25)
                for line in read_preset:
                    if line[0] == 'o': continue
                    cmd = line.rstrip()
                    n_cmd = self.assemble_command(cmd,'w')
                    d = self.send(n_cmd)
            return
        cmd0 = self.UID+ '000104' + '00' + self.ACT_BLKS + self.ACT_Mode + self.OP_Mode
        n_cmd0 = self.assemble_command(cmd0,'w')
        state = self.send(n_cmd0)
        self.OP_Mode = temp


    def set_OP_Mode(self,value,level):
        '''Set operating mode (i.e. All off, turn on/off, single pulse, continous)
        ARGS: value: 0 or 1 setting each option either on or off
              level: which part of the mode to set(i.e. single/continuous, high or low freq)'''
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
        print(self.OP_Mode)


    def set_ACT_Mode(self,mode):
        '''Set actuation mode (i.e.Unipolar, bipolar)
        ARGS: mode: value to set mode to'''
        self.ACT_Mode = '%0*X'%(2,mode)


    def set_ACT_Cnt(self,num_blks):
        '''Set number of blocks of 32 actuators
        ARGS: num_blks: number of actuator blocks'''
        self.ACT_BLKS = '%0*X'%(2,num_blks)


    def set_one_pulse_duration(self,time,mode):
        '''Set duration of single pulse on and pause times
        ARGS: time: time on/off
              mode: set time to pulse on time or pause time'''
        try:
            time = int(time)
        except ValueError:
            print('Must enter a number')
        print(time)
        t = '%0*X'%(4,time)
        if mode == 'on':
            self.t_pulse = t#[6:]+t[4:6]+t[2:4]+t[0:2]
        else:
            self.t_pause = t#[6:]+t[4:6]+t[2:4]+t[0:2]
        # self.set_Timing()


    def set_pulse_freq(self,freq,mode):
        '''Set frequency of pulsing
        ARGS: freq: frequency
              mode: set frequency of high or low modulation'''
        print(freq)
        T = int((1/freq)*1000)
        if mode == 'high':
            t = '%0*X'%(4,T)
            self.T_high = t#[2:4]+t[0:2]
        else:
            t = '%0*X'%(4,T)
            self.T_low = t#[2:4]+t[0:2]
        # self.set_Timing()


    def set_Timing(self):
        '''Set timing for actuation (i.e. single or continous pulse with high and/or low freq modulation)'''
        # Blk9(0x24) Blk10(0x28) Blk11(0x2C)
        #LSB first
        self.Alloff()
        # print(self.t_pulse)
        cmd3 = self.UID+ '090104' + self.t_pulse + self.t_pause# +'0000'
        cmd4 = self.UID+ '0A0104' + self.T_high + self.DC_high# +'0000'
        cmd5 = self.UID+ '0B0104' + self.T_low + self.DC_low# +'0000'
        n_cmd3 = self.assemble_command(cmd3,'w')
        n_cmd4 = self.assemble_command(cmd4,'w')
        n_cmd5 = self.assemble_command(cmd5,'w')
        state = self.send(n_cmd3)
        state = self.send(n_cmd4)
        state = self.send(n_cmd5)
        if self.append_to_file:
            self.preset_file.write(cmd3+'\n')
            self.preset_file.write(cmd4+'\n')
            self.preset_file.write(cmd5+'\n')


    def set_ACT_intensity(self,dc,mode):
        # Modulate DC/PWM to adjust inensitiy of actuators
        try:
            dc = int(dc)
        except ValueError:
            print('Must enter a number')
        print(dc)
        if mode == 'high':
            t_h = self.T_high[2:4]+self.T_high[0:2] # value is stored reversed, so it needs to be flipped again
            temp = int((dc/100)*int(self.T_high,16)) # DC percentage times the high freq period
            temp = '%0*X'%(4,temp) # convert to hex string
            self.DC_high = temp#[2:4]+temp[0:2] # Store in reverse for sending command
            # print(self.DC_high)
        else:
            t_l = self.T_low[2:4]+self.T_low[0:2]
            temp = int((dc/100.0)*int(self.T_low,16))
            temp = '%0*X'%(4,temp)
            self.DC_low = temp#[2:4]+temp[0:2]
            # print(self.DC_low)
        # self.set_Timing()


    def Alloff(self):
        print('Alloff')
        cmd = self.UID+'00010402000000'
        n_cmd = self.assemble_command(cmd,'w')
        res = self.send(n_cmd)
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
                print('No action')
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
                if not self.append_to_file:
                    action = True

            # print(self.ACT_ON)

        if action:
            temp_blk = 0
            for act in self.ACT_ON:
                shift_act = 1 << act-1
                temp_blk |= shift_act
            temp_blk = '%0*X'%(32,temp_blk)

            # print(temp_blk)
            blk1 = temp_blk[24:]
            # blk1 = blk1[6:]+blk1[4:6]+blk1[2:4]+blk1[0:2]
            blk2 = temp_blk[16:24]
            # blk2 = blk2[6:]+blk2[4:6]+blk2[2:4]+blk2[0:2]
            blk3 = '00000000'
            blk4 = '00000000'
            if self.ACT_BLKS == '03':
                blk3 = temp_blk[8:16]
                # blk3 = blk3[6:]+blk3[4:6]+blk3[2:4]+blk3[0:2]
            if self.ACT_BLKS == '04':
                blk3 = temp_blk[8:16]
                # blk3 = blk3[6:]+blk3[4:6]+blk3[2:4]+blk3[0:2]
                blk4 = temp_blk[0:8]
                # blk4 = blk4[6:]+blk4[4:6]+blk4[2:4]+blk4[0:2]

            # Blk 0
            print(self.OP_Mode)
            blk0 = '00' + self.ACT_BLKS + self.ACT_Mode + self.OP_Mode
            cmd0 = self.UID+ '000104' + blk0#+'0000'
                    #|UID     |BlkAdr |data |padding
            #(9552D9D0F35902E0)
            # Blk 1
            cmd1 = self.UID+ '010104' + blk1 #+ '0000'
            #Blk 2
            cmd2 = self.UID+ '020104' + blk2 #+ '0000'
            cmd3 = self.UID+ '030104' + blk3 #+ '0000'
            cmd4 = self.UID+ '040104' + blk4 #+ '0000'
            n_cmd0 = self.assemble_command(cmd0,'w')
            n_cmd1 = self.assemble_command(cmd1,'w')
            n_cmd2 = self.assemble_command(cmd2,'w')
            n_cmd3 = self.assemble_command(cmd3,'w')
            n_cmd4 = self.assemble_command(cmd4,'w')
            state = self.send(n_cmd1)
            state = self.send(n_cmd2)
            if self.ACT_BLKS == '03':
                state = self.send(n_cmd3)
            if self.ACT_BLKS == '04':
                state = self.send(n_cmd3)
                state = self.send(n_cmd4)
            state = self.send(n_cmd0)
            if self.append_to_file:
                print('writing')
                self.preset_file.write(cmd1+'\n')
                self.preset_file.write(cmd2+'\n')
                if self.ACT_BLKS == '03':
                    self.preset_file.write(cmd3+'\n')
                if self.ACT_BLKS == '04':
                    self.preset_file.write(cmd3+'\n')
                    self.preset_file.write(cmd4+'\n')
                self.preset_file.write(cmd0+'\n')
                self.display_preset.write(str(self.ACT_ON)+',')

        else:
            cmd = self.UID+'00010402000000'
            n_cmd = self.assemble_command(cmd,'w')
            res = self.send(n_cmd)


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


    def assemble_command(self,cmd,mode):
        temp_cmd = []
        for i in range(0,len(cmd),2):
            temp_cmd.append(int(cmd[i:i+2],16))
        if mode == 'w':
            cmd_array = self.data_w_header + temp_cmd
        elif mode == 'r':
            cmd_array = self.data_r_header + temp_cmd
        return cmd_array


    def preset_num2name(self,preset,num):
        if preset == 1:
            return 'sweep'
        elif preset == 2:
            return '2i_blk'
        return options[num]




if __name__ == '__main__':
    vr = USB_VR_PRTCL()
    vr.connect()
    if vr.active_flag:
        vr.get_inventory()
    vr.disconnect()
