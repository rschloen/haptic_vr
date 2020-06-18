# Haptic VR Project
## GUI

### Files:
`GUI/`
    `vr_gui.py`: Main executable. Displays GUI and calls NFC library
    `VR_NFC.py`: Library for NFC with serial communication
    `pyusb_VR_NFC.py`: Library for NFC with usb communication
    `vr_gui_layout.py`(and .ui): Main gui layout script, describes all widgets and is loaded in from the vr_gui.py
    `actuator_layout.py`: Custom widget that is used to generate blocks of buttons (representing actuators), in different orientations and (in future) size, that can be placed into different layouts

    other supporting file:
    `test_act_layout.ui` and `test_act_layout_horizontal.ui`: Original buttons layouts that was used to generate most of the code for `actuator_layout.py`
    `thermal_actuator_layout.ui`: Button layout for thermal actuators (in future should be added to `actuator_layout.py` or added to main window in similar way)

`img/` :holds images to display in GUI(not really used)
`preset_display_serial/` and `preset_display_usb/`: each files in this directory holds dictionary with actuators to turn on when displaying preset in gui. Files are automatically added when creating new preset in gui.

`preset_files_serial/` and `preset_files_usb/`: each files in directory holds series of commands that are read to the device. Files are automatically added when creating new preset in gui.
