# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vr_gui_layout.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1121, 813)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    border: 2px solid black;\n"
"    height: 30px; \n"
"    width: 261px; \n"
"    background-color: rgb(149, 27, 218);\n"
"    margin: 2px;\n"
"    \n"
"}\n"
"QTabBar::tab:selected{\n"
"    background-color: rgb(218, 58, 245);    \n"
"    margin: 2px;\n"
"}\n"
"QTabWidget{\n"
"    background-color: rgb(149, 27, 218);}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.Manual = QtWidgets.QWidget()
        self.Manual.setAutoFillBackground(False)
        self.Manual.setStyleSheet("QPushButton {    font-size: 20pt;}\n"
"QLabel {font-size: 20pt;}\n"
"QRadioButton{font-size: 20pt;}\n"
"")
        self.Manual.setObjectName("Manual")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.Manual)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 10, 766, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalLayoutWidget_7.sizePolicy().hasHeightForWidth())
        self.horizontalLayoutWidget_7.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.multi_modal = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.multi_modal.sizePolicy().hasHeightForWidth())
        self.multi_modal.setSizePolicy(sizePolicy)
        self.multi_modal.setMaximum(1)
        self.multi_modal.setOrientation(QtCore.Qt.Vertical)
        self.multi_modal.setObjectName("multi_modal")
        self.horizontalLayout_5.addWidget(self.multi_modal)
        spacerItem4 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.threeD_touch = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.threeD_touch.sizePolicy().hasHeightForWidth())
        self.threeD_touch.setSizePolicy(sizePolicy)
        self.threeD_touch.setMaximum(1)
        self.threeD_touch.setOrientation(QtCore.Qt.Vertical)
        self.threeD_touch.setObjectName("threeD_touch")
        self.horizontalLayout_5.addWidget(self.threeD_touch)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.single_pulse_dur_label = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.single_pulse_dur_label.sizePolicy().hasHeightForWidth())
        self.single_pulse_dur_label.setSizePolicy(sizePolicy)
        self.single_pulse_dur_label.setStyleSheet("QLabel {\n"
"font-size: 20pt;\n"
"}")
        self.single_pulse_dur_label.setScaledContents(True)
        self.single_pulse_dur_label.setObjectName("single_pulse_dur_label")
        self.horizontalLayout_6.addWidget(self.single_pulse_dur_label)
        self.single_pulse_dur_text = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.single_pulse_dur_text.sizePolicy().hasHeightForWidth())
        self.single_pulse_dur_text.setSizePolicy(sizePolicy)
        self.single_pulse_dur_text.setObjectName("single_pulse_dur_text")
        self.horizontalLayout_6.addWidget(self.single_pulse_dur_text)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.pulse_mode = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pulse_mode.sizePolicy().hasHeightForWidth())
        self.pulse_mode.setSizePolicy(sizePolicy)
        self.pulse_mode.setStyleSheet("")
        self.pulse_mode.setMaximum(1)
        self.pulse_mode.setOrientation(QtCore.Qt.Vertical)
        self.pulse_mode.setObjectName("pulse_mode")
        self.horizontalLayout_7.addWidget(self.pulse_mode)
        spacerItem8 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.pulse_duration = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pulse_duration.sizePolicy().hasHeightForWidth())
        self.pulse_duration.setSizePolicy(sizePolicy)
        self.pulse_duration.setMaximum(5000)
        self.pulse_duration.setSingleStep(10)
        self.pulse_duration.setProperty("value", 500)
        self.pulse_duration.setOrientation(QtCore.Qt.Horizontal)
        self.pulse_duration.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pulse_duration.setTickInterval(500)
        self.pulse_duration.setObjectName("pulse_duration")
        self.horizontalLayout_7.addWidget(self.pulse_duration)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.hf_mod = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.hf_mod.sizePolicy().hasHeightForWidth())
        self.hf_mod.setSizePolicy(sizePolicy)
        self.hf_mod.setAutoExclusive(False)
        self.hf_mod.setObjectName("hf_mod")
        self.verticalLayout_5.addWidget(self.hf_mod)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.h_dc_text = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.h_dc_text.sizePolicy().hasHeightForWidth())
        self.h_dc_text.setSizePolicy(sizePolicy)
        self.h_dc_text.setObjectName("h_dc_text")
        self.verticalLayout_2.addWidget(self.h_dc_text)
        self.h_dc = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.h_dc.sizePolicy().hasHeightForWidth())
        self.h_dc.setSizePolicy(sizePolicy)
        self.h_dc.setAutoFillBackground(False)
        self.h_dc.setMaximum(100)
        self.h_dc.setSliderPosition(50)
        self.h_dc.setOrientation(QtCore.Qt.Horizontal)
        self.h_dc.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.h_dc.setTickInterval(10)
        self.h_dc.setObjectName("h_dc")
        self.verticalLayout_2.addWidget(self.h_dc)
        self.pulse_Hfreq_text = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pulse_Hfreq_text.sizePolicy().hasHeightForWidth())
        self.pulse_Hfreq_text.setSizePolicy(sizePolicy)
        self.pulse_Hfreq_text.setBaseSize(QtCore.QSize(50, 50))
        self.pulse_Hfreq_text.setObjectName("pulse_Hfreq_text")
        self.verticalLayout_2.addWidget(self.pulse_Hfreq_text)
        self.pulse_Hfreq = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pulse_Hfreq.sizePolicy().hasHeightForWidth())
        self.pulse_Hfreq.setSizePolicy(sizePolicy)
        self.pulse_Hfreq.setMinimum(100)
        self.pulse_Hfreq.setMaximum(1000)
        self.pulse_Hfreq.setSingleStep(10)
        self.pulse_Hfreq.setPageStep(100)
        self.pulse_Hfreq.setProperty("value", 100)
        self.pulse_Hfreq.setOrientation(QtCore.Qt.Horizontal)
        self.pulse_Hfreq.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pulse_Hfreq.setTickInterval(100)
        self.pulse_Hfreq.setObjectName("pulse_Hfreq")
        self.verticalLayout_2.addWidget(self.pulse_Hfreq)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.lf_mod = QtWidgets.QRadioButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lf_mod.sizePolicy().hasHeightForWidth())
        self.lf_mod.setSizePolicy(sizePolicy)
        self.lf_mod.setAutoExclusive(False)
        self.lf_mod.setObjectName("lf_mod")
        self.verticalLayout_5.addWidget(self.lf_mod)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.l_dc_text = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.l_dc_text.sizePolicy().hasHeightForWidth())
        self.l_dc_text.setSizePolicy(sizePolicy)
        self.l_dc_text.setObjectName("l_dc_text")
        self.verticalLayout_3.addWidget(self.l_dc_text)
        self.l_dc = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.l_dc.sizePolicy().hasHeightForWidth())
        self.l_dc.setSizePolicy(sizePolicy)
        self.l_dc.setAutoFillBackground(False)
        self.l_dc.setMaximum(100)
        self.l_dc.setProperty("value", 50)
        self.l_dc.setOrientation(QtCore.Qt.Horizontal)
        self.l_dc.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.l_dc.setTickInterval(10)
        self.l_dc.setObjectName("l_dc")
        self.verticalLayout_3.addWidget(self.l_dc)
        self.pulse_Lfreq_text = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pulse_Lfreq_text.sizePolicy().hasHeightForWidth())
        self.pulse_Lfreq_text.setSizePolicy(sizePolicy)
        self.pulse_Lfreq_text.setObjectName("pulse_Lfreq_text")
        self.verticalLayout_3.addWidget(self.pulse_Lfreq_text)
        self.pulse_Lfreq = QtWidgets.QSlider(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pulse_Lfreq.sizePolicy().hasHeightForWidth())
        self.pulse_Lfreq.setSizePolicy(sizePolicy)
        self.pulse_Lfreq.setProperty("value", 2)
        self.pulse_Lfreq.setOrientation(QtCore.Qt.Horizontal)
        self.pulse_Lfreq.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pulse_Lfreq.setTickInterval(10)
        self.pulse_Lfreq.setObjectName("pulse_Lfreq")
        self.verticalLayout_3.addWidget(self.pulse_Lfreq)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.all_off = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.all_off.sizePolicy().hasHeightForWidth())
        self.all_off.setSizePolicy(sizePolicy)
        self.all_off.setMinimumSize(QtCore.QSize(50, 50))
        self.all_off.setObjectName("all_off")
        self.verticalLayout_4.addWidget(self.all_off)
        self.active_selected = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.active_selected.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.active_selected.sizePolicy().hasHeightForWidth())
        self.active_selected.setSizePolicy(sizePolicy)
        self.active_selected.setMinimumSize(QtCore.QSize(50, 50))
        self.active_selected.setObjectName("active_selected")
        self.verticalLayout_4.addWidget(self.active_selected)
        self.set_time = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.set_time.sizePolicy().hasHeightForWidth())
        self.set_time.setSizePolicy(sizePolicy)
        self.set_time.setMinimumSize(QtCore.QSize(50, 50))
        self.set_time.setObjectName("set_time")
        self.verticalLayout_4.addWidget(self.set_time)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.append_preset_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.append_preset_name.sizePolicy().hasHeightForWidth())
        self.append_preset_name.setSizePolicy(sizePolicy)
        self.append_preset_name.setObjectName("append_preset_name")
        self.verticalLayout_4.addWidget(self.append_preset_name)
        self.append_preset = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.append_preset.sizePolicy().hasHeightForWidth())
        self.append_preset.setSizePolicy(sizePolicy)
        self.append_preset.setMinimumSize(QtCore.QSize(0, 50))
        self.append_preset.setCheckable(True)
        self.append_preset.setObjectName("append_preset")
        self.verticalLayout_4.addWidget(self.append_preset)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.Manual, "")
        self.Automatic = QtWidgets.QWidget()
        self.Automatic.setObjectName("Automatic")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Automatic)
        self.verticalLayout.setObjectName("verticalLayout")
        self.preset_button = QtWidgets.QPushButton(self.Automatic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_button.sizePolicy().hasHeightForWidth())
        self.preset_button.setSizePolicy(sizePolicy)
        self.preset_button.setMinimumSize(QtCore.QSize(0, 60))
        self.preset_button.setMaximumSize(QtCore.QSize(16777215, 500))
        self.preset_button.setObjectName("preset_button")
        self.verticalLayout.addWidget(self.preset_button)
        self.tab_position = QtWidgets.QTabWidget(self.Automatic)
        self.tab_position.setStyleSheet("QTabBar::tab { \n"
"    height: 120px; \n"
"    width: 120px; \n"
"}\n"
"QTabBar::tab:first {\n"
"    border-image: url(/home/rschloen/haptic_vr/GUI//img/preset_stomach.png);\n"
"}\n"
"\n"
"")
        self.tab_position.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab_position.setElideMode(QtCore.Qt.ElideLeft)
        self.tab_position.setObjectName("tab_position")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setStyleSheet("")
        self.tab_1.setObjectName("tab_1")
        self.tab_position.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.sweep_type = QtWidgets.QComboBox(self.tab_2)
        self.sweep_type.setGeometry(QtCore.QRect(20, 30, 181, 41))
        self.sweep_type.setObjectName("sweep_type")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.sweep_type.addItem("")
        self.tab_position.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Act18 = QtWidgets.QPushButton(self.tab_3)
        self.Act18.setGeometry(QtCore.QRect(330, 320, 50, 50))
        self.Act18.setText("")
        self.Act18.setCheckable(True)
        self.Act18.setObjectName("Act18")
        self.Act10 = QtWidgets.QPushButton(self.tab_3)
        self.Act10.setGeometry(QtCore.QRect(480, 220, 50, 50))
        self.Act10.setAutoFillBackground(False)
        self.Act10.setText("")
        self.Act10.setCheckable(True)
        self.Act10.setObjectName("Act10")
        self.Act5 = QtWidgets.QPushButton(self.tab_3)
        self.Act5.setGeometry(QtCore.QRect(230, 220, 50, 50))
        self.Act5.setText("")
        self.Act5.setCheckable(True)
        self.Act5.setObjectName("Act5")
        self.Act11 = QtWidgets.QPushButton(self.tab_3)
        self.Act11.setGeometry(QtCore.QRect(250, 270, 50, 50))
        self.Act11.setText("")
        self.Act11.setCheckable(True)
        self.Act11.setObjectName("Act11")
        self.Act31 = QtWidgets.QPushButton(self.tab_3)
        self.Act31.setGeometry(QtCore.QRect(430, 420, 50, 50))
        self.Act31.setText("")
        self.Act31.setCheckable(True)
        self.Act31.setObjectName("Act31")
        self.Act2 = QtWidgets.QPushButton(self.tab_3)
        self.Act2.setGeometry(QtCore.QRect(300, 170, 50, 50))
        self.Act2.setText("")
        self.Act2.setCheckable(True)
        self.Act2.setObjectName("Act2")
        self.Act33 = QtWidgets.QPushButton(self.tab_3)
        self.Act33.setGeometry(QtCore.QRect(250, 470, 50, 50))
        self.Act33.setText("")
        self.Act33.setCheckable(True)
        self.Act33.setObjectName("Act33")
        self.Act22 = QtWidgets.QPushButton(self.tab_3)
        self.Act22.setGeometry(QtCore.QRect(250, 370, 50, 50))
        self.Act22.setText("")
        self.Act22.setCheckable(True)
        self.Act22.setObjectName("Act22")
        self.Act16 = QtWidgets.QPushButton(self.tab_3)
        self.Act16.setGeometry(QtCore.QRect(230, 320, 50, 50))
        self.Act16.setText("")
        self.Act16.setCheckable(True)
        self.Act16.setObjectName("Act16")
        self.Act25 = QtWidgets.QPushButton(self.tab_3)
        self.Act25.setGeometry(QtCore.QRect(400, 370, 50, 50))
        self.Act25.setText("")
        self.Act25.setCheckable(True)
        self.Act25.setObjectName("Act25")
        self.Act13 = QtWidgets.QPushButton(self.tab_3)
        self.Act13.setGeometry(QtCore.QRect(350, 270, 50, 50))
        self.Act13.setText("")
        self.Act13.setCheckable(True)
        self.Act13.setObjectName("Act13")
        self.Act30 = QtWidgets.QPushButton(self.tab_3)
        self.Act30.setGeometry(QtCore.QRect(380, 420, 50, 50))
        self.Act30.setText("")
        self.Act30.setCheckable(True)
        self.Act30.setObjectName("Act30")
        self.Act36 = QtWidgets.QPushButton(self.tab_3)
        self.Act36.setGeometry(QtCore.QRect(460, 470, 50, 50))
        self.Act36.setText("")
        self.Act36.setCheckable(True)
        self.Act36.setObjectName("Act36")
        self.Act6 = QtWidgets.QPushButton(self.tab_3)
        self.Act6.setGeometry(QtCore.QRect(280, 220, 50, 50))
        self.Act6.setText("")
        self.Act6.setCheckable(True)
        self.Act6.setObjectName("Act6")
        self.Act24 = QtWidgets.QPushButton(self.tab_3)
        self.Act24.setGeometry(QtCore.QRect(350, 370, 50, 50))
        self.Act24.setText("")
        self.Act24.setCheckable(True)
        self.Act24.setObjectName("Act24")
        self.Act26 = QtWidgets.QPushButton(self.tab_3)
        self.Act26.setGeometry(QtCore.QRect(450, 370, 50, 50))
        self.Act26.setText("")
        self.Act26.setCheckable(True)
        self.Act26.setObjectName("Act26")
        self.Act14 = QtWidgets.QPushButton(self.tab_3)
        self.Act14.setGeometry(QtCore.QRect(400, 270, 50, 50))
        self.Act14.setText("")
        self.Act14.setCheckable(True)
        self.Act14.setObjectName("Act14")
        self.Act4 = QtWidgets.QPushButton(self.tab_3)
        self.Act4.setGeometry(QtCore.QRect(460, 170, 50, 50))
        self.Act4.setText("")
        self.Act4.setCheckable(True)
        self.Act4.setObjectName("Act4")
        self.Act29 = QtWidgets.QPushButton(self.tab_3)
        self.Act29.setGeometry(QtCore.QRect(330, 420, 50, 50))
        self.Act29.setText("")
        self.Act29.setCheckable(True)
        self.Act29.setObjectName("Act29")
        self.Act9 = QtWidgets.QPushButton(self.tab_3)
        self.Act9.setGeometry(QtCore.QRect(430, 220, 50, 50))
        self.Act9.setText("")
        self.Act9.setCheckable(True)
        self.Act9.setObjectName("Act9")
        self.Act34 = QtWidgets.QPushButton(self.tab_3)
        self.Act34.setGeometry(QtCore.QRect(300, 470, 50, 50))
        self.Act34.setText("")
        self.Act34.setCheckable(True)
        self.Act34.setObjectName("Act34")
        self.Act12 = QtWidgets.QPushButton(self.tab_3)
        self.Act12.setGeometry(QtCore.QRect(300, 270, 50, 50))
        self.Act12.setText("")
        self.Act12.setCheckable(True)
        self.Act12.setChecked(False)
        self.Act12.setObjectName("Act12")
        self.Act8 = QtWidgets.QPushButton(self.tab_3)
        self.Act8.setGeometry(QtCore.QRect(380, 220, 50, 50))
        self.Act8.setText("")
        self.Act8.setCheckable(True)
        self.Act8.setChecked(False)
        self.Act8.setAutoExclusive(False)
        self.Act8.setObjectName("Act8")
        self.Act23 = QtWidgets.QPushButton(self.tab_3)
        self.Act23.setGeometry(QtCore.QRect(300, 370, 50, 50))
        self.Act23.setText("")
        self.Act23.setCheckable(True)
        self.Act23.setObjectName("Act23")
        self.Act28 = QtWidgets.QPushButton(self.tab_3)
        self.Act28.setGeometry(QtCore.QRect(280, 420, 50, 50))
        self.Act28.setText("")
        self.Act28.setCheckable(True)
        self.Act28.setObjectName("Act28")
        self.Act7 = QtWidgets.QPushButton(self.tab_3)
        self.Act7.setGeometry(QtCore.QRect(330, 220, 50, 50))
        self.Act7.setText("")
        self.Act7.setCheckable(True)
        self.Act7.setObjectName("Act7")
        self.Act20 = QtWidgets.QPushButton(self.tab_3)
        self.Act20.setGeometry(QtCore.QRect(430, 320, 50, 50))
        self.Act20.setText("")
        self.Act20.setCheckable(True)
        self.Act20.setObjectName("Act20")
        self.Act27 = QtWidgets.QPushButton(self.tab_3)
        self.Act27.setGeometry(QtCore.QRect(230, 420, 50, 50))
        self.Act27.setText("")
        self.Act27.setCheckable(True)
        self.Act27.setObjectName("Act27")
        self.Act21 = QtWidgets.QPushButton(self.tab_3)
        self.Act21.setGeometry(QtCore.QRect(480, 320, 50, 50))
        self.Act21.setText("")
        self.Act21.setCheckable(True)
        self.Act21.setObjectName("Act21")
        self.Act15 = QtWidgets.QPushButton(self.tab_3)
        self.Act15.setGeometry(QtCore.QRect(450, 270, 50, 50))
        self.Act15.setText("")
        self.Act15.setCheckable(True)
        self.Act15.setObjectName("Act15")
        self.Act1 = QtWidgets.QPushButton(self.tab_3)
        self.Act1.setGeometry(QtCore.QRect(250, 170, 50, 50))
        self.Act1.setAutoFillBackground(False)
        self.Act1.setStyleSheet("")
        self.Act1.setText("")
        self.Act1.setCheckable(True)
        self.Act1.setChecked(False)
        self.Act1.setObjectName("Act1")
        self.Act19 = QtWidgets.QPushButton(self.tab_3)
        self.Act19.setGeometry(QtCore.QRect(380, 320, 50, 50))
        self.Act19.setText("")
        self.Act19.setCheckable(True)
        self.Act19.setObjectName("Act19")
        self.Act35 = QtWidgets.QPushButton(self.tab_3)
        self.Act35.setGeometry(QtCore.QRect(410, 470, 50, 50))
        self.Act35.setText("")
        self.Act35.setCheckable(True)
        self.Act35.setObjectName("Act35")
        self.Act17 = QtWidgets.QPushButton(self.tab_3)
        self.Act17.setGeometry(QtCore.QRect(280, 320, 50, 50))
        self.Act17.setText("")
        self.Act17.setCheckable(True)
        self.Act17.setObjectName("Act17")
        self.Act3 = QtWidgets.QPushButton(self.tab_3)
        self.Act3.setGeometry(QtCore.QRect(410, 170, 50, 50))
        self.Act3.setText("")
        self.Act3.setCheckable(True)
        self.Act3.setChecked(False)
        self.Act3.setAutoExclusive(True)
        self.Act3.setObjectName("Act3")
        self.Act32 = QtWidgets.QPushButton(self.tab_3)
        self.Act32.setGeometry(QtCore.QRect(480, 420, 50, 50))
        self.Act32.setText("")
        self.Act32.setCheckable(True)
        self.Act32.setObjectName("Act32")
        self.tab_position.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tab_position)
        self.tabWidget.addTab(self.Automatic, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.PORT = QtWidgets.QLabel(self.Settings)
        self.PORT.setGeometry(QtCore.QRect(180, 20, 241, 21))
        self.PORT.setObjectName("PORT")
        self.rf_power = QtWidgets.QSlider(self.Settings)
        self.rf_power.setGeometry(QtCore.QRect(40, 170, 160, 21))
        self.rf_power.setMinimum(4)
        self.rf_power.setMaximum(12)
        self.rf_power.setProperty("value", 4)
        self.rf_power.setSliderPosition(4)
        self.rf_power.setOrientation(QtCore.Qt.Horizontal)
        self.rf_power.setInvertedAppearance(False)
        self.rf_power.setInvertedControls(False)
        self.rf_power.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.rf_power.setTickInterval(1)
        self.rf_power.setObjectName("rf_power")
        self.label_8 = QtWidgets.QLabel(self.Settings)
        self.label_8.setGeometry(QtCore.QRect(40, 140, 91, 21))
        self.label_8.setObjectName("label_8")
        self.connect_button = QtWidgets.QPushButton(self.Settings)
        self.connect_button.setGeometry(QtCore.QRect(20, 20, 141, 25))
        self.connect_button.setObjectName("connect_button")
        self.UID = QtWidgets.QLabel(self.Settings)
        self.UID.setGeometry(QtCore.QRect(130, 60, 301, 21))
        self.UID.setObjectName("UID")
        self.rf_power_text = QtWidgets.QLabel(self.Settings)
        self.rf_power_text.setGeometry(QtCore.QRect(120, 140, 67, 21))
        self.rf_power_text.setObjectName("rf_power_text")
        self.read_uuid = QtWidgets.QPushButton(self.Settings)
        self.read_uuid.setGeometry(QtCore.QRect(20, 60, 89, 25))
        self.read_uuid.setObjectName("read_uuid")
        self.tabWidget.addTab(self.Settings, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tab_position.setCurrentIndex(2)
        self.sweep_type.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VR Haptics"))
        self.label.setText(_translate("MainWindow", "Multi-\n"
"Modal"))
        self.label_3.setText(_translate("MainWindow", "   3D\n"
"Touch"))
        self.label_2.setText(_translate("MainWindow", "Single\n"
"Pulse"))
        self.single_pulse_dur_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Single Pulse Duration(ms): </span></p></body></html>"))
        self.single_pulse_dur_text.setText(_translate("MainWindow", "500"))
        self.label_4.setText(_translate("MainWindow", "Continuous"))
        self.hf_mod.setText(_translate("MainWindow", "Pulsing (High Freq modulation)"))
        self.h_dc_text.setText(_translate("MainWindow", "Intensity: 50 %"))
        self.pulse_Hfreq_text.setText(_translate("MainWindow", "Pulsing Frequency: 100 Hz"))
        self.lf_mod.setText(_translate("MainWindow", "Repeated Pulse\n"
"(Low Freq modulation)"))
        self.l_dc_text.setText(_translate("MainWindow", "Intensity: 50 %"))
        self.pulse_Lfreq_text.setText(_translate("MainWindow", "Repeated Pulse Frequency: 2 Hz"))
        self.all_off.setText(_translate("MainWindow", "ALL OFF"))
        self.active_selected.setText(_translate("MainWindow", "Activate Selected"))
        self.set_time.setText(_translate("MainWindow", "Set Timing"))
        self.append_preset.setText(_translate("MainWindow", "Append to preset"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manual), _translate("MainWindow", "Manual"))
        self.preset_button.setText(_translate("MainWindow", "Activate Preset"))
        self.sweep_type.setCurrentText(_translate("MainWindow", "Left to Right (LR)"))
        self.sweep_type.setItemText(0, _translate("MainWindow", "Left to Right (LR)"))
        self.sweep_type.setItemText(1, _translate("MainWindow", "Right to Left (RL)"))
        self.sweep_type.setItemText(2, _translate("MainWindow", "Top to Bottom (TB)"))
        self.sweep_type.setItemText(3, _translate("MainWindow", "Bottom to Top (BT)"))
        self.sweep_type.setItemText(4, _translate("MainWindow", "+45º BT"))
        self.sweep_type.setItemText(5, _translate("MainWindow", "+45º TB"))
        self.sweep_type.setItemText(6, _translate("MainWindow", "-45º BT"))
        self.sweep_type.setItemText(7, _translate("MainWindow", "-45º TB"))
        self.sweep_type.setItemText(8, _translate("MainWindow", "Explosion"))
        self.sweep_type.setItemText(9, _translate("MainWindow", "Implosion"))
        self.tab_position.setTabText(self.tab_position.indexOf(self.tab_2), _translate("MainWindow", "Sweeping"))
        self.tab_position.setTabText(self.tab_position.indexOf(self.tab_3), _translate("MainWindow", "ABCs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Automatic), _translate("MainWindow", "Automatic"))
        self.PORT.setText(_translate("MainWindow", "Serial Port:"))
        self.label_8.setText(_translate("MainWindow", "RF Power:"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.UID.setText(_translate("MainWindow", "UID:  XX XX XX XX XX XX XX XX"))
        self.rf_power_text.setText(_translate("MainWindow", "4 Watts"))
        self.read_uuid.setText(_translate("MainWindow", "Read UID"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Settings), _translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
