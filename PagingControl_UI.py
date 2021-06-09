# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagingcontrol_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Slot, Signal

import PagingControl_icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.icon_Page_Setup = QtGui.QIcon()
        self.icon_Page_Setup.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Ind_Audio = QtGui.QIcon()
        self.icon_Ind_Audio.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/music_dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Ind_Audio.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/music.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.icon_ind_Comm = QtGui.QIcon()
        self.icon_ind_Comm.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/arrows_dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_ind_Comm.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/arrows.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.icon_Ind_Server = QtGui.QIcon()
        self.icon_Ind_Server.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/database_dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Ind_Server.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/database.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.icon_IP = QtGui.QIcon()
        self.icon_IP.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/database.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Serial = QtGui.QIcon()
        self.icon_Serial.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/share.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Audio = QtGui.QIcon()
        self.icon_Audio.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Selected = QtGui.QIcon()
        self.icon_Selected.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/selected.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Chacked_1 = QtGui.QIcon()
        self.icon_Chacked_1.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/checked_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Chacked_2 = QtGui.QIcon()
        self.icon_Chacked_2.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/checked_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Checked_3 = QtGui.QIcon()
        self.icon_Checked_3.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/checked_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Checked_4 = QtGui.QIcon()
        self.icon_Checked_4.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/checked_3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_home = QtGui.QIcon()
        self.icon_home.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_play = QtGui.QIcon()
        self.icon_play.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/play-button_dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_play.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/play-button.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.icon_pause = QtGui.QIcon()
        self.icon_pause.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/pause_dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_pause.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/pause.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.icon_stop = QtGui.QIcon()
        self.icon_stop.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/stop_dis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_stop.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/stop.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.icon_Return = QtGui.QIcon()
        self.icon_Return.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/return.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_Plug = QtGui.QIcon()
        self.icon_Plug.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/plug.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveIcon = QtGui.QIcon()
        self.saveIcon.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.indcator_Icons = [self.icon_Ind_Audio,
                               self. icon_ind_Comm, self.icon_Ind_Server]

        # Button Style
        self.main_Menu_Style = ("QPushButton{color:gray; font-size:8px; text-align: center; border-style:none;} QPushButton:Checked {color:white; background-color: #2C5579; font-size:12px; font-weight:bold;  border-style:none; text-align: center;} QPushButton:pressed {color : black ; background-color: #FF0000;border-style:none;}")
        self.RG1_Style = (
            "QPushButton{background-color:#424242; color:white;border-style:none;} QPushButton:Checked {color : black ; background-color: #E3E9F1; border-style:none;} QPushButton:pressed {color : black ; background-color: #FF0000;border-style:none;}")
        self.RG2_Style = (
            "QPushButton{background-color:#424242; color:white;border-style:none;} QPushButton:Checked {color : black ; background-color: #EBF1F0; border-style:none;} QPushButton:pressed {color : black ; background-color: #FF0000;border-style:none;}")
        self.RG3_Style = (
            "QPushButton{background-color:#424242; color:white;border-style:none;} QPushButton:Checked {color : black ; background-color: #E8E5E0; border-style:none;} QPushButton:pressed {color : black ; background-color: #FF0000;border-style:none;}")
        self.RG4_Style = (
            "QPushButton{background-color:#424242; color:white;border-style:none;} QPushButton:Checked {color : black ; background-color: #E4E6E4; border-style:none;} QPushButton:pressed {color : black ; background-color: #FF0000;border-style:none;}")
        self.FN_Style = ("QPushButton{background-color:#424242; color:white;border-style:none;} QPushButton:Checked {color : white ; background-color: #0174DF; border-style:none;} QPushButton:pressed {color : black ; background-color: #FF0000;border-style:none;}")
        self.SetupMenu_Style = (
            "QPushButton{background-color:#2e2e2e; color:white; text-align:left; border-width:0px; border-style:none;} QPushButton:Checked{color: white; border-width:0px; border-style:none}")
        self.QBtn_Border_None = (
            "QPushButton{color:white; border-style:none;}")

        self.lbl_Style = ("QLabel{color: white; }")
        self.lineEdit_Style = (
            "QLineEdit {background:white; border: 1px solid gray}")
        self.line_style = ("QFrame {color: white;}")

        self.font_Point_8 = QtGui.QFont()
        self.font_Point_8.setFamily("나눔고딕")
        self.font_Point_8.setPointSize(8)
        self.font_Point_10 = QtGui.QFont()
        self.font_Point_10.setFamily("나눔고딕")
        self.font_Point_10.setPointSize(10)
        self.font_Bold_Point_10 = QtGui.QFont()
        self.font_Bold_Point_10.setFamily("나눔고딕")
        self.font_Bold_Point_10.setPointSize(10)
        self.font_Bold_Point_10.setBold(True)
        self.font_Point_11 = QtGui.QFont()
        self.font_Point_11.setFamily("나눔고딕")
        self.font_Point_11.setPointSize(11)
        self.font_Point_12 = QtGui.QFont()
        self.font_Point_12.setFamily("나눔고딕")
        self.font_Point_12.setPointSize(12)
        self.font_Point_12_Weight_50 = QtGui.QFont()
        self.font_Point_12_Weight_50.setFamily("나눔고딕")
        self.font_Point_12_Weight_50.setPointSize(12)
        self.font_Point_12_Weight_50.setWeight(50)
        self.font_Point_13 = QtGui.QFont()
        self.font_Point_13.setFamily("나눔고딕")
        self.font_Point_13.setPointSize(13)
        self.font_Point_14 = QtGui.QFont()
        self.font_Point_14.setFamily("나눔고딕")
        self.font_Point_14.setPointSize(14)
        self.font_Bold_Point_14 = QtGui.QFont()
        self.font_Bold_Point_14.setFamily("나눔고딕")
        self.font_Bold_Point_14.setPointSize(14)
        self.font_Bold_Point_14.setBold(True)
        self.font_Bold_Point_14_Weight_75 = QtGui.QFont()
        self.font_Bold_Point_14_Weight_75.setFamily("나눔고딕")
        self.font_Bold_Point_14_Weight_75.setPointSize(14)
        self.font_Bold_Point_14_Weight_75.setBold(True)
        self.font_Bold_Point_14_Weight_75.setWeight(75)
        self.font_Bold_Point_16_Weight_75 = QtGui.QFont()
        self.font_Bold_Point_16_Weight_75.setFamily("나눔고딕")
        self.font_Bold_Point_16_Weight_75.setPointSize(16)
        self.font_Bold_Point_16_Weight_75.setBold(True)
        self.font_Bold_Point_16_Weight_75.setWeight(75)

        self.btn_RG1_ = [str(i) for i in range(26)]
        self.btn_RG2_ = [str(i) for i in range(26)]
        self.btn_RG3_ = [str(i) for i in range(26)]
        self.btn_RG4_ = [str(i) for i in range(26)]
        self.lbl_Setup_Buttons_NameTag_1 = [str(i) for i in range(24)]
        self.lbl_Setup_Buttons_NameTag_2 = [str(i) for i in range(24)]
        self.lbl_Setup_Buttons_NameTag_3 = [str(i) for i in range(24)]
        self.lbl_Setup_Buttons_NameTag_4 = [str(i) for i in range(24)]
        self.lineEdit_Setup_Buttons_Name_1_ = [str(i) for i in range(24)]
        self.lineEdit_Setup_Buttons_Name_2_ = [str(i) for i in range(24)]
        self.lineEdit_Setup_Buttons_Name_3_ = [str(i) for i in range(24)]
        self.lineEdit_Setup_Buttons_Name_4_ = [str(i) for i in range(24)]
        self.lineEdit_IP = [str(i) for i in range(4)]
        self.lineEdit_NM = [str(i) for i in range(4)]
        self.lineEdit_GW = [str(i) for i in range(4)]
        self.lineEdit_Client = [str(i) for i in range(4)]

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        # MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        icon_Pabicon = QtGui.QIcon()
        icon_Pabicon.addPixmap(QtGui.QPixmap(
            ":/Icons/icons/graphic-design.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon_Pabicon)
        MainWindow.setIconSize(QtCore.QSize(16, 16))
        MainWindow.setDocumentMode(False)
        MainWindow.setStyleSheet("QMainWindow {background-color:#151515}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Button Group
        self.buttonGroup_MainMenu = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_MainMenu.setExclusive(True)
        self.buttonGroup_MainMenu.setObjectName("buttonGroup_MainMenu")

        self.buttonGroup_RG1 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_RG1.setObjectName("buttonGroup_RG1")
        self.buttonGroup_RG1.setExclusive(False)

        self.buttonGroup_RG2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_RG2.setObjectName("buttonGroup_RG2")
        self.buttonGroup_RG2.setExclusive(False)

        self.buttonGroup_RG3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_RG3.setObjectName("buttonGroup_RG3")
        self.buttonGroup_RG3.setExclusive(False)

        self.buttonGroup_RG4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_RG4.setObjectName("buttonGroup_RG4")
        self.buttonGroup_RG4.setExclusive(False)

        self.buttonGroup_Setup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_Setup.setObjectName("buttonGroup_Setup")
        self.buttonGroup_Setup.setExclusive(True)

        self.audioButtonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.audioButtonGroup.setObjectName("audioButtonGroup")
        self.audioButtonGroup.setExclusive(True)


########################################################################################################################################################################
# Main_Menu
        self.Main_Menu = QtWidgets.QWidget(self.centralwidget)
        self.Main_Menu.setGeometry(QtCore.QRect(0, 0, 800, 40))
        self.Main_Menu.setObjectName("Main_Menu")

# Main Menu Buttons
        self.Top_Relay_Group_Sel = QtWidgets.QHBoxLayout(self.Main_Menu)
        self.Top_Relay_Group_Sel.setContentsMargins(0, 0, 0, 0)
        # self.Top_Relay_Group_Sel.setSpacing(0)

        self.btn_Main_Page_Setup = QtWidgets.QPushButton(self.Main_Menu)
        self.btn_Main_Page_Setup.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_Main_Page_Setup.setStyleSheet(
            "QPushButton{text-align:left; border-style:none;}")
        self.btn_Main_Page_Setup.setIcon(self.icon_Page_Setup)
        self.btn_Main_Page_Setup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Main_Page_Setup.setCheckable(True)
        self.Top_Relay_Group_Sel.addWidget(self.btn_Main_Page_Setup)

        self.Main_Menu_Buttons = [str(i) for i in range(4)]

        for i in range(4):
            self.Main_Menu_Buttons[i] = QtWidgets.QPushButton(self.Main_Menu)
            self.Main_Menu_Buttons[i].setMinimumSize(QtCore.QSize(150, 40))
            self.Main_Menu_Buttons[i].setFont(self.font_Point_8)
            self.Main_Menu_Buttons[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.Main_Menu_Buttons[i].setStyleSheet(self.main_Menu_Style)
            self.Main_Menu_Buttons[i].setCheckable(True)
            self.Top_Relay_Group_Sel.addWidget(self.Main_Menu_Buttons[i])

        self.Main_Menu_Buttons[0].setChecked(True)
        self.Main_Menu_Indcators = [str(i) for i in range(3)]

        for i in range(3):
            self.Main_Menu_Indcators[i] = QtWidgets.QPushButton(self.Main_Menu)
            self.Main_Menu_Indcators[i].setStyleSheet(self.QBtn_Border_None)
            self.Main_Menu_Indcators[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.Main_Menu_Indcators[i].setIcon(self.indcator_Icons[i])
            self.Main_Menu_Indcators[i].setMinimumSize(QtCore.QSize(35, 35))
            self.Main_Menu_Indcators[i].setCheckable(True)
            self.Top_Relay_Group_Sel.addWidget(self.Main_Menu_Indcators[i])

        self.buttonGroup_MainMenu.addButton(self.btn_Main_Page_Setup, 4)
        self.buttonGroup_MainMenu.addButton(self.Main_Menu_Buttons[0], 0)
        self.buttonGroup_MainMenu.addButton(self.Main_Menu_Buttons[1], 1)
        self.buttonGroup_MainMenu.addButton(self.Main_Menu_Buttons[2], 2)
        self.buttonGroup_MainMenu.addButton(self.Main_Menu_Buttons[3], 3)

#######################################################################################################################################################################
# Main View
        self.Main_View = QtWidgets.QStackedWidget(self.centralwidget)
        self.Main_View.setGeometry(QtCore.QRect(0, 40, 800, 415))
        self.Main_View.setStyleSheet("QWidget {background-color:#2e2e2e;}")
        self.Main_View.setFrameShape(QtWidgets.QFrame.NoFrame)

# Relay Group 1
        self.page_RG_1 = QtWidgets.QWidget()

        self.lbl_Rg1_Name_1 = QtWidgets.QLabel(self.page_RG_1)
        self.lbl_Rg1_Name_1.setGeometry(QtCore.QRect(30, 10, 130, 30))
        self.lbl_Rg1_Name_1.setFont(self.font_Bold_Point_16_Weight_75)
        self.lbl_Rg1_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Rg1_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.lbl_Rg1_Name_2 = QtWidgets.QLabel(self.page_RG_1)
        self.lbl_Rg1_Name_2.setGeometry(QtCore.QRect(170, 10, 131, 30))
        self.lbl_Rg1_Name_2.setFont(self.font_Point_12_Weight_50)
        self.lbl_Rg1_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Rg1_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.line_Menu_Name = QtWidgets.QFrame(self.page_RG_1)
        self.line_Menu_Name.setGeometry(QtCore.QRect(30, 40, 740, 10))
        self.line_Menu_Name.setStyleSheet(self.line_style)
        self.line_Menu_Name.setLineWidth(2)
        self.line_Menu_Name.setFrameShape(QtWidgets.QFrame.HLine)

        # RG1 Grid Widget
        self.gridLayoutWidget_RG1 = QtWidgets.QWidget(self.page_RG_1)
        self.gridLayoutWidget_RG1.setGeometry(QtCore.QRect(40, 60, 720, 340))

        self.gridLayout_RG_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_RG1)
        self.gridLayout_RG_1.setContentsMargins(0, 2, 0, 2)
        self.gridLayout_RG_1.setHorizontalSpacing(8)
        self.gridLayout_RG_1.setVerticalSpacing(10)

        for i in range(26):
            if i <= 7:
                self.btn_RG1_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG1)
                self.btn_RG1_[i].setCheckable(True)
                self.gridLayout_RG_1.addWidget(self.btn_RG1_[i], 2, i, 1, 1)
            elif i > 7 and i <= 15:
                self.btn_RG1_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG1)
                self.btn_RG1_[i].setCheckable(True)
                self.gridLayout_RG_1.addWidget(
                    self.btn_RG1_[i], 4, (i - 8), 1, 1)
            elif i > 15 and i <= 23:
                self.btn_RG1_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG1)
                self.btn_RG1_[i].setCheckable(True)
                self.gridLayout_RG_1.addWidget(
                    self.btn_RG1_[i], 6, (i - 16), 1, 1)
            elif i == 24:
                self.btn_RG1_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG1)
                self.btn_RG1_[i].setText("ALL ON")
                self.gridLayout_RG_1.addWidget(self.btn_RG1_[i], 0, 2, 1, 2)
            elif i == 25:
                self.btn_RG1_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG1)
                self.btn_RG1_[i].setText("ALL OFF")
                self.gridLayout_RG_1.addWidget(self.btn_RG1_[i], 0, 4, 1, 2)

            self.btn_RG1_[i].setFixedHeight(60)
            self.btn_RG1_[i].setFont(self.font_Point_10)
            self.btn_RG1_[i].setStyleSheet(self.RG1_Style)
            self.btn_RG1_[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.buttonGroup_RG1.addButton(self.btn_RG1_[i], i)

        # Grid Lines
        self.RG1_Lines = [str(i) for i in range(3)]
        for i in range(3):
            self.RG1_Lines[i] = QtWidgets.QFrame(self.gridLayoutWidget_RG1)
            self.RG1_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)
            self.RG1_Lines[i].setStyleSheet(self.line_style)
            self.gridLayout_RG_1.addWidget(self.RG1_Lines[i], (1+i*2), 0, 1, 8)

        self.Main_View.addWidget(self.page_RG_1)

# Relay Group 2
        self.page_RG_2 = QtWidgets.QWidget()

        self.lbl_Rg2_Name_1 = QtWidgets.QLabel(self.page_RG_2)
        self.lbl_Rg2_Name_1.setGeometry(QtCore.QRect(30, 10, 130, 30))
        self.lbl_Rg2_Name_1.setFont(self.font_Bold_Point_16_Weight_75)
        self.lbl_Rg2_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Rg2_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.lbl_Rg2_Name_2 = QtWidgets.QLabel(self.page_RG_2)
        self.lbl_Rg2_Name_2.setGeometry(QtCore.QRect(170, 10, 131, 30))
        self.lbl_Rg2_Name_2.setFont(self.font_Point_12_Weight_50)
        self.lbl_Rg2_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Rg2_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.line_Main_2 = QtWidgets.QFrame(self.page_RG_2)
        self.line_Main_2.setGeometry(QtCore.QRect(30, 40, 740, 10))
        self.line_Main_2.setStyleSheet(self.line_style)
        self.line_Main_2.setLineWidth(2)
        self.line_Main_2.setFrameShape(QtWidgets.QFrame.HLine)

        self.gridLayoutWidget_RG2 = QtWidgets.QWidget(self.page_RG_2)
        self.gridLayoutWidget_RG2.setGeometry(QtCore.QRect(40, 60, 720, 340))

        self.gridLayout_RG_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_RG2)
        self.gridLayout_RG_2.setContentsMargins(0, 2, 0, 2)
        self.gridLayout_RG_2.setHorizontalSpacing(8)
        self.gridLayout_RG_2.setVerticalSpacing(10)

        for i in range(26):
            if i <= 7:
                self.btn_RG2_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG2)
                self.btn_RG2_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG2_[i].setCheckable(True)
                self.gridLayout_RG_2.addWidget(self.btn_RG2_[i], 2, i, 1, 1)

            elif i > 7 and i <= 15:
                self.btn_RG2_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG2)
                self.btn_RG2_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG2_[i].setCheckable(True)
                self.gridLayout_RG_2.addWidget(
                    self.btn_RG2_[i], 4, (i - 8), 1, 1)
            elif i > 15 and i <= 23:
                self.btn_RG2_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG2)
                self.btn_RG2_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG2_[i].setCheckable(True)
                self.gridLayout_RG_2.addWidget(
                    self.btn_RG2_[i], 6, (i - 16), 1, 1)

            elif i == 24:
                self.btn_RG2_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG2)
                self.btn_RG2_[i].setMaximumSize(QtCore.QSize(200, 60))
                self.btn_RG2_[i].setText("ALL ON")
                self.gridLayout_RG_2.addWidget(self.btn_RG2_[i], 0, 2, 1, 2)

            elif i == 25:
                self.btn_RG2_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG2)
                self.btn_RG2_[i].setMaximumSize(QtCore.QSize(200, 60))
                self.btn_RG2_[i].setText("ALL OFF")
                self.gridLayout_RG_2.addWidget(self.btn_RG2_[i], 0, 4, 1, 2)

            self.btn_RG2_[i].setFixedHeight(60)
            self.btn_RG2_[i].setFont(self.font_Point_10)
            self.btn_RG2_[i].setStyleSheet(self.RG2_Style)
            self.btn_RG2_[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.buttonGroup_RG2.addButton(self.btn_RG2_[i], i)

        # Grid Lines
        self.RG2_Lines = [str(i) for i in range(3)]
        for i in range(3):
            self.RG2_Lines[i] = QtWidgets.QFrame(self.gridLayoutWidget_RG2)
            self.RG2_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)
            self.RG2_Lines[i].setStyleSheet(self.line_style)
            self.gridLayout_RG_2.addWidget(self.RG2_Lines[i], (1+i*2), 0, 1, 8)

        self.Main_View.addWidget(self.page_RG_2)

# Relay Group 3
        self.page_RG_3 = QtWidgets.QWidget()

        self.lbl_Rg3_Name_1 = QtWidgets.QLabel(self.page_RG_3)
        self.lbl_Rg3_Name_1.setGeometry(QtCore.QRect(30, 10, 130, 30))
        self.lbl_Rg3_Name_1.setFont(self.font_Bold_Point_16_Weight_75)
        self.lbl_Rg3_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Rg3_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.lbl_Rg3_Name_2 = QtWidgets.QLabel(self.page_RG_3)
        self.lbl_Rg3_Name_2.setGeometry(QtCore.QRect(170, 10, 131, 30))
        self.lbl_Rg3_Name_2.setFont(self.font_Point_12_Weight_50)
        self.lbl_Rg3_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Rg3_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.line_Main_3 = QtWidgets.QFrame(self.page_RG_3)
        self.line_Main_3.setGeometry(QtCore.QRect(30, 40, 740, 10))
        self.line_Main_3.setStyleSheet(self.line_style)
        self.line_Main_3.setLineWidth(2)
        self.line_Main_3.setFrameShape(QtWidgets.QFrame.HLine)

        self.gridLayoutWidget_RG3 = QtWidgets.QWidget(self.page_RG_3)
        self.gridLayoutWidget_RG3.setGeometry(QtCore.QRect(40, 60, 720, 340))

        self.gridLayout_RG_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_RG3)
        self.gridLayout_RG_3.setContentsMargins(0, 2, 0, 2)
        self.gridLayout_RG_3.setHorizontalSpacing(8)
        self.gridLayout_RG_3.setVerticalSpacing(10)

        for i in range(26):
            if i <= 7:
                self.btn_RG3_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG3)
                self.btn_RG3_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG3_[i].setCheckable(True)
                self.gridLayout_RG_3.addWidget(self.btn_RG3_[i], 2, i, 1, 1)

            elif i > 7 and i <= 15:
                self.btn_RG3_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG3)
                self.btn_RG3_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG3_[i].setCheckable(True)
                self.gridLayout_RG_3.addWidget(
                    self.btn_RG3_[i], 4, (i - 8), 1, 1)
            elif i > 15 and i <= 23:
                self.btn_RG3_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG3)
                self.btn_RG3_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG3_[i].setCheckable(True)
                self.gridLayout_RG_3.addWidget(
                    self.btn_RG3_[i], 6, (i - 16), 1, 1)

            elif i == 24:
                self.btn_RG3_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG3)
                self.btn_RG3_[i].setMaximumSize(QtCore.QSize(200, 60))
                self.btn_RG3_[i].setText("ALL ON")
                self.gridLayout_RG_3.addWidget(self.btn_RG3_[i], 0, 2, 1, 2)

            elif i == 25:
                self.btn_RG3_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG3)
                self.btn_RG3_[i].setMaximumSize(QtCore.QSize(200, 60))
                self.btn_RG3_[i].setText("ALL OFF")
                self.gridLayout_RG_3.addWidget(self.btn_RG3_[i], 0, 4, 1, 2)

            self.btn_RG3_[i].setFixedHeight(60)
            self.btn_RG3_[i].setFont(self.font_Point_10)
            self.btn_RG3_[i].setStyleSheet(self.RG3_Style)
            self.btn_RG3_[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.buttonGroup_RG3.addButton(self.btn_RG3_[i], i)

        # Grid Lines
        self.RG3_Lines = [str(i) for i in range(3)]
        for i in range(3):
            self.RG3_Lines[i] = QtWidgets.QFrame(self.gridLayoutWidget_RG3)
            self.RG3_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)
            self.RG3_Lines[i].setStyleSheet(self.line_style)
            self.gridLayout_RG_3.addWidget(self.RG3_Lines[i], (1+i*2), 0, 1, 8)

        self.Main_View.addWidget(self.page_RG_3)

# Relay Group 4
        self.page_RG_4 = QtWidgets.QWidget()

        self.lbl_RG4_Name_1 = QtWidgets.QLabel(self.page_RG_4)
        self.lbl_RG4_Name_1.setGeometry(QtCore.QRect(30, 10, 130, 30))
        self.lbl_RG4_Name_1.setFont(self.font_Bold_Point_16_Weight_75)
        self.lbl_RG4_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_RG4_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.lbl_RG4_Name_2 = QtWidgets.QLabel(self.page_RG_4)
        self.lbl_RG4_Name_2.setGeometry(QtCore.QRect(170, 10, 131, 30))
        self.lbl_RG4_Name_2.setFont(self.font_Point_12_Weight_50)
        self.lbl_RG4_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_RG4_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.line_Main_4 = QtWidgets.QFrame(self.page_RG_4)
        self.line_Main_4.setGeometry(QtCore.QRect(30, 40, 740, 10))
        self.line_Main_4.setStyleSheet(self.line_style)
        self.line_Main_4.setLineWidth(2)
        self.line_Main_4.setFrameShape(QtWidgets.QFrame.HLine)

        self.gridLayoutWidget_RG4 = QtWidgets.QWidget(self.page_RG_4)
        self.gridLayoutWidget_RG4.setGeometry(QtCore.QRect(40, 60, 720, 340))

        self.gridLayout_RG_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_RG4)
        self.gridLayout_RG_4.setContentsMargins(0, 2, 0, 2)
        self.gridLayout_RG_4.setHorizontalSpacing(8)
        self.gridLayout_RG_4.setVerticalSpacing(10)

        for i in range(26):
            if i <= 7:
                self.btn_RG4_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG4)
                self.btn_RG4_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG4_[i].setCheckable(True)
                self.gridLayout_RG_4.addWidget(self.btn_RG4_[i], 2, i, 1, 1)

            elif i > 7 and i <= 15:
                self.btn_RG4_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG4)
                self.btn_RG4_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG4_[i].setCheckable(True)
                self.gridLayout_RG_4.addWidget(
                    self.btn_RG4_[i], 4, (i - 8), 1, 1)
            elif i > 15 and i <= 23:
                self.btn_RG4_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG4)
                self.btn_RG4_[i].setMaximumSize(QtCore.QSize(85, 60))
                self.btn_RG4_[i].setCheckable(True)
                self.gridLayout_RG_4.addWidget(
                    self.btn_RG4_[i], 6, (i - 16), 1, 1)

            elif i == 24:
                self.btn_RG4_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG4)
                self.btn_RG4_[i].setMaximumSize(QtCore.QSize(200, 60))
                self.btn_RG4_[i].setText("ALL ON")
                self.gridLayout_RG_4.addWidget(self.btn_RG4_[i], 0, 2, 1, 2)

            elif i == 25:
                self.btn_RG4_[i] = QtWidgets.QPushButton(
                    self.gridLayoutWidget_RG4)
                self.btn_RG4_[i].setMaximumSize(QtCore.QSize(200, 60))
                self.btn_RG4_[i].setText("ALL OFF")
                self.gridLayout_RG_4.addWidget(self.btn_RG4_[i], 0, 4, 1, 2)

            self.btn_RG4_[i].setFixedHeight(60)
            self.btn_RG4_[i].setFont(self.font_Point_10)
            self.btn_RG4_[i].setStyleSheet(self.RG4_Style)
            self.btn_RG4_[i].setFocusPolicy(QtCore.Qt.NoFocus)
            self.buttonGroup_RG4.addButton(self.btn_RG4_[i], i)

        # Grid Lines
        self.RG4_Lines = [str(i) for i in range(3)]
        for i in range(3):
            self.RG4_Lines[i] = QtWidgets.QFrame(self.gridLayoutWidget_RG4)
            self.RG4_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)
            self.RG4_Lines[i].setStyleSheet(self.line_style)
            self.gridLayout_RG_4.addWidget(self.RG4_Lines[i], (1+i*2), 0, 1, 8)

        self.Main_View.addWidget(self.page_RG_4)
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Page Setup
        """
        self.page_Setup = QtWidgets.QWidget()

        # Setup Menu
        self.widget_Menu = QtWidgets.QWidget(self.page_Setup)
        self.widget_Menu.setGeometry(QtCore.QRect(0, 0, 140, 410))

        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_Menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 121, 406))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout_SetupMenu = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget)
        self.verticalLayout_SetupMenu.setObjectName("verticalLayout_SetupMenu")

        self.Setup_Buttons = [str(i) for i in range(9)]
        self.Setup_Icons = [self.icon_Page_Setup, self.icon_IP, self.icon_Serial, self.icon_Audio,
                            self.icon_Selected, self.icon_Chacked_1, self.icon_Chacked_2, self.icon_Checked_3, self.icon_Checked_4]

        self.Setup_V_Lines = [str(i) for i in range(3)]

        for i in range(3):
            self.Setup_V_Lines[i] = QtWidgets.QFrame(self.verticalLayoutWidget)
            self.Setup_V_Lines[i].setStyleSheet(self.line_style)
            self.Setup_V_Lines[i].setMinimumSize(QtCore.QSize(0, 10))
            self.Setup_V_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)

        for i in range(9):
            self.Setup_Buttons[i] = QtWidgets.QPushButton(
                self.verticalLayoutWidget)
            self.Setup_Buttons[i].setFont(self.font_Point_10)
            self.Setup_Buttons[i].setLayoutDirection(QtCore.Qt.LeftToRight)
            self.Setup_Buttons[i].setStyleSheet(self.SetupMenu_Style)
            self.Setup_Buttons[i].setIcon(self.Setup_Icons[i])
            self.Setup_Buttons[i].setFlat(True)
            self.Setup_Buttons[i].setIconSize(QtCore.QSize(30, 30))
            self.buttonGroup_Setup.addButton(self.Setup_Buttons[i], i)

        self.verticalLayout_SetupMenu.addWidget(self.Setup_V_Lines[0])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[0])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[1])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[2])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[3])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[4])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_V_Lines[1])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[5])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[6])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[7])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_Buttons[8])
        self.verticalLayout_SetupMenu.addWidget(self.Setup_V_Lines[2])

        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
# Setup FN Widget

        self.stackedWidget_Setup = QtWidgets.QStackedWidget(self.page_Setup)
        self.stackedWidget_Setup.setGeometry(QtCore.QRect(140, 0, 660, 410))

        self.page_FN = QtWidgets.QWidget()
        self.page_FN.setObjectName("page_FN")

        self.Setup_FN_Page = QtWidgets.QWidget(self.page_FN)
        self.Setup_FN_Page.setGeometry(QtCore.QRect(0, 0, 640, 410))

        self.SetFunctionBT = QtWidgets.QHBoxLayout(self.Setup_FN_Page)
        self.SetFunctionBT.setContentsMargins(20, 20, 20, 20)
        # self.Top_Relay_Group_Sel.setSpacing(0)

        self.setFunctionButton1 = QtWidgets.QPushButton(self.page_FN)
        self.setFunctionButton1.setMinimumSize(QtCore.QSize(80, 120))
        self.setFunctionButton1.setMaximumSize(QtCore.QSize(200, 120))
        self.setFunctionButton1.setStyleSheet(self.FN_Style)
        self.setFunctionButton1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setFunctionButton1.setCheckable(True)
        self.SetFunctionBT.addWidget(self.setFunctionButton1)

        self.setFunctionButton2 = QtWidgets.QPushButton(self.page_FN)
        self.setFunctionButton2.setMinimumSize(QtCore.QSize(80, 120))
        self.setFunctionButton2.setMaximumSize(QtCore.QSize(200, 120))
        self.setFunctionButton2.setStyleSheet(self.FN_Style)
        self.setFunctionButton2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setFunctionButton2.setCheckable(True)
        self.SetFunctionBT.addWidget(self.setFunctionButton2)

        self.stackedWidget_Setup.addWidget(self.page_FN)

        """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
# Setup IP Widget

        self.page_IP = QtWidgets.QWidget()
        self.page_IP.setObjectName("page_IP")

        self.Setup_IP_Page = QtWidgets.QWidget(self.page_IP)
        self.Setup_IP_Page.setGeometry(QtCore.QRect(50, 10, 431, 370))

        self.Setup_IP_Grid_Layout = QtWidgets.QGridLayout(self.Setup_IP_Page)

        self.Setup_IP_Lines = [str(i) for i in range(5)]
        for i in range(5):
            self.Setup_IP_Lines[i] = QtWidgets.QFrame(self.Setup_IP_Page)
            self.Setup_IP_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)
            self.Setup_IP_Lines[i].setStyleSheet(self.line_style)

        self.Setup_IP_Grid_Layout.addWidget(self.Setup_IP_Lines[0], 1, 0, 1, 6)
        self.Setup_IP_Grid_Layout.addWidget(self.Setup_IP_Lines[1], 7, 0, 1, 6)
        self.Setup_IP_Grid_Layout.addWidget(self.Setup_IP_Lines[2], 9, 0, 1, 6)
        self.Setup_IP_Grid_Layout.addWidget(
            self.Setup_IP_Lines[3], 11, 0, 1, 6)
        self.Setup_IP_Grid_Layout.addWidget(
            self.Setup_IP_Lines[4], 13, 0, 1, 6)

        self.lbl_Setup_IP_Menu = [str(i) for i in range(6)]
        for i in range(6):
            self.lbl_Setup_IP_Menu[i] = QtWidgets.QLabel(self.Setup_IP_Page)

            if i % 2 == 0:
                self.lbl_Setup_IP_Menu[i].setFont(self.font_Bold_Point_14)
                self.lbl_Setup_IP_Menu[i].setStyleSheet(self.lbl_Style)
                self.lbl_Setup_IP_Menu[i].setAlignment(
                    QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
            else:
                self.lbl_Setup_IP_Menu[i].setFont(self.font_Point_10)
                self.lbl_Setup_IP_Menu[i].setStyleSheet(self.lbl_Style)
                self.lbl_Setup_IP_Menu[i].setAlignment(
                    QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)

        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP_Menu[0], 0, 0)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP_Menu[1], 0, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP_Menu[2], 8, 0)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP_Menu[3], 8, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP_Menu[4], 12, 0)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP_Menu[5], 12, 1)

        self.lbl_Setup_IP = [str(i) for i in range(7)]

        for i in range(7):
            self.lbl_Setup_IP[i] = QtWidgets.QLabel(self.Setup_IP_Page)
            self.lbl_Setup_IP[i].setFont(self.font_Point_10)
            self.lbl_Setup_IP[i].setStyleSheet(self.lbl_Style)

        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[0], 4, 1, 1, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[1], 5, 1, 1, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[2], 6, 1, 1, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[3], 10, 1, 1, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[4], 14, 1, 1, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[5], 15, 1, 1, 1)
        self.Setup_IP_Grid_Layout.addWidget(self.lbl_Setup_IP[6], 16, 1, 1, 1)

        for i in range(4):
            self.lineEdit_IP[i] = QtWidgets.QLineEdit(self.Setup_IP_Page)
            self.lineEdit_IP[i].setFont(self.font_Point_10)
            self.lineEdit_IP[i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_IP[i].setMaxLength(3)
            self.Setup_IP_Grid_Layout.addWidget(
                self.lineEdit_IP[i], 4, (i + 2), 1, 1)

        for i in range(4):
            self.lineEdit_NM[i] = QtWidgets.QLineEdit(self.Setup_IP_Page)
            self.lineEdit_NM[i].setFont(self.font_Point_10)
            self.lineEdit_NM[i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_NM[i].setMaxLength(3)
            self.Setup_IP_Grid_Layout.addWidget(
                self.lineEdit_NM[i], 5, (i + 2), 1, 1)

        for i in range(4):
            self.lineEdit_GW[i] = QtWidgets.QLineEdit(self.Setup_IP_Page)
            self.lineEdit_GW[i].setFont(self.font_Point_10)
            self.lineEdit_GW[i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_GW[i].setMaxLength(3)
            self.Setup_IP_Grid_Layout.addWidget(
                self.lineEdit_GW[i], 6, (i + 2), 1, 1)

        self.lineEdit_Server_Port = QtWidgets.QLineEdit(self.Setup_IP_Page)
        self.lineEdit_Server_Port.setFont(self.font_Point_10)
        self.lineEdit_Server_Port.setStyleSheet(self.lineEdit_Style)
        self.lineEdit_Server_Port.setMaxLength(5)
        self.Setup_IP_Grid_Layout.addWidget(
            self.lineEdit_Server_Port, 10, 2, 1, 1)

        for i in range(4):
            self.lineEdit_Client[i] = QtWidgets.QLineEdit(self.Setup_IP_Page)
            self.lineEdit_Client[i].setFont(self.font_Point_10)
            self.lineEdit_Client[i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_Client[i].setMaxLength(3)
            self.Setup_IP_Grid_Layout.addWidget(
                self.lineEdit_Client[i], 14, (i + 2), 1, 1)

        self.lineEdit_Client_Port = QtWidgets.QLineEdit(self.Setup_IP_Page)
        self.lineEdit_Client_Port.setFont(self.font_Point_10)
        self.lineEdit_Client_Port.setStyleSheet(self.lineEdit_Style)
        self.lineEdit_Client_Port.setMaxLength(5)
        self.Setup_IP_Grid_Layout.addWidget(
            self.lineEdit_Client_Port, 15, 2, 1, 1)

        self.lineEdit_Client_ID = QtWidgets.QLineEdit(self.Setup_IP_Page)
        self.lineEdit_Client_ID.setFont(self.font_Point_10)
        self.lineEdit_Client_ID.setStyleSheet(self.lineEdit_Style)
        self.lineEdit_Client_ID.setMaxLength(5)
        self.Setup_IP_Grid_Layout.addWidget(
            self.lineEdit_Client_ID, 16, 2, 1, 1)

        self.btn_IP_Save = QtWidgets.QPushButton(self.page_IP)
        self.btn_IP_Save.setGeometry(QtCore.QRect(530, 350, 61, 51))
        self.btn_IP_Save.setIcon(self.saveIcon)
        self.btn_IP_Save.setStyleSheet(self.QBtn_Border_None)
        self.btn_IP_Save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_IP_Save.setIconSize(QtCore.QSize(40, 40))

        self.btn_Setup_Home = QtWidgets.QPushButton(self.page_IP)
        self.btn_Setup_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_Setup_Home.setIcon(self.icon_home)
        self.btn_Setup_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_Setup_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Setup_Home.setIconSize(QtCore.QSize(40, 40))

        self.stackedWidget_Setup.addWidget(self.page_IP)
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
시리얼 통신
        """

        self.page_Serial = QtWidgets.QWidget()

        self.Setup_Serial_Page = QtWidgets.QWidget(self.page_Serial)
        self.Setup_Serial_Page.setGeometry(QtCore.QRect(50, 30, 500, 300))

        self.Setup_Serial_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Serial_Page)
        self.Setup_Serial_Grid_Layout.setHorizontalSpacing(20)

        self.lbl_Setup_Serial_Menu_1 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_Menu_1.setFont(self.font_Bold_Point_14_Weight_75)
        self.lbl_Setup_Serial_Menu_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Serial_Menu_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_Menu_1, 0, 0, 1, 1)

        self.lbl_Setup_Serial_Menu_2 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_Menu_2.setFont(self.font_Point_10)
        self.lbl_Setup_Serial_Menu_2.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Serial_Menu_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_Menu_2, 0, 1, 1, 2)

        self.lbl_Setup_Serial_Menu_3 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_Menu_3.setFont(self.font_Bold_Point_14_Weight_75)
        self.lbl_Setup_Serial_Menu_3.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Serial_Menu_3.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_Menu_3, 4, 0, 1, 1)

        self.lbl_Setup_Serial_Menu_4 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_Menu_4.setFont(self.font_Point_10)
        self.lbl_Setup_Serial_Menu_4.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Serial_Menu_4.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_Menu_4, 4, 1, 1, 2)

        self.lbl_Setup_Serial_1 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_1.setFont(self.font_Point_10)
        self.lbl_Setup_Serial_1.setStyleSheet(self.lbl_Style)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_1, 2, 1, 1, 1)

        self.lbl_Setup_Serial_2 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_2.setFont(self.font_Point_10)
        self.lbl_Setup_Serial_2.setStyleSheet(self.lbl_Style)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_2, 6, 1, 1, 1)

        self.lbl_Setup_Serial_3 = QtWidgets.QLabel(self.Setup_Serial_Page)
        self.lbl_Setup_Serial_3.setFont(self.font_Point_10)
        self.lbl_Setup_Serial_3.setStyleSheet(self.lbl_Style)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lbl_Setup_Serial_3, 7, 1, 1, 1)

        self.Setup_Serial_Line_1 = QtWidgets.QFrame(self.Setup_Serial_Page)
        self.Setup_Serial_Line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Setup_Serial_Line_1.setStyleSheet(self.line_style)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.Setup_Serial_Line_1, 1, 0, 1, 4)
        self.Setup_Serial_Line_2 = QtWidgets.QFrame(self.Setup_Serial_Page)
        self.Setup_Serial_Line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Setup_Serial_Line_2.setStyleSheet(self.line_style)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.Setup_Serial_Line_2, 3, 0, 1, 4)
        self.Setup_Serial_Line_3 = QtWidgets.QFrame(self.Setup_Serial_Page)
        self.Setup_Serial_Line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.Setup_Serial_Line_3.setStyleSheet(self.line_style)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.Setup_Serial_Line_3, 5, 0, 1, 4)

        self.comboBox_Serial_Mode = QtWidgets.QComboBox(self.Setup_Serial_Page)
        self.comboBox_Serial_Mode.setFont(self.font_Point_10)
        self.comboBox_Serial_Mode.setMinimumSize(QtCore.QSize(120, 30))
        self.comboBox_Serial_Mode.setStyleSheet("QComboBox {color:white;}")
        self.comboBox_Serial_Mode.setModelColumn(0)
        self.comboBox_Serial_Mode.addItems(['SovicoRealy', 'DRG-116'])
        self.comboBox_Serial_Mode.setCurrentIndex(1)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.comboBox_Serial_Mode, 2, 2, 1, 2)

        self.lineEdit_Bss_Reboot_Code = QtWidgets.QLineEdit(
            self.Setup_Serial_Page)
        self.lineEdit_Bss_Reboot_Code.setFont(self.font_Point_10)
        self.lineEdit_Bss_Reboot_Code.setStyleSheet(self.lineEdit_Style)
        self.lineEdit_Bss_Reboot_Code.setMaxLength(40)
        self.Setup_Serial_Grid_Layout.addWidget(
            self.lineEdit_Bss_Reboot_Code, 6, 2, 1, 2)

        self.btn_BssReboot = QtWidgets.QPushButton(self.Setup_Serial_Page)
        self.btn_BssReboot.setMinimumSize(QtCore.QSize(100, 45))
        self.btn_BssReboot.setFont(self.font_Point_8)
        self.btn_BssReboot.setIcon(self.icon_Plug)
        self.btn_BssReboot.setIconSize(QtCore.QSize(35, 35))
        self.btn_BssReboot.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_BssReboot.setStyleSheet(self.QBtn_Border_None)
        self.Setup_Serial_Grid_Layout.addWidget(self.btn_BssReboot, 7, 2, 1, 2)

        self.btn_Serial_Save = QtWidgets.QPushButton(self.page_Serial)
        self.btn_Serial_Save.setGeometry(QtCore.QRect(530, 350, 61, 51))
        self.btn_Serial_Save.setIcon(self.saveIcon)
        self.btn_Serial_Save.setStyleSheet(self.QBtn_Border_None)
        self.btn_Serial_Save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Serial_Save.setIconSize(QtCore.QSize(40, 40))

        self.btn_Serial_Home = QtWidgets.QPushButton(self.page_Serial)
        self.btn_Serial_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_Serial_Home.setIcon(self.icon_home)
        self.btn_Serial_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_Serial_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Serial_Home.setIconSize(QtCore.QSize(40, 40))

        self.stackedWidget_Setup.addWidget(self.page_Serial)

        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
오디오 
        """

        self.page_Audio = QtWidgets.QWidget()
        self.page_Audio.setObjectName("page_Audio")

        self.Setup_Audio_Page = QtWidgets.QWidget(self.page_Audio)
        self.Setup_Audio_Page.setGeometry(QtCore.QRect(50, 50, 500, 280))
        self.Setup_Audio_Page.setObjectName("Setup_Audio_Page")

        self.Setup_Audio_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Audio_Page)
        self.Setup_Audio_Grid_Layout.setHorizontalSpacing(5)
        self.Setup_Audio_Grid_Layout.setVerticalSpacing(15)

        self.lbl_Setup_Audio_Menu_1 = QtWidgets.QLabel(self.Setup_Audio_Page)
        self.lbl_Setup_Audio_Menu_1.setFont(self.font_Bold_Point_14)
        self.lbl_Setup_Audio_Menu_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Audio_Menu_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Audio_Grid_Layout.addWidget(
            self.lbl_Setup_Audio_Menu_1, 0, 0, 1, 1)

        self.lbl_Setup_Audio_Menu_2 = QtWidgets.QLabel(self.Setup_Audio_Page)
        self.lbl_Setup_Audio_Menu_2.setFont(self.font_Point_10)
        self.lbl_Setup_Audio_Menu_2.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Audio_Menu_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Audio_Grid_Layout.addWidget(
            self.lbl_Setup_Audio_Menu_2, 0, 1, 1, 1)

        self.Setup_Audio_Line_1 = QtWidgets.QFrame(self.Setup_Audio_Page)
        self.Setup_Audio_Line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Setup_Audio_Line_1.setStyleSheet(self.line_style)
        self.Setup_Audio_Grid_Layout.addWidget(
            self.Setup_Audio_Line_1, 1, 0, 1, 4)

        self.audioPlayButton = ['i']*9
        for i in range(len(self.audioPlayButton)):
            self.audioPlayButton[i] = QtWidgets.QPushButton(
                '{}'.format(i+1), self.Setup_Audio_Page)
            self.audioPlayButton[i].setStyleSheet(self.FN_Style)
            self.audioPlayButton[i].setMinimumSize(QtCore.QSize(100, 50))
            self.Setup_Audio_Grid_Layout.addWidget(
                self.audioPlayButton[i], i/4+2, i % 4, 1, 1)
            self.audioButtonGroup.addButton(self.audioPlayButton[i], i)

        '''

        self.lbl_Setup_Audio_1 = QtWidgets.QLabel(self.Setup_Audio_Page)
        self.lbl_Setup_Audio_1.setFont(self.font_Point_10)
        self.lbl_Setup_Audio_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Audio_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Setup_Audio_Grid_Layout.addWidget(self.lbl_Setup_Audio_1, 2, 1, 1, 1)

        self.lineEdit_Streaming_address = QtWidgets.QLineEdit(self.Setup_Audio_Page)
        self.lineEdit_Streaming_address.setMinimumSize(QtCore.QSize(150, 25))
        self.lineEdit_Streaming_address.setFont(self.font_Point_10)
        self.lineEdit_Streaming_address.setStyleSheet(self.lineEdit_Style)
        self.Setup_Audio_Grid_Layout.addWidget(self.lineEdit_Streaming_address, 2, 2, 1, 1)

        

        self.Setup_Audio_Line_2 = QtWidgets.QFrame(self.Setup_Audio_Page)
        self.Setup_Audio_Line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Setup_Audio_Grid_Layout.addWidget(self.Setup_Audio_Line_2, 7, 0, 1, 3)

        self.Setup_Audio_Buttons = QtWidgets.QWidget(self.page_Audio)
        self.Setup_Audio_Buttons.setGeometry(QtCore.QRect(100, 200, 391, 51))

        self.Setup_Audio_Buttons_Layout = QtWidgets.QHBoxLayout(self.Setup_Audio_Buttons)
        self.Setup_Audio_Buttons_Layout.setContentsMargins(0, 0, 0, 0)

        self.btn_Streaming_Play = QtWidgets.QPushButton(self.Setup_Audio_Buttons)
        self.btn_Streaming_Play.setFont(self.font_Point_8)
        self.btn_Streaming_Play.setIcon(self.icon_play)
        self.btn_Streaming_Play.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Streaming_Play.setStyleSheet(self.QBtn_Border_None)
        self.btn_Streaming_Play.setIconSize(QtCore.QSize(45, 45))
        self.btn_Streaming_Play.setCheckable(True)
        self.Setup_Audio_Buttons_Layout.addWidget(self.btn_Streaming_Play)

        self.btn_Streaming_Pause = QtWidgets.QPushButton(self.Setup_Audio_Buttons)
        self.btn_Streaming_Pause.setFont(self.font_Point_8)
        self.btn_Streaming_Pause.setIcon(self.icon_pause)
        self.btn_Streaming_Pause.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Streaming_Pause.setStyleSheet(self.QBtn_Border_None)
        self.btn_Streaming_Pause.setIconSize(QtCore.QSize(45, 45))
        self.btn_Streaming_Pause.setCheckable(True)
        self.Setup_Audio_Buttons_Layout.addWidget(self.btn_Streaming_Pause)

        self.btn_Streaming_Stop = QtWidgets.QPushButton(self.Setup_Audio_Buttons)
        self.btn_Streaming_Stop.setFont(self.font_Point_8)
        self.btn_Streaming_Stop.setIcon(self.icon_stop)
        self.btn_Streaming_Stop.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Streaming_Stop.setStyleSheet(self.QBtn_Border_None)
        self.btn_Streaming_Stop.setIconSize(QtCore.QSize(45, 45))
        self.btn_Streaming_Stop.setCheckable(True)
        self.btn_Streaming_Stop.setChecked(True)
        self.Setup_Audio_Buttons_Layout.addWidget(self.btn_Streaming_Stop)


        self.buttonGroup_AudioPlayer.addButton(self.btn_Streaming_Play)
        self.buttonGroup_AudioPlayer.addButton(self.btn_Streaming_Pause)
        self.buttonGroup_AudioPlayer.addButton(self.btn_Streaming_Stop)
        '''

        self.btn_Streaming_Home = QtWidgets.QPushButton(self.page_Audio)
        self.btn_Streaming_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_Streaming_Home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_Streaming_Home.setIcon(self.icon_home)
        self.btn_Streaming_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_Streaming_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Streaming_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_Streaming_Home.setObjectName("btn_Streaming_Home")

        self.stackedWidget_Setup.addWidget(self.page_Audio)

        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
상태 값 저장
        """
        self.page_SaveSetup = QtWidgets.QWidget()

        self.Setup_Save_Page = QtWidgets.QWidget(self.page_SaveSetup)
        self.Setup_Save_Page.setGeometry(QtCore.QRect(110, 20, 350, 350))

        self.Setup_Save_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Save_Page)
        self.Setup_Save_Grid_Layout.setHorizontalSpacing(20)
        self.Setup_Save_Grid_Layout.setVerticalSpacing(5)

        self.Setup_Save_Lines = [str(i) for i in range(6)]
        for i in range(6):
            self.Setup_Save_Lines[i] = QtWidgets.QFrame(self.Setup_Save_Page)
            self.Setup_Save_Lines[i].setFrameShape(QtWidgets.QFrame.HLine)
            self.Setup_Save_Lines[i].setStyleSheet(self.line_style)

        self.Setup_Save_Grid_Layout.addWidget(
            self.Setup_Save_Lines[0], 1, 0, 1, 3)
        self.Setup_Save_Grid_Layout.addWidget(
            self.Setup_Save_Lines[1], 3, 0, 1, 3)
        self.Setup_Save_Grid_Layout.addWidget(
            self.Setup_Save_Lines[2], 6, 0, 1, 3)
        self.Setup_Save_Grid_Layout.addWidget(
            self.Setup_Save_Lines[3], 8, 0, 1, 3)
        self.Setup_Save_Grid_Layout.addWidget(
            self.Setup_Save_Lines[4], 10, 0, 1, 3)
        self.Setup_Save_Grid_Layout.addWidget(
            self.Setup_Save_Lines[5], 12, 0, 1, 3)

        self.lbl_Setup_Save = [str(i) for i in range(6)]
        for i in range(6):
            self.lbl_Setup_Save[i] = QtWidgets.QLabel(self.Setup_Save_Page)
            if i % 2 == 0:
                self.lbl_Setup_Save[i].setAlignment(
                    QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
                self.lbl_Setup_Save[i].setFont(self.font_Bold_Point_14)
                self.lbl_Setup_Save[i].setStyleSheet(self.lbl_Style)
            else:
                self.lbl_Setup_Save[i].setAlignment(
                    QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
                self.lbl_Setup_Save[i].setFont(self.font_Point_10)
                self.lbl_Setup_Save[i].setStyleSheet(self.lbl_Style)

        self.Setup_Save_Grid_Layout.addWidget(
            self.lbl_Setup_Save[0], 0, 0, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.lbl_Setup_Save[1], 0, 1, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.lbl_Setup_Save[2], 5, 0, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.lbl_Setup_Save[3], 5, 1, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.lbl_Setup_Save[4], 9, 0, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.lbl_Setup_Save[5], 9, 1, 1, 1)

        self.btn_Setup_Save = [str(i) for i in range(5)]
        for i in range(5):
            self.btn_Setup_Save[i] = QtWidgets.QPushButton(
                self.Setup_Save_Page)
            self.btn_Setup_Save[i].setMinimumSize(QtCore.QSize(100, 45))
            self.btn_Setup_Save[i].setFont(self.font_Point_8)
            if i == 0 or i == 2:
                self.btn_Setup_Save[i].setIcon(self.saveIcon)
            elif i == 1 or i == 3:
                self.btn_Setup_Save[i].setIcon(self.icon_Return)
            elif i == 4:
                self.btn_Setup_Save[i].setIcon(self.icon_Plug)
            self.btn_Setup_Save[i].setIconSize(QtCore.QSize(35, 35))
            self.btn_Setup_Save[i].setStyleSheet(self.QBtn_Border_None)

        self.Setup_Save_Grid_Layout.addWidget(
            self.btn_Setup_Save[0], 2, 1, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.btn_Setup_Save[1], 2, 2, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.btn_Setup_Save[2], 7, 1, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.btn_Setup_Save[3], 7, 2, 1, 1)
        self.Setup_Save_Grid_Layout.addWidget(
            self.btn_Setup_Save[4], 11, 1, 1, 1)

        self.btn_Status_Home = QtWidgets.QPushButton(self.page_SaveSetup)
        self.btn_Status_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_Status_Home.setIcon(self.icon_home)
        self.btn_Status_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_Status_Home.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_Status_Home.setIconSize(QtCore.QSize(40, 40))

        self.stackedWidget_Setup.addWidget(self.page_SaveSetup)
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
릴레이 그룹 셋업 1
        """
        self.page_RG1 = QtWidgets.QWidget()
        self.page_RG1.setObjectName("page_RG1")

        self.Setup_Button_Name_1_Page = QtWidgets.QWidget(self.page_RG1)
        self.Setup_Button_Name_1_Page.setGeometry(
            QtCore.QRect(10, 20, 150, 50))

        self.Setup_Button_Name_1_Name_Labels = QtWidgets.QHBoxLayout(
            self.Setup_Button_Name_1_Page)

        self.lbl_Setup_Buttons_1_Name_1 = QtWidgets.QLabel(
            self.Setup_Button_Name_1_Page)
        self.lbl_Setup_Buttons_1_Name_1.setFont(self.font_Bold_Point_14)
        self.lbl_Setup_Buttons_1_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_1_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Button_Name_1_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_1_Name_1)

        self.lbl_Setup_Buttons_1_Name_2 = QtWidgets.QLabel(
            self.Setup_Button_Name_1_Page)
        self.lbl_Setup_Buttons_1_Name_2.setFont(self.font_Point_10)
        self.lbl_Setup_Buttons_1_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_1_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Button_Name_1_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_1_Name_2)

        self.Setup_Button_Name_1 = QtWidgets.QWidget(self.page_RG1)
        self.Setup_Button_Name_1.setGeometry(QtCore.QRect(10, 60, 631, 261))

        self.Setup_Buttons_1_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Button_Name_1)

        for i in range(24):
            if i <= 7:
                self.lbl_Setup_Buttons_NameTag_1[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_1)

                self.lineEdit_Setup_Buttons_Name_1_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_1)

                self.Setup_Buttons_1_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_1[i], 1, i, 1, 1)
                self.Setup_Buttons_1_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_1_[i], 2, i, 1, 1)
            elif i > 7 and i <= 15:
                self.lbl_Setup_Buttons_NameTag_1[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_1)
                self.lineEdit_Setup_Buttons_Name_1_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_1)
                self.Setup_Buttons_1_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_1[i], 4, (i - 8), 1, 1)
                self.Setup_Buttons_1_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_1_[i], 5, (i - 8), 1, 1)
            else:
                self.lbl_Setup_Buttons_NameTag_1[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_1)
                self.lineEdit_Setup_Buttons_Name_1_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_1)
                self.Setup_Buttons_1_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_1[i], 8, (i - 16), 1, 1)
                self.Setup_Buttons_1_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_1_[i], 9, (i - 16), 1, 1)

            self.lbl_Setup_Buttons_NameTag_1[i].setStyleSheet(self.lbl_Style)
            self.lbl_Setup_Buttons_NameTag_1[i].setMinimumSize(
                QtCore.QSize(0, 25))
            self.lbl_Setup_Buttons_NameTag_1[i].setFont(self.font_Point_10)
            self.lbl_Setup_Buttons_NameTag_1[i].setAlignment(
                QtCore.Qt.AlignCenter)
            self.lineEdit_Setup_Buttons_Name_1_[
                i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_Setup_Buttons_Name_1_[
                i].setMinimumSize(QtCore.QSize(0, 25))
            self.lineEdit_Setup_Buttons_Name_1_[i].setFont(self.font_Point_10)

        self.Setup_Buttons_name_Lines_1 = [str(i) for i in range(4)]
        for i in range(4):
            self.Setup_Buttons_name_Lines_1[i] = QtWidgets.QFrame(
                self.Setup_Button_Name_1)
            self.Setup_Buttons_name_Lines_1[i].setFrameShape(
                QtWidgets.QFrame.HLine)
            self.Setup_Buttons_name_Lines_1[i].setStyleSheet(self.line_style)
        self.Setup_Buttons_1_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_1[0], 0, 0, 1, 8)
        self.Setup_Buttons_1_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_1[1], 3, 0, 1, 8)
        self.Setup_Buttons_1_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_1[2], 7, 0, 1, 8)
        self.Setup_Buttons_1_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_1[3], 10, 0, 1, 8)

        self.btn_Name_Save_RG1 = QtWidgets.QPushButton(self.page_RG1)
        self.btn_Name_Save_RG1.setGeometry(QtCore.QRect(530, 350, 61, 51))
        self.btn_Name_Save_RG1.setIcon(self.saveIcon)
        self.btn_Name_Save_RG1.setIconSize(QtCore.QSize(40, 40))
        self.btn_Name_Save_RG1.setStyleSheet(self.QBtn_Border_None)
        self.btn_Name_Save_RG1.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btn_RG1_Home = QtWidgets.QPushButton(self.page_RG1)
        self.btn_RG1_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_RG1_Home.setIcon(self.icon_home)
        self.btn_RG1_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_RG1_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_RG1_Home.setFocusPolicy(QtCore.Qt.NoFocus)

        self.stackedWidget_Setup.addWidget(self.page_RG1)
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
릴레이 그룹 셋팅 2
        """
        self.page_RG2 = QtWidgets.QWidget()

        self.Setup_Button_Name_2_Page = QtWidgets.QWidget(self.page_RG2)
        self.Setup_Button_Name_2_Page.setGeometry(
            QtCore.QRect(10, 20, 150, 50))

        self.Setup_Button_Name_2_Name_Labels = QtWidgets.QHBoxLayout(
            self.Setup_Button_Name_2_Page)

        self.lbl_Setup_Buttons_2_Name_1 = QtWidgets.QLabel(
            self.Setup_Button_Name_2_Page)
        self.lbl_Setup_Buttons_2_Name_1.setFont(self.font_Bold_Point_14)
        self.lbl_Setup_Buttons_2_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_2_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Button_Name_2_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_2_Name_1)

        self.lbl_Setup_Buttons_2_Name_2 = QtWidgets.QLabel(
            self.Setup_Button_Name_2_Page)
        self.lbl_Setup_Buttons_2_Name_2.setFont(self.font_Point_10)
        self.lbl_Setup_Buttons_2_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_2_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Button_Name_2_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_2_Name_2)

        self.Setup_Button_Name_2 = QtWidgets.QWidget(self.page_RG2)
        self.Setup_Button_Name_2.setGeometry(QtCore.QRect(10, 60, 631, 261))

        self.Setup_Buttons_2_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Button_Name_2)

        for i in range(24):
            if i <= 7:
                self.lbl_Setup_Buttons_NameTag_2[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_2)
                self.lineEdit_Setup_Buttons_Name_2_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_2)
                self.Setup_Buttons_2_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_2[i], 1, i, 1, 1)
                self.Setup_Buttons_2_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_2_[i], 2, i, 1, 1)
            elif i > 7 and i <= 15:
                self.lbl_Setup_Buttons_NameTag_2[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_2)
                self.lineEdit_Setup_Buttons_Name_2_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_2)
                self.Setup_Buttons_2_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_2[i], 4, (i - 8), 1, 1)
                self.Setup_Buttons_2_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_2_[i], 5, (i - 8), 1, 1)
            else:
                self.lbl_Setup_Buttons_NameTag_2[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_2)
                self.lineEdit_Setup_Buttons_Name_2_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_2)
                self.Setup_Buttons_2_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_2[i], 8, (i - 16), 1, 1)
                self.Setup_Buttons_2_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_2_[i], 9, (i - 16), 1, 1)

            self.lbl_Setup_Buttons_NameTag_2[i].setStyleSheet(self.lbl_Style)
            self.lbl_Setup_Buttons_NameTag_2[i].setMinimumSize(
                QtCore.QSize(0, 25))
            self.lbl_Setup_Buttons_NameTag_2[i].setFont(self.font_Point_10)
            self.lbl_Setup_Buttons_NameTag_2[i].setAlignment(
                QtCore.Qt.AlignCenter)
            self.lineEdit_Setup_Buttons_Name_2_[
                i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_Setup_Buttons_Name_2_[
                i].setMinimumSize(QtCore.QSize(0, 25))
            self.lineEdit_Setup_Buttons_Name_2_[i].setFont(self.font_Point_10)

        self.Setup_Buttons_name_Lines_2 = [str(i) for i in range(4)]
        for i in range(4):
            self.Setup_Buttons_name_Lines_2[i] = QtWidgets.QFrame(
                self.Setup_Button_Name_2)
            self.Setup_Buttons_name_Lines_2[i].setFrameShape(
                QtWidgets.QFrame.HLine)
            self.Setup_Buttons_name_Lines_2[i].setStyleSheet(self.line_style)
        self.Setup_Buttons_2_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_2[0], 0, 0, 1, 8)
        self.Setup_Buttons_2_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_2[1], 3, 0, 1, 8)
        self.Setup_Buttons_2_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_2[2], 7, 0, 1, 8)
        self.Setup_Buttons_2_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_2[3], 10, 0, 1, 8)

        self.btn_Name_Save_RG2 = QtWidgets.QPushButton(self.page_RG2)
        self.btn_Name_Save_RG2.setGeometry(QtCore.QRect(530, 350, 61, 51))
        self.btn_Name_Save_RG2.setIcon(self.saveIcon)
        self.btn_Name_Save_RG2.setIconSize(QtCore.QSize(40, 40))
        self.btn_Name_Save_RG2.setStyleSheet(self.QBtn_Border_None)
        self.btn_Name_Save_RG2.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btn_RG2_Home = QtWidgets.QPushButton(self.page_RG2)
        self.btn_RG2_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_RG2_Home.setIcon(self.icon_home)
        self.btn_RG2_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_RG2_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_RG2_Home.setFocusPolicy(QtCore.Qt.NoFocus)

        self.stackedWidget_Setup.addWidget(self.page_RG2)

        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
릴레이 버튼 세팅 3
        """

        self.page_RG3 = QtWidgets.QWidget()

        self.Setup_Button_Name_3_Page = QtWidgets.QWidget(self.page_RG3)
        self.Setup_Button_Name_3_Page.setGeometry(
            QtCore.QRect(10, 20, 150, 50))

        self.Setup_Button_Name_3_Name_Labels = QtWidgets.QHBoxLayout(
            self.Setup_Button_Name_3_Page)

        self.lbl_Setup_Buttons_3_Name_1 = QtWidgets.QLabel(
            self.Setup_Button_Name_3_Page)
        self.lbl_Setup_Buttons_3_Name_1.setFont(self.font_Bold_Point_14)
        self.lbl_Setup_Buttons_3_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_3_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Button_Name_3_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_3_Name_1)

        self.lbl_Setup_Buttons_3_Name_2 = QtWidgets.QLabel(
            self.Setup_Button_Name_3_Page)
        self.lbl_Setup_Buttons_3_Name_2.setFont(self.font_Point_10)
        self.lbl_Setup_Buttons_3_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_3_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Button_Name_3_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_3_Name_2)

        self.Setup_Button_Name_3 = QtWidgets.QWidget(self.page_RG3)
        self.Setup_Button_Name_3.setGeometry(QtCore.QRect(10, 60, 631, 261))

        self.Setup_Buttons_3_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Button_Name_3)

        for i in range(24):
            if i <= 7:
                self.lbl_Setup_Buttons_NameTag_3[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_3)
                self.lineEdit_Setup_Buttons_Name_3_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_3)
                self.Setup_Buttons_3_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_3[i], 1, i, 1, 1)
                self.Setup_Buttons_3_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_3_[i], 2, i, 1, 1)
            elif i > 7 and i <= 15:
                self.lbl_Setup_Buttons_NameTag_3[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_3)
                self.lineEdit_Setup_Buttons_Name_3_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_3)
                self.Setup_Buttons_3_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_3[i], 4, (i - 8), 1, 1)
                self.Setup_Buttons_3_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_3_[i], 5, (i - 8), 1, 1)
            else:
                self.lbl_Setup_Buttons_NameTag_3[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_3)
                self.lineEdit_Setup_Buttons_Name_3_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_3)
                self.Setup_Buttons_3_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_3[i], 8, (i - 16), 1, 1)
                self.Setup_Buttons_3_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_3_[i], 9, (i - 16), 1, 1)

            self.lbl_Setup_Buttons_NameTag_3[i].setStyleSheet(self.lbl_Style)
            self.lbl_Setup_Buttons_NameTag_3[i].setMinimumSize(
                QtCore.QSize(0, 25))
            self.lbl_Setup_Buttons_NameTag_3[i].setFont(self.font_Point_10)
            self.lbl_Setup_Buttons_NameTag_3[i].setAlignment(
                QtCore.Qt.AlignCenter)
            self.lineEdit_Setup_Buttons_Name_3_[
                i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_Setup_Buttons_Name_3_[
                i].setMinimumSize(QtCore.QSize(0, 25))
            self.lineEdit_Setup_Buttons_Name_3_[i].setFont(self.font_Point_10)

        self.Setup_Buttons_name_Lines_3 = [str(i) for i in range(4)]
        for i in range(4):
            self.Setup_Buttons_name_Lines_3[i] = QtWidgets.QFrame(
                self.Setup_Button_Name_3)
            self.Setup_Buttons_name_Lines_3[i].setFrameShape(
                QtWidgets.QFrame.HLine)
            self.Setup_Buttons_name_Lines_3[i].setStyleSheet(self.line_style)
        self.Setup_Buttons_3_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_3[0], 0, 0, 1, 8)
        self.Setup_Buttons_3_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_3[1], 3, 0, 1, 8)
        self.Setup_Buttons_3_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_3[2], 7, 0, 1, 8)
        self.Setup_Buttons_3_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_3[3], 10, 0, 1, 8)

        self.btn_RG3_Home = QtWidgets.QPushButton(self.page_RG3)
        self.btn_RG3_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_RG3_Home.setIcon(self.icon_home)
        self.btn_RG3_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_RG3_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_RG3_Home.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btn_Name_Save_RG3 = QtWidgets.QPushButton(self.page_RG3)
        self.btn_Name_Save_RG3.setGeometry(QtCore.QRect(530, 350, 61, 51))
        self.btn_Name_Save_RG3.setIcon(self.saveIcon)
        self.btn_Name_Save_RG3.setIconSize(QtCore.QSize(40, 40))
        self.btn_Name_Save_RG3.setStyleSheet(self.QBtn_Border_None)
        self.btn_Name_Save_RG3.setFocusPolicy(QtCore.Qt.NoFocus)

        self.stackedWidget_Setup.addWidget(self.page_RG3)

        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
릴레이 버튼 세팅 4
        """

        self.page_RG4 = QtWidgets.QWidget()

        self.Setup_Button_Name_4_Page = QtWidgets.QWidget(self.page_RG4)
        self.Setup_Button_Name_4_Page.setGeometry(
            QtCore.QRect(10, 20, 150, 50))

        self.Setup_Button_Name_4_Name_Labels = QtWidgets.QHBoxLayout(
            self.Setup_Button_Name_4_Page)

        self.lbl_Setup_Buttons_4_Name_1 = QtWidgets.QLabel(
            self.Setup_Button_Name_4_Page)
        self.lbl_Setup_Buttons_4_Name_1.setFont(self.font_Bold_Point_14)
        self.lbl_Setup_Buttons_4_Name_1.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_4_Name_1.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.Setup_Button_Name_4_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_4_Name_1)

        self.lbl_Setup_Buttons_4_Name_2 = QtWidgets.QLabel(
            self.Setup_Button_Name_4_Page)
        self.lbl_Setup_Buttons_4_Name_2.setFont(self.font_Point_10)
        self.lbl_Setup_Buttons_4_Name_2.setStyleSheet(self.lbl_Style)
        self.lbl_Setup_Buttons_4_Name_2.setAlignment(
            QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.Setup_Button_Name_4_Name_Labels.addWidget(
            self.lbl_Setup_Buttons_4_Name_2)

        self.Setup_Button_Name_4 = QtWidgets.QWidget(self.page_RG4)
        self.Setup_Button_Name_4.setGeometry(QtCore.QRect(10, 60, 631, 261))

        self.Setup_Buttons_4_Grid_Layout = QtWidgets.QGridLayout(
            self.Setup_Button_Name_4)
        self.Setup_Buttons_4_Grid_Layout.setObjectName(
            "Setup_Buttons_4_Grid_Layout")

        for i in range(24):
            if i <= 7:
                self.lbl_Setup_Buttons_NameTag_4[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_4)
                self.lineEdit_Setup_Buttons_Name_4_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_4)
                self.Setup_Buttons_4_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_4[i], 1, i, 1, 1)
                self.Setup_Buttons_4_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_4_[i], 2, i, 1, 1)
            elif i > 7 and i <= 15:
                self.lbl_Setup_Buttons_NameTag_4[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_4)
                self.lineEdit_Setup_Buttons_Name_4_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_4)
                self.Setup_Buttons_4_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_4[i], 4, (i - 8), 1, 1)
                self.Setup_Buttons_4_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_4_[i], 5, (i - 8), 1, 1)
            else:
                self.lbl_Setup_Buttons_NameTag_4[i] = QtWidgets.QLabel(
                    self.Setup_Button_Name_4)
                self.lineEdit_Setup_Buttons_Name_4_[
                    i] = QtWidgets.QLineEdit(self.Setup_Button_Name_4)
                self.Setup_Buttons_4_Grid_Layout.addWidget(
                    self.lbl_Setup_Buttons_NameTag_4[i], 8, (i - 16), 1, 1)
                self.Setup_Buttons_4_Grid_Layout.addWidget(
                    self.lineEdit_Setup_Buttons_Name_4_[i], 9, (i - 16), 1, 1)

            self.lbl_Setup_Buttons_NameTag_4[i].setStyleSheet(self.lbl_Style)
            self.lbl_Setup_Buttons_NameTag_4[i].setMinimumSize(
                QtCore.QSize(0, 25))
            self.lbl_Setup_Buttons_NameTag_4[i].setFont(self.font_Point_10)
            self.lbl_Setup_Buttons_NameTag_4[i].setAlignment(
                QtCore.Qt.AlignCenter)
            self.lineEdit_Setup_Buttons_Name_4_[
                i].setStyleSheet(self.lineEdit_Style)
            self.lineEdit_Setup_Buttons_Name_4_[
                i].setMinimumSize(QtCore.QSize(0, 25))
            self.lineEdit_Setup_Buttons_Name_4_[i].setFont(self.font_Point_10)

        self.Setup_Buttons_name_Lines_4 = [str(i) for i in range(4)]
        for i in range(4):
            self.Setup_Buttons_name_Lines_4[i] = QtWidgets.QFrame(
                self.Setup_Button_Name_3)
            self.Setup_Buttons_name_Lines_4[i].setFrameShape(
                QtWidgets.QFrame.HLine)
            self.Setup_Buttons_name_Lines_4[i].setStyleSheet(self.line_style)
        self.Setup_Buttons_4_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_4[0], 0, 0, 1, 8)
        self.Setup_Buttons_4_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_4[1], 3, 0, 1, 8)
        self.Setup_Buttons_4_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_4[2], 7, 0, 1, 8)
        self.Setup_Buttons_4_Grid_Layout.addWidget(
            self.Setup_Buttons_name_Lines_4[3], 10, 0, 1, 8)

        self.btn_Name_Save_RG4 = QtWidgets.QPushButton(self.page_RG4)
        self.btn_Name_Save_RG4.setGeometry(QtCore.QRect(530, 350, 61, 51))
        self.btn_Name_Save_RG4.setIcon(self.saveIcon)
        self.btn_Name_Save_RG4.setIconSize(QtCore.QSize(40, 40))
        self.btn_Name_Save_RG4.setStyleSheet(self.QBtn_Border_None)
        self.btn_Name_Save_RG4.setFocusPolicy(QtCore.Qt.NoFocus)

        self.btn_RG4_Home = QtWidgets.QPushButton(self.page_RG4)
        self.btn_RG4_Home.setGeometry(QtCore.QRect(590, 350, 61, 51))
        self.btn_RG4_Home.setText("")
        self.btn_RG4_Home.setIcon(self.icon_home)
        self.btn_RG4_Home.setIconSize(QtCore.QSize(40, 40))
        self.btn_RG4_Home.setStyleSheet(self.QBtn_Border_None)
        self.btn_RG4_Home.setFocusPolicy(QtCore.Qt.NoFocus)

        self.stackedWidget_Setup.addWidget(self.page_RG4)

        self.Main_View.addWidget(self.page_Setup)
        MainWindow.setCentralWidget(self.centralwidget)

# Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setFont(self.font_Point_10)
        self.statusbar.setStyleSheet(
            "QStatusBar { min-height: 25;  color:white; background-color:#6E6E6E}")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Main_View.setCurrentIndex(0)
        self.stackedWidget_Setup.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
# Slot
        self.buttonGroup_MainMenu.buttonClicked.connect(
            MainWindow.main_Page_Change)
        self.buttonGroup_Setup.buttonClicked[int].connect(
            MainWindow.setup_Page_Change)
        self.buttonGroup_RG1.buttonClicked[int].connect(
            MainWindow.btn_Clicked_RG_1)
        self.buttonGroup_RG2.buttonClicked[int].connect(
            MainWindow.btn_Clicked_RG_2)
        self.buttonGroup_RG3.buttonClicked[int].connect(
            MainWindow.btn_Clicked_RG_3)
        self.buttonGroup_RG4.buttonClicked[int].connect(
            MainWindow.btn_Clicked_RG_4)
        self.audioButtonGroup.buttonClicked[int].connect(
            MainWindow.audioPlayButton_Clicked)
        self.btn_IP_Save.clicked.connect(MainWindow.serverIpAddressSave)
        self.btn_Setup_Home.clicked.connect(MainWindow.setHome)
        self.btn_Serial_Home.clicked.connect(MainWindow.setHome)
        self.btn_Streaming_Home.clicked.connect(MainWindow.setHome)
        self.btn_Status_Home.clicked.connect(MainWindow.setHome)
        self.btn_RG1_Home.clicked.connect(MainWindow.setHome)
        self.btn_RG2_Home.clicked.connect(MainWindow.setHome)
        self.btn_RG3_Home.clicked.connect(MainWindow.setHome)
        self.btn_RG4_Home.clicked.connect(MainWindow.setHome)
        self.btn_Serial_Save.clicked.connect(MainWindow.serialModeSaveToFile)
        self.Main_Menu_Indcators[2].clicked.connect(
            MainWindow.ind_Network_Check)
        self.btn_Name_Save_RG1.clicked.connect(MainWindow.RG_All_Name_Save)
        self.btn_Name_Save_RG2.clicked.connect(MainWindow.RG_All_Name_Save)
        self.btn_Name_Save_RG3.clicked.connect(MainWindow.RG_All_Name_Save)
        self.btn_Name_Save_RG4.clicked.connect(MainWindow.RG_All_Name_Save)
        self.btn_Setup_Save[0].clicked.connect(MainWindow.buttonStateSave)
        self.btn_Setup_Save[1].clicked.connect(MainWindow.buttonStateLoad)
        self.btn_Setup_Save[2].clicked.connect(MainWindow.RG_All_Name_Save)
        self.btn_Setup_Save[3].clicked.connect(MainWindow.RG_All_Name_Load)
        self.btn_Setup_Save[4].clicked.connect(MainWindow.systemReboot)
        # self.btn_Streaming_Play.clicked.connect(MainWindow.streaming_Play)
        # self.btn_Streaming_Pause.clicked.connect(MainWindow.streaming_Pause)
        # self.btn_Streaming_Stop.clicked.connect(MainWindow.streaming_Stop)
        self.comboBox_Serial_Mode.currentIndexChanged.connect(
            MainWindow.serialModeChange)
        self.btn_BssReboot.clicked.connect(MainWindow.bssReoot_function)
        self.setFunctionButton1.clicked.connect(MainWindow.bssLocalMic_Btn)
        self.setFunctionButton2.clicked.connect(MainWindow.bssFuction_Btn)

        self.lineEdit_IP[0].selectionChanged.connect(MainWindow.touchInput_IP)
        self.lineEdit_IP[1].selectionChanged.connect(MainWindow.touchInput_IP)
        self.lineEdit_IP[2].selectionChanged.connect(MainWindow.touchInput_IP)
        self.lineEdit_IP[3].selectionChanged.connect(MainWindow.touchInput_IP)
        self.lineEdit_NM[0].selectionChanged.connect(MainWindow.touchInput_NM)
        self.lineEdit_NM[1].selectionChanged.connect(MainWindow.touchInput_NM)
        self.lineEdit_NM[2].selectionChanged.connect(MainWindow.touchInput_NM)
        self.lineEdit_NM[3].selectionChanged.connect(MainWindow.touchInput_NM)
        self.lineEdit_GW[0].selectionChanged.connect(MainWindow.touchInput_GW)
        self.lineEdit_GW[1].selectionChanged.connect(MainWindow.touchInput_GW)
        self.lineEdit_GW[2].selectionChanged.connect(MainWindow.touchInput_GW)
        self.lineEdit_GW[3].selectionChanged.connect(MainWindow.touchInput_GW)
        self.lineEdit_Client[0].selectionChanged.connect(
            MainWindow.touchInput_CLIENT)
        self.lineEdit_Client[1].selectionChanged.connect(
            MainWindow.touchInput_CLIENT)
        self.lineEdit_Client[2].selectionChanged.connect(
            MainWindow.touchInput_CLIENT)
        self.lineEdit_Client[3].selectionChanged.connect(
            MainWindow.touchInput_CLIENT)

        self.lineEdit_Server_Port.selectionChanged.connect(
            MainWindow.touchInput_ServerPort)
        self.lineEdit_Client_Port.selectionChanged.connect(
            MainWindow.touchInput_ClientPort)
        self.lineEdit_Client_ID.selectionChanged.connect(
            MainWindow.touchInput_LocalID)

        """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
# 라벨

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Paging Controller"))
        self.Main_Menu_Buttons[0].setText(
            _translate("MainWindow", "Relay\nGroup 1"))
        self.Main_Menu_Buttons[1].setText(
            _translate("MainWindow", "Relay\nGroup 2"))
        self.Main_Menu_Buttons[2].setText(
            _translate("MainWindow", "Relay\nGroup 3"))
        self.Main_Menu_Buttons[3].setText(
            _translate("MainWindow", "Relay\nGroup 4"))
        self.lbl_Rg1_Name_1.setText(_translate("MainWindow", "방송 구간 선택"))
        self.lbl_Rg1_Name_2.setText(_translate("MainWindow", ">> 방송 지역 1"))
        self.lbl_Rg2_Name_1.setText(_translate("MainWindow", "방송 구간 선택"))
        self.lbl_Rg2_Name_2.setText(_translate("MainWindow", ">> 방송 지역 2"))
        self.lbl_Rg3_Name_1.setText(_translate("MainWindow", "방송 구간 선택"))
        self.lbl_Rg3_Name_2.setText(_translate("MainWindow", ">> 방송 지역 3"))
        self.lbl_RG4_Name_1.setText(_translate("MainWindow", "방송 구간 선택"))
        self.lbl_RG4_Name_2.setText(_translate("MainWindow", ">> 방송 지역 4"))

        self.Setup_Buttons[0].setText(_translate("MainWindow", " 기능버튼"))
        self.Setup_Buttons[1].setText(_translate("MainWindow", " IP 설정"))
        self.Setup_Buttons[2].setText(_translate("MainWindow", " 시리얼 통신"))
        self.Setup_Buttons[3].setText(_translate("MainWindow", " 오디오\n 플레이어"))
        self.Setup_Buttons[4].setText(_translate("MainWindow", " 설정 저장"))
        self.Setup_Buttons[5].setText(_translate("MainWindow", " 그룹 1"))
        self.Setup_Buttons[6].setText(_translate("MainWindow", " 그룹 2"))
        self.Setup_Buttons[7].setText(_translate("MainWindow", " 그룹 3"))
        self.Setup_Buttons[8].setText(_translate("MainWindow", " 그룹 4"))

        self.setFunctionButton1.setText(_translate("MainWindow", "지점 마이크"))
        self.setFunctionButton2.setText(_translate("MainWindow", "CDP 송출"))

        self.lbl_Setup_IP[0].setText(_translate("MainWindow", "IP ADDRESS"))
        self.lbl_Setup_IP[1].setText(_translate("MainWindow", "NET MASK"))
        self.lbl_Setup_IP[2].setText(_translate("MainWindow", "GATE WAY"))
        self.lbl_Setup_IP[3].setText(_translate("MainWindow", "PORT"))
        self.lbl_Setup_IP[4].setText(_translate("MainWindow", "IP ADDRESS"))
        self.lbl_Setup_IP[5].setText(_translate("MainWindow", "PORT"))
        self.lbl_Setup_IP[6].setText(_translate("MainWindow", "지점 ID"))
        self.lbl_Setup_IP_Menu[0].setText(_translate("MainWindow", "IP 설정"))
        self.lbl_Setup_IP_Menu[1].setText(
            _translate("MainWindow", ">> 시스템 IP 설정"))
        self.lbl_Setup_IP_Menu[2].setText(_translate("MainWindow", "IP 설정"))
        self.lbl_Setup_IP_Menu[3].setText(_translate("MainWindow", ">> 서버 설정"))
        self.lbl_Setup_IP_Menu[4].setText(_translate("MainWindow", "IP 설정"))
        self.lbl_Setup_IP_Menu[5].setText(
            _translate("MainWindow", ">> 클라이언트 설정"))

        self.lbl_Setup_Serial_Menu_1.setText(
            _translate("MainWindow", "시리얼 통신"))
        self.lbl_Setup_Serial_Menu_2.setText(
            _translate("MainWindow", ">> 시리얼 통신 설정"))
        self.lbl_Setup_Serial_Menu_3.setText(
            _translate("MainWindow", "시리얼 통신"))
        self.lbl_Setup_Serial_Menu_4.setText(
            _translate("MainWindow", ">> BSS 재부팅 설정"))
        self.lbl_Setup_Serial_1.setText(_translate("MainWindow", "통신 모드"))
        self.lbl_Setup_Serial_2.setText(_translate("MainWindow", "BSS 주소"))
        self.lbl_Setup_Serial_3.setText(_translate("MainWindow", "리부팅"))

        self.lbl_Setup_Audio_Menu_1.setText(
            _translate("MainWindow", "오디오          "))
        self.lbl_Setup_Audio_Menu_2.setText(
            _translate("MainWindow", ">> 오디오 플레이어"))
        self.audioPlayButton[8].setText(_translate("MainWindow", "정지"))
        '''
        self.lbl_Setup_Audio_1.setText(_translate("MainWindow", "스트리밍 주소"))
        self.btn_Streaming_Play.setText(_translate("MainWindow", "스트리밍\n시작"))
        self.btn_Streaming_Pause.setText(_translate("MainWindow", "일시정지"))
        self.btn_Streaming_Stop.setText(_translate("MainWindow", "정지"))
        '''
        self.lbl_Setup_Save[0].setText(_translate("MainWindow", "설정 저장"))
        self.lbl_Setup_Save[1].setText(_translate("MainWindow", ">> 버튼 상태값"))
        self.lbl_Setup_Save[2].setText(_translate("MainWindow", "설정 저장"))
        self.lbl_Setup_Save[3].setText(_translate("MainWindow", ">> 버튼 이름"))
        self.lbl_Setup_Save[4].setText(_translate("MainWindow", "설정 저장"))
        self.lbl_Setup_Save[5].setText(_translate("MainWindow", ">> 시스템 리부팅"))
        self.btn_Setup_Save[0].setText(_translate("MainWindow", "저장하기"))
        self.btn_Setup_Save[1].setText(_translate("MainWindow", "불러오기"))
        self.btn_Setup_Save[2].setText(_translate("MainWindow", "저장하기"))
        self.btn_Setup_Save[3].setText(_translate("MainWindow", "불러오기"))
        self.btn_Setup_Save[4].setText(_translate("MainWindow", "리부팅"))
        self.lbl_Setup_Buttons_1_Name_1.setText(
            _translate("MainWindow", "그룹1"))
        self.lbl_Setup_Buttons_1_Name_2.setText(
            _translate("MainWindow", ">> 버튼 이름"))
        for i in range(24):
            self.lbl_Setup_Buttons_NameTag_1[i].setText(
                _translate("MainWindow", "CH {}".format(i + 1)))
        self.lbl_Setup_Buttons_2_Name_1.setText(
            _translate("MainWindow", "그룹2"))
        self.lbl_Setup_Buttons_2_Name_2.setText(
            _translate("MainWindow", ">> 버튼 이름"))
        for i in range(24):
            self.lbl_Setup_Buttons_NameTag_2[i].setText(
                _translate("MainWindow", "CH {}".format(i + 1)))
        self.lbl_Setup_Buttons_3_Name_1.setText(
            _translate("MainWindow", "그룹3"))
        self.lbl_Setup_Buttons_3_Name_2.setText(
            _translate("MainWindow", ">> 버튼 이름"))
        for i in range(24):
            self.lbl_Setup_Buttons_NameTag_3[i].setText(
                _translate("MainWindow", "CH {}".format(i + 1)))
        self.lbl_Setup_Buttons_4_Name_1.setText(
            _translate("MainWindow", "그룹4"))
        self.lbl_Setup_Buttons_4_Name_2.setText(
            _translate("MainWindow", ">> 버튼 이름"))
        for i in range(24):
            self.lbl_Setup_Buttons_NameTag_4[i].setText(
                _translate("MainWindow", "CH {}".format(i + 1)))


# 메인 함수
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
