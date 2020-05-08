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
        MainWindow.resize(800, 410)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.gridLayoutWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.Manual = QtWidgets.QWidget()
        self.Manual.setObjectName("Manual")
        self.multi_modal = QtWidgets.QSlider(self.Manual)
        self.multi_modal.setGeometry(QtCore.QRect(50, 50, 16, 50))
        self.multi_modal.setMaximum(1)
        self.multi_modal.setOrientation(QtCore.Qt.Vertical)
        self.multi_modal.setObjectName("multi_modal")
        self.pulse_mode = QtWidgets.QSlider(self.Manual)
        self.pulse_mode.setGeometry(QtCore.QRect(110, 50, 16, 50))
        self.pulse_mode.setMaximum(1)
        self.pulse_mode.setOrientation(QtCore.Qt.Vertical)
        self.pulse_mode.setObjectName("pulse_mode")
        self.threeD_touch = QtWidgets.QSlider(self.Manual)
        self.threeD_touch.setGeometry(QtCore.QRect(170, 50, 16, 50))
        self.threeD_touch.setMaximum(1)
        self.threeD_touch.setOrientation(QtCore.Qt.Vertical)
        self.threeD_touch.setObjectName("threeD_touch")
        self.haptic_intensity = QtWidgets.QSlider(self.Manual)
        self.haptic_intensity.setGeometry(QtCore.QRect(40, 190, 160, 16))
        self.haptic_intensity.setAutoFillBackground(False)
        self.haptic_intensity.setOrientation(QtCore.Qt.Horizontal)
        self.haptic_intensity.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.haptic_intensity.setTickInterval(10)
        self.haptic_intensity.setObjectName("haptic_intensity")
        self.pushButton = QtWidgets.QPushButton(self.Manual)
        self.pushButton.setGeometry(QtCore.QRect(340, 50, 51, 41))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 30, 51, 41))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.Manual)
        self.label.setGeometry(QtCore.QRect(40, 0, 67, 61))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.Manual)
        self.label_3.setGeometry(QtCore.QRect(160, 0, 67, 61))
        self.label_3.setObjectName("label_3")
        self.pulse_freq = QtWidgets.QSlider(self.Manual)
        self.pulse_freq.setGeometry(QtCore.QRect(40, 250, 160, 16))
        self.pulse_freq.setOrientation(QtCore.Qt.Horizontal)
        self.pulse_freq.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pulse_freq.setTickInterval(10)
        self.pulse_freq.setObjectName("pulse_freq")
        self.pulse_sensitivity = QtWidgets.QSlider(self.Manual)
        self.pulse_sensitivity.setGeometry(QtCore.QRect(40, 310, 160, 16))
        self.pulse_sensitivity.setOrientation(QtCore.Qt.Horizontal)
        self.pulse_sensitivity.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.pulse_sensitivity.setTickInterval(10)
        self.pulse_sensitivity.setObjectName("pulse_sensitivity")
        self.label_2 = QtWidgets.QLabel(self.Manual)
        self.label_2.setGeometry(QtCore.QRect(100, 0, 67, 61))
        self.label_2.setObjectName("label_2")
        self.haptic_int_text = QtWidgets.QLabel(self.Manual)
        self.haptic_int_text.setGeometry(QtCore.QRect(40, 160, 191, 17))
        self.haptic_int_text.setObjectName("haptic_int_text")
        self.pulse_freq_text = QtWidgets.QLabel(self.Manual)
        self.pulse_freq_text.setGeometry(QtCore.QRect(40, 220, 201, 17))
        self.pulse_freq_text.setObjectName("pulse_freq_text")
        self.pulse_sens_text = QtWidgets.QLabel(self.Manual)
        self.pulse_sens_text.setGeometry(QtCore.QRect(40, 280, 211, 17))
        self.pulse_sens_text.setObjectName("pulse_sens_text")
        self.pushButton_3 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 60, 51, 41))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 30, 51, 41))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 60, 51, 41))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_6.setGeometry(QtCore.QRect(640, 30, 51, 41))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 80, 51, 41))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 110, 51, 41))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_9.setGeometry(QtCore.QRect(520, 80, 51, 41))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_10.setGeometry(QtCore.QRect(700, 60, 51, 41))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_11.setGeometry(QtCore.QRect(340, 100, 51, 41))
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_12.setGeometry(QtCore.QRect(580, 110, 51, 41))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_13.setGeometry(QtCore.QRect(640, 80, 51, 41))
        self.pushButton_13.setText("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_14.setGeometry(QtCore.QRect(700, 110, 51, 41))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_15.setGeometry(QtCore.QRect(400, 130, 51, 41))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_16.setGeometry(QtCore.QRect(520, 130, 51, 41))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_17.setGeometry(QtCore.QRect(640, 130, 51, 41))
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_18.setGeometry(QtCore.QRect(460, 160, 51, 41))
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_19.setGeometry(QtCore.QRect(580, 160, 51, 41))
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_20.setGeometry(QtCore.QRect(400, 180, 51, 41))
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_21.setGeometry(QtCore.QRect(520, 180, 51, 41))
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_22.setGeometry(QtCore.QRect(640, 180, 51, 41))
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_23.setGeometry(QtCore.QRect(460, 210, 51, 41))
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_24.setGeometry(QtCore.QRect(580, 210, 51, 41))
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_25.setGeometry(QtCore.QRect(400, 230, 51, 41))
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_26.setGeometry(QtCore.QRect(400, 280, 51, 41))
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_28 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_28.setGeometry(QtCore.QRect(460, 260, 51, 41))
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_29.setGeometry(QtCore.QRect(520, 230, 51, 41))
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_30.setGeometry(QtCore.QRect(580, 260, 51, 41))
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_31.setGeometry(QtCore.QRect(640, 230, 51, 41))
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_27 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_27.setGeometry(QtCore.QRect(520, 280, 51, 41))
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_32 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_32.setGeometry(QtCore.QRect(640, 280, 51, 41))
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_33.setGeometry(QtCore.QRect(340, 260, 51, 41))
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_34.setGeometry(QtCore.QRect(340, 210, 51, 41))
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_35.setGeometry(QtCore.QRect(700, 260, 51, 41))
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.Manual)
        self.pushButton_36.setGeometry(QtCore.QRect(700, 210, 51, 41))
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.tabWidget.addTab(self.Manual, "")
        self.Automatic = QtWidgets.QWidget()
        self.Automatic.setObjectName("Automatic")
        self.tab_position = QtWidgets.QTabWidget(self.Automatic)
        self.tab_position.setGeometry(QtCore.QRect(0, 0, 801, 541))
        self.tab_position.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab_position.setElideMode(QtCore.Qt.ElideLeft)
        self.tab_position.setObjectName("tab_position")
        self.Position1 = QtWidgets.QWidget()
        self.Position1.setObjectName("Position1")
        self.pushButton_37 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_37.setGeometry(QtCore.QRect(190, 50, 51, 41))
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_38.setGeometry(QtCore.QRect(250, 30, 51, 41))
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_39.setGeometry(QtCore.QRect(250, 80, 51, 41))
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_40.setGeometry(QtCore.QRect(310, 50, 51, 41))
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_41.setGeometry(QtCore.QRect(370, 30, 51, 41))
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_42.setGeometry(QtCore.QRect(370, 80, 51, 41))
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_43.setGeometry(QtCore.QRect(430, 50, 51, 41))
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_44.setGeometry(QtCore.QRect(490, 30, 51, 41))
        self.pushButton_44.setText("")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_45.setGeometry(QtCore.QRect(490, 80, 51, 41))
        self.pushButton_45.setText("")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_46.setGeometry(QtCore.QRect(190, 100, 51, 41))
        self.pushButton_46.setText("")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_47.setGeometry(QtCore.QRect(310, 100, 51, 41))
        self.pushButton_47.setText("")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_48.setGeometry(QtCore.QRect(430, 100, 51, 41))
        self.pushButton_48.setText("")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_49.setGeometry(QtCore.QRect(250, 130, 51, 41))
        self.pushButton_49.setText("")
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_50.setGeometry(QtCore.QRect(370, 130, 51, 41))
        self.pushButton_50.setText("")
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_51.setGeometry(QtCore.QRect(490, 130, 51, 41))
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_52.setGeometry(QtCore.QRect(430, 150, 51, 41))
        self.pushButton_52.setText("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_53.setGeometry(QtCore.QRect(310, 150, 51, 41))
        self.pushButton_53.setText("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_54.setGeometry(QtCore.QRect(250, 180, 51, 41))
        self.pushButton_54.setText("")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_55.setGeometry(QtCore.QRect(310, 200, 51, 41))
        self.pushButton_55.setText("")
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_56.setGeometry(QtCore.QRect(370, 180, 51, 41))
        self.pushButton_56.setText("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_57.setGeometry(QtCore.QRect(430, 200, 51, 41))
        self.pushButton_57.setText("")
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_58.setGeometry(QtCore.QRect(490, 180, 51, 41))
        self.pushButton_58.setText("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_59.setGeometry(QtCore.QRect(310, 250, 51, 41))
        self.pushButton_59.setText("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_60.setGeometry(QtCore.QRect(430, 250, 51, 41))
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_61.setGeometry(QtCore.QRect(490, 230, 51, 41))
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_62.setGeometry(QtCore.QRect(490, 280, 51, 41))
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_63.setGeometry(QtCore.QRect(370, 230, 51, 41))
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_64.setGeometry(QtCore.QRect(370, 280, 51, 41))
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_65.setGeometry(QtCore.QRect(250, 230, 51, 41))
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_66.setGeometry(QtCore.QRect(250, 280, 51, 41))
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_67.setGeometry(QtCore.QRect(190, 260, 51, 41))
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_68.setGeometry(QtCore.QRect(190, 210, 51, 41))
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_69.setGeometry(QtCore.QRect(550, 210, 51, 41))
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_70.setGeometry(QtCore.QRect(550, 260, 51, 41))
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_71.setGeometry(QtCore.QRect(550, 50, 51, 41))
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.Position1)
        self.pushButton_72.setGeometry(QtCore.QRect(550, 100, 51, 41))
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.tab_position.addTab(self.Position1, "")
        self.Position2 = QtWidgets.QWidget()
        self.Position2.setObjectName("Position2")
        self.pushButton_73 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_73.setGeometry(QtCore.QRect(550, 50, 51, 41))
        self.pushButton_73.setText("")
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_74.setGeometry(QtCore.QRect(190, 260, 51, 41))
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_75.setGeometry(QtCore.QRect(190, 100, 51, 41))
        self.pushButton_75.setText("")
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_76.setGeometry(QtCore.QRect(550, 210, 51, 41))
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_77.setGeometry(QtCore.QRect(310, 150, 51, 41))
        self.pushButton_77.setText("")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_78.setGeometry(QtCore.QRect(550, 260, 51, 41))
        self.pushButton_78.setText("")
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_79.setGeometry(QtCore.QRect(490, 180, 51, 41))
        self.pushButton_79.setText("")
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_80.setGeometry(QtCore.QRect(490, 130, 51, 41))
        self.pushButton_80.setText("")
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_81.setGeometry(QtCore.QRect(250, 130, 51, 41))
        self.pushButton_81.setText("")
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_82 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_82.setGeometry(QtCore.QRect(310, 50, 51, 41))
        self.pushButton_82.setText("")
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_83.setGeometry(QtCore.QRect(490, 30, 51, 41))
        self.pushButton_83.setText("")
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_84 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_84.setGeometry(QtCore.QRect(430, 200, 51, 41))
        self.pushButton_84.setText("")
        self.pushButton_84.setObjectName("pushButton_84")
        self.pushButton_85 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_85.setGeometry(QtCore.QRect(370, 130, 51, 41))
        self.pushButton_85.setText("")
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_86 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_86.setGeometry(QtCore.QRect(430, 150, 51, 41))
        self.pushButton_86.setText("")
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_87 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_87.setGeometry(QtCore.QRect(550, 100, 51, 41))
        self.pushButton_87.setText("")
        self.pushButton_87.setObjectName("pushButton_87")
        self.pushButton_88 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_88.setGeometry(QtCore.QRect(190, 50, 51, 41))
        self.pushButton_88.setText("")
        self.pushButton_88.setObjectName("pushButton_88")
        self.pushButton_89 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_89.setGeometry(QtCore.QRect(430, 250, 51, 41))
        self.pushButton_89.setText("")
        self.pushButton_89.setObjectName("pushButton_89")
        self.pushButton_90 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_90.setGeometry(QtCore.QRect(370, 30, 51, 41))
        self.pushButton_90.setText("")
        self.pushButton_90.setObjectName("pushButton_90")
        self.pushButton_91 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_91.setGeometry(QtCore.QRect(370, 230, 51, 41))
        self.pushButton_91.setText("")
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_92 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_92.setGeometry(QtCore.QRect(250, 30, 51, 41))
        self.pushButton_92.setText("")
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_93 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_93.setGeometry(QtCore.QRect(370, 280, 51, 41))
        self.pushButton_93.setText("")
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_94 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_94.setGeometry(QtCore.QRect(490, 80, 51, 41))
        self.pushButton_94.setText("")
        self.pushButton_94.setObjectName("pushButton_94")
        self.pushButton_95 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_95.setGeometry(QtCore.QRect(310, 200, 51, 41))
        self.pushButton_95.setText("")
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_96 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_96.setGeometry(QtCore.QRect(370, 80, 51, 41))
        self.pushButton_96.setText("")
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_97 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_97.setGeometry(QtCore.QRect(310, 250, 51, 41))
        self.pushButton_97.setText("")
        self.pushButton_97.setObjectName("pushButton_97")
        self.pushButton_98 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_98.setGeometry(QtCore.QRect(190, 210, 51, 41))
        self.pushButton_98.setText("")
        self.pushButton_98.setObjectName("pushButton_98")
        self.pushButton_99 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_99.setGeometry(QtCore.QRect(250, 230, 51, 41))
        self.pushButton_99.setText("")
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_100 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_100.setGeometry(QtCore.QRect(370, 180, 51, 41))
        self.pushButton_100.setText("")
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_101 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_101.setGeometry(QtCore.QRect(490, 230, 51, 41))
        self.pushButton_101.setText("")
        self.pushButton_101.setObjectName("pushButton_101")
        self.pushButton_102 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_102.setGeometry(QtCore.QRect(430, 100, 51, 41))
        self.pushButton_102.setText("")
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_103 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_103.setGeometry(QtCore.QRect(250, 180, 51, 41))
        self.pushButton_103.setText("")
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_104 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_104.setGeometry(QtCore.QRect(310, 100, 51, 41))
        self.pushButton_104.setText("")
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_105 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_105.setGeometry(QtCore.QRect(490, 280, 51, 41))
        self.pushButton_105.setText("")
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_106 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_106.setGeometry(QtCore.QRect(250, 80, 51, 41))
        self.pushButton_106.setText("")
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_107 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_107.setGeometry(QtCore.QRect(430, 50, 51, 41))
        self.pushButton_107.setText("")
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_108 = QtWidgets.QPushButton(self.Position2)
        self.pushButton_108.setGeometry(QtCore.QRect(250, 280, 51, 41))
        self.pushButton_108.setText("")
        self.pushButton_108.setObjectName("pushButton_108")
        self.tab_position.addTab(self.Position2, "")
        self.tabWidget.addTab(self.Automatic, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.label_7 = QtWidgets.QLabel(self.Settings)
        self.label_7.setGeometry(QtCore.QRect(130, 60, 181, 21))
        self.label_7.setObjectName("label_7")
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
        self.connect_button.setGeometry(QtCore.QRect(20, 20, 89, 25))
        self.connect_button.setObjectName("connect_button")
        self.disconnect = QtWidgets.QPushButton(self.Settings)
        self.disconnect.setGeometry(QtCore.QRect(140, 20, 91, 25))
        self.disconnect.setObjectName("disconnect")
        self.UUID = QtWidgets.QLabel(self.Settings)
        self.UUID.setGeometry(QtCore.QRect(260, 60, 151, 21))
        self.UUID.setObjectName("UUID")
        self.rf_power_text = QtWidgets.QLabel(self.Settings)
        self.rf_power_text.setGeometry(QtCore.QRect(120, 140, 67, 21))
        self.rf_power_text.setObjectName("rf_power_text")
        self.read_uuid = QtWidgets.QPushButton(self.Settings)
        self.read_uuid.setGeometry(QtCore.QRect(20, 60, 89, 25))
        self.read_uuid.setObjectName("read_uuid")
        self.tabWidget.addTab(self.Settings, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tab_position.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VR Haptics"))
        self.label.setText(_translate("MainWindow", "Multi-\n"
"Modal"))
        self.label_3.setText(_translate("MainWindow", "   3D\n"
"Touch"))
        self.label_2.setText(_translate("MainWindow", "Pulse\n"
"Mode"))
        self.haptic_int_text.setText(_translate("MainWindow", "Haptic Intensity: 0 units"))
        self.pulse_freq_text.setText(_translate("MainWindow", "Pulse Frequency: 0 units"))
        self.pulse_sens_text.setText(_translate("MainWindow", "Pulse Sensitivity: 0 units"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Manual), _translate("MainWindow", "Manual"))
        self.tab_position.setTabText(self.tab_position.indexOf(self.Position1), _translate("MainWindow", "Position 1"))
        self.tab_position.setTabText(self.tab_position.indexOf(self.Position2), _translate("MainWindow", "Position 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Automatic), _translate("MainWindow", "Automatic"))
        self.label_7.setText(_translate("MainWindow", "Detected Device:"))
        self.label_8.setText(_translate("MainWindow", "RF Power:"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.UUID.setText(_translate("MainWindow", "Device XXXXX"))
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

