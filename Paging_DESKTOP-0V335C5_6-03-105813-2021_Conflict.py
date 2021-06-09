# -*- coding: utf-8 -*-

import sys
import os
import socket
import platform
import serial
import subprocess
import vlc
import binascii
import re
import threading
from _thread import *
import RPi.GPIO as GPIO
from time import sleep
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QStatusBar
from PySide2.QtCore import Qt, Slot, Signal, QThread
from PagingControl_UI import Ui_MainWindow
from PopupDialog import Ui_DialogQuestion, Ui_DialogInfo, Ui_DialogEM, Ui_DialogKeypad_ip, Ui_DialogKeypad_Port
from Sovico_DRG116 import sovico_DRG116
from Blue_Relay import blueRg
from Hiqnet_Check import hiqnet_checksum

# Bagic veriable
osPlatform = None
tcpServerPort = 8888
serialBaud = 115200
em_Set_State = None
clientServerIP = None
clientServerPort = None
LocalID = None
bssLevelPresence = ['0']*48
udpLogDest = ('192.168.1.105', 9999)


class Main_UI(QMainWindow, Ui_MainWindow):
    tcpServerReturnString = Signal(str)
    tcpServerReset = Signal()
    serialReturnString = Signal(str)
    setSerialBaudChange = Signal(str)
    player_play = Signal(int)
    player_pause = Signal()
    player_stop = Signal()
    bssHiqnetString = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        global clientServerIP, clientServerPort, LocalID, logServerIp, udpLogDest

        self.tcpServerNetworkStatus = False
        self.ind_Streaming_State = False
        self.tcpServerAddress = [
            '0', '192.168.1.199', '255.255.255.0', '0.0.0.0', '8888', '127.0.0.1', '12302', '1']
        self.ip = ['0']*4
        self.nm = ['0']*4
        self.gw = ['0']*4
        self.clientIp = ['0']*4
        self.btn_State_FileName = [
            'ButtonState_RG1.txt', 'ButtonState_RG2.txt', 'ButtonState_RG3.txt', 'ButtonState_RG4.txt']
        self.btn_Name_FileName = [
            'ButtonName_RG1.txt', 'ButtonName_RG2.txt', 'ButtonName_RG3.txt', 'ButtonName_RG4.txt']
        self.btn_Name = [self.lineEdit_Setup_Buttons_Name_1_, self.lineEdit_Setup_Buttons_Name_2_,
                         self.lineEdit_Setup_Buttons_Name_3_, self.lineEdit_Setup_Buttons_Name_4_]
        self.btn_Ui = [self.btn_RG1_, self.btn_RG2_,
                       self.btn_RG3_, self.btn_RG4_]

        self.em_Popup = False
        self.serialMode = 0
        self.ipTouchInpusStatus = 0

        self.change_IP_Address(False)

        tcpServerPort = int(self.tcpServerAddress[4])
        clientServerIP = self.tcpServerAddress[5]
        clientServerPort = self.tcpServerAddress[6]
        LocalID = self.tcpServerAddress[7]

        # thread 변수 선언
        self.TcpSoketServer = TCPServer_Socket()
        self.serial_BssMeterRT = serial_BssMeterRT()
        self.audioStreamReceiver = audioStreamReceiver()
        self.udpSendBssMeter = udpSendBssMeter()
        self.em_Alarm = EM_Alarm()

        # thread 변수 연결
        self.TcpSoketServer.TCPServerReceiveString.connect(
            self.server_data_parcing)
        self.TcpSoketServer.TCPServerConnectClient.connect(
            self.serverConnectClient)
        self.TcpSoketServer.TCPServerComm.connect(self.Communicate_State_Start)
        self.tcpServerReturnString.connect(self.TcpSoketServer.stringReturn)
        self.player_play.connect(self.audioStreamReceiver.play)
        self.player_stop.connect(self.audioStreamReceiver.stop)
        self.audioStreamReceiver.player_State.connect(self.player_State_Return)
        self.audioStreamReceiver.play_on.connect(self.streaming_Play_On)
        self.em_Alarm.em_Set.connect(self.em_Alarm_Set)
        self.bssHiqnetString.connect(self.serial_BssMeterRT.bssReboot)
        self.udpSendBssMeter.udpMeterRT.connect(self.bssMeterReturn)

        # Popup Setup
        self.qdialog = QDialog()
        self.qdialog.Qui = Ui_DialogQuestion()
        self.qdialog.Qui.setupUi(self.qdialog)
        self.idialog = QDialog()
        self.idialog.Qui = Ui_DialogInfo()
        self.idialog.Qui.setupUi(self.idialog)
        self.emdialog = QDialog()
        self.emdialog.Qui = Ui_DialogEM()
        self.emdialog.Qui.setupUi(self.emdialog)
        self.touch4bayDialog = QDialog()
        self.touch4bayDialog.Qui = Ui_DialogKeypad_ip()
        self.touch4bayDialog.Qui.setupUi(self.touch4bayDialog)
        self.touch1bayDialog = QDialog()
        self.touch1bayDialog.Qui = Ui_DialogKeypad_Port()
        self.touch1bayDialog.Qui.setupUi(self.touch1bayDialog)
        self.touch4bay_text_ip = [self.touch4bayDialog.Qui.text_Ip1, self.touch4bayDialog.Qui.text_Ip2,
                                  self.touch4bayDialog.Qui.text_Ip3, self.touch4bayDialog.Qui.text_Ip4]

        self.setSerialfrom_()  # Serial Port Setup
        self.buttonNameLoad_()  # Button Name

        self.TcpSoketServer.start()
        print('TCP Server Loading Completed')
        self.serial_BssMeterRT.start()
        self.udpSendBssMeter.start()
        self.audioStreamReceiver.start()
        print('Audio Stream Receiver Ready')
        self.em_Alarm.start()

        # serial Port
        try:
            if self.serialMode == 0:
                self.serNum2 = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)
            elif self.serialMode == 1:
                self.serNum2 = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
        except:
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- USB Serial 디바이스 없습니다.'))

        start_new_thread(self.udpLogReturn,
                         (LocalID, 'Paging Control -- 시스템이 시작되었습니다.'))
        # UI Start
        self.show()
        # Button State Reload
        sleep(1)
        self.buttonStateFileLoad()

    # Log Sender
    def udpLogReturn(self, localId, RtString):
        try:
            self.udpLogRt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udpLogRt.sendto('{},{}'.format(
                localId, RtString).encode('utf8'), udpLogDest)
            self.udpLogRt.close()
            start_new_thread(self.Communicate_State, (True,))
        except:
            self.statusBar().showMessage('네트워크가 활성화 되지 않았습니다.', 5000)

    # EM Alarm
    @Slot(bool, int)
    def em_Alarm_Set(self, state, pinNum):
        if state == 1:
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- 비상이 발생하였습니다.PIN {}'.format(pinNum)))
            # dialog
            if self.em_Popup == False:
                try:
                    start_new_thread(self.udpReturnThread,
                                     ('e,{},1,!'.format(LocalID), ))
                except:
                    self.statusBar().showMessage('네트워크가 활성화 되지 않았습니다.', 5000)

                self.em_Popup = True
                # EM Popup
                self.emdialog.Qui.Title_message.setText("  EM")
                self.emdialog.Qui.Main_Message.setText("비상이 발생하였습니다.")
                if self.emdialog.exec_():
                    self.em_Popup = False
                    start_new_thread(
                        self.udpLogReturn, (LocalID, 'Paging Control -- 지점에서 비상 상황을 확인 하였습니다.'))
        elif state == 0:
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- 비상이 해제되었습니다.PIN {}'.format(pinNum)))
            start_new_thread(self.udpReturnThread,
                             ('e,{},0,!'.format(LocalID), ))
        elif state == 2:
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- 비상 감지 시스템에 장애가 발생 하였습니다.'))
        elif state == 3:
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- 비상 감지 시스템을 시작 하였습니다.'))
    # Touch Input

    @Slot()
    def touchInput_IP(self):

        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch4bayDialog.Qui.Title_message.setText("    IP 설정")
            for i, items in enumerate(self.touch4bay_text_ip):
                items.setText(self.lineEdit_IP[i].text())
            if self.touch4bayDialog.exec_():
                for i, items in enumerate(self.touch4bay_text_ip):
                    self.lineEdit_IP[i].setText(items.text())
                self.ipTouchInpusStatus = 0
            else:
                for item in self.lineEdit_IP:
                    item.deselect()
                self.ipTouchInpusStatus = 0

    @Slot()
    def touchInput_NM(self):
        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch4bayDialog.Qui.Title_message.setText("    NETMASK 설정")
            for i, items in enumerate(self.touch4bay_text_ip):
                items.setText(self.lineEdit_NM[i].text())
            if self.touch4bayDialog.exec_():
                for i, items in enumerate(self.touch4bay_text_ip):
                    self.lineEdit_NM[i].setText(items.text())
                self.ipTouchInpusStatus = 0
            else:
                for item in self.lineEdit_NM:
                    item.deselect()
                self.ipTouchInpusStatus = 0

    @Slot()
    def touchInput_GW(self):
        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch4bayDialog.Qui.Title_message.setText("    GATEWAY 설정")
            for i, items in enumerate(self.touch4bay_text_ip):
                items.setText(self.lineEdit_GW[i].text())
            if self.touch4bayDialog.exec_():
                for i, items in enumerate(self.touch4bay_text_ip):
                    self.lineEdit_GW[i].setText(items.text())
                self.ipTouchInpusStatus = 0
            else:
                for item in self.lineEdit_GW:
                    item.deselect()
                self.ipTouchInpusStatus = 0

    @Slot()
    def touchInput_CLIENT(self):
        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch4bayDialog.Qui.Title_message.setText("    AMX 서버 주소 설정")
            for i, items in enumerate(self.touch4bay_text_ip):
                items.setText(self.lineEdit_Client[i].text())
            if self.touch4bayDialog.exec_():
                for i, items in enumerate(self.touch4bay_text_ip):
                    self.lineEdit_Client[i].setText(items.text())
                self.ipTouchInpusStatus = 0
            else:
                for item in self.lineEdit_Client:
                    item.deselect()
                self.ipTouchInpusStatus = 0

    @Slot()
    def touchInput_ServerPort(self):
        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch1bayDialog.Qui.Title_message.setText("    통신 포트 설정")
            self.touch1bayDialog.Qui.text_Port.setText(
                self.lineEdit_Server_Port.text())
            if self.touch1bayDialog.exec_():
                self.lineEdit_Server_Port.setText(
                    self.touch1bayDialog.Qui.text_Port.text())
                self.ipTouchInpusStatus = 0
            else:
                self.lineEdit_Server_Port.deselect()
                self.ipTouchInpusStatus = 0

    @Slot()
    def touchInput_ClientPort(self):
        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch1bayDialog.Qui.Title_message.setText("    AMX 포트 설정")
            self.touch1bayDialog.Qui.text_Port.setText(
                self.lineEdit_Client_Port.text())
            if self.touch1bayDialog.exec_():
                self.lineEdit_Client_Port.setText(
                    self.touch1bayDialog.Qui.text_Port.text())
                self.ipTouchInpusStatus = 0
            else:
                self.lineEdit_Client_Port.deselect()
                self.ipTouchInpusStatus = 0

    @Slot()
    def touchInput_LocalID(self):
        if self.ipTouchInpusStatus == 0:
            self.ipTouchInpusStatus = 1
            self.touch1bayDialog.Qui.Title_message.setText("    LOCAL ID 설정")
            self.touch1bayDialog.Qui.text_Port.setText(
                self.lineEdit_Client_ID.text())
            if self.touch1bayDialog.exec_():
                self.lineEdit_Client_ID.setText(
                    self.touch1bayDialog.Qui.text_Port.text())
                self.ipTouchInpusStatus = 0
            else:
                self.lineEdit_Client_ID.deselect()
                self.ipTouchInpusStatus = 0

    # Bss Reboot
    @Slot()
    def bssReoot_function(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  BSS BLU 재부팅")
        self.qdialog.Qui.Main_Message.setText("BSS BLU DSP를 재부팅 하시겠습니까?")
        # OK
        if self.qdialog.exec_():
            self.hiqnetNodeAddr = [0]*6
            self.rebootHqinetNodeAddr = self.lineEdit_Bss_Reboot_Code.text()
            self.hiqnetNodeAddr[0] = self.rebootHqinetNodeAddr[:2]
            self.hiqnetNodeAddr[1] = self.rebootHqinetNodeAddr[2:4]
            self.hiqnetNodeAddr[2] = self.rebootHqinetNodeAddr[4:6]
            self.hiqnetNodeAddr[3] = self.rebootHqinetNodeAddr[6:8]
            self.hiqnetNodeAddr[4] = self.rebootHqinetNodeAddr[8:10]
            self.hiqnetNodeAddr[5] = self.rebootHqinetNodeAddr[10:12]

            try:
                self.bssSetString = hiqnet_checksum(
                    '88', self.hiqnetNodeAddr, 1, 1)
                self.bssHiqnetString.emit(self.bssSetString)
                self.statusBar().showMessage('BSS BLU DSP가 재부팅 됩니다. 최대 5분정도 소요됩니다.', 5000)
                self.udpLogReturn(
                    LocalID, 'Paging Control -- BSS DSP가 Paging Control에 의해서 재부팅 되었습니다.')
            except:
                self.udpLogReturn(
                    LocalID, 'Paging Control -- BSS장비와의 통신에 문제가 발생했습니다.')
                self.statusBar().showMessage('BSS장비와의 통신에 문제가 발생했습니다.', 5000)

    @Slot()
    def bssLocalMic_Btn(self):
        self.hiqnet_localid = str(LocalID).zfill(2)

        if self.setFunctionButton1.isChecked():
            # type,nodeAddr,nodeId,parameterValue
            self.hiqnetNodeAddr = [
                '20', self.hiqnet_localid, '03', '00', '07', '01']
            self.bssSetString = hiqnet_checksum(
                '88', self.hiqnetNodeAddr, 33, 0)
        else:
            self.hiqnetNodeAddr = [
                '20', self.hiqnet_localid, '03', '00', '07', '01']
            self.bssSetString = hiqnet_checksum(
                '88', self.hiqnetNodeAddr, 33, 1)

        try:
            self.bssHiqnetString.emit(self.bssSetString)
            if self.setFunctionButton1.isChecked():
                self.udpLogReturn(
                    LocalID, 'Paging Control -- 지점 마이크 사용이 시작 되었습니다.')
                self.statusBar().showMessage('지점 마이크 사용이 시작 되었습니다.', 5000)
            else:
                self.udpLogReturn(
                    LocalID, 'Paging Control -- 지점 마이크 사용이 종료 되었습니다.')
                self.statusBar().showMessage('지점 마이크 사용이 종료 되었습니다.', 5000)
        except:
            self.udpLogReturn(
                LocalID, 'Paging Control -- BSS장비와의 통신에 문제가 발생했습니다.')
            self.statusBar().showMessage('BSS장비와의 통신에 문제가 발생했습니다.', 5000)

    @Slot()
    def bssFuction_Btn(self):
        self.hiqnet_localid = str(LocalID).zfill(2)

        if self.setFunctionButton2.isChecked():
            # type,nodeAddr,nodeId,parameterValue
            self.hiqnetNodeAddr = [
                '20', self.hiqnet_localid, '03', '00', '07', '01']
            self.bssSetString = hiqnet_checksum(
                '88', self.hiqnetNodeAddr, 35, 0)
        else:
            self.hiqnetNodeAddr = [
                '20', self.hiqnet_localid, '03', '00', '07', '01']
            self.bssSetString = hiqnet_checksum(
                '88', self.hiqnetNodeAddr, 35, 1)

        try:
            self.bssHiqnetString.emit(self.bssSetString)
            if self.setFunctionButton1.isChecked():
                self.udpLogReturn(
                    LocalID, 'Paging Control -- 지점 이벤트 기능이 활성화 되었습니다.')
                self.statusBar().showMessage('지점 이벤트 기능이 활성화 되었습니다.', 5000)
            else:
                self.udpLogReturn(
                    LocalID, 'Paging Control -- 지점 이벤트 기능이 종료 되었습니다.')
                self.statusBar().showMessage('지점 이벤트 기능이 종료 되었습니다.', 5000)
        except:
            self.udpLogReturn(
                LocalID, 'Paging Control -- BSS장비와의 통신에 문제가 발생했습니다.')
            self.statusBar().showMessage('BSS장비와의 통신에 문제가 발생했습니다.', 5000)

    @Slot()
    def player_State_Return(self, rtData):
        self.statusBar().showMessage(rtData, 5000)
        start_new_thread(self.udpLogReturn, (LocalID, rtData))

    @Slot(bool)
    def streaming_Play_On(self, state):
        if state == True:
            self.Main_Menu_Indcators[0].setChecked(True)
            self.ind_Streaming_State = True
        else:
            self.Main_Menu_Indcators[0].setChecked(False)
            self.ind_Streaming_State = False

    # Button Name Save
    @Slot()
    def RG_All_Name_Save(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  버튼 이름 저장")
        self.qdialog.Qui.Main_Message.setText("버튼의 이름을 저장 하시겠습니까?")
        # OK
        if self.qdialog.exec_():
            self.buttonNameSave_()
        else:
            self.buttonNameLoad_()

    def buttonNameSave_(self):
        for group in range(4):
            with open(self.btn_Name_FileName[group], 'w') as file:
                for i in range(24):
                    file.write(self.btn_Name[group][i].text() + '\n')
                    self.btn_Ui[group][i].setText(
                        self.btn_Name[group][i].text())
        self.statusBar().showMessage('버튼 이름을 저장 하였습니다.', 5000)
        start_new_thread(self.udpLogReturn,
                         (LocalID, 'Paging Control -- 릴레이 버튼 이름이 변경되었습니다.'))

    # Button Name Load
    # Popup Check
    @Slot()
    def RG_All_Name_Load(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  전체 버튼 이름 불러오기")
        self.qdialog.Qui.Main_Message.setText("전체 버튼의 이름을 불러 오시겠습니까?")
        # OK
        if self.qdialog.exec_():
            self.buttonNameLoad_()
            self.statusBar().showMessage('버튼 이름을 불러왔습니다.', 5000)

    # Loding Action
    def buttonNameLoad_(self):
        try:
            for group in range(4):
                with open(self.btn_Name_FileName[group], 'r') as file:
                    self.line = file.read().splitlines()
                    for i in range(24):
                        self.btn_Name[group][i].setText(self.line[i])
                        self.btn_Ui[group][i].setText(self.line[i])
        except:
            pass

    # 버튼 상태 저장하기
    def buttonStateSave(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  버튼 상태값 저장")
        self.qdialog.Qui.Main_Message.setText("버튼 상태값을 저장 하시겠습니까?")

        if self.qdialog.exec_():
            self.buttonStateFileSave()

    def buttonStateFileSave(self):
        for group in range(4):
            with open(self.btn_State_FileName[group], 'w') as file:
                for i in range(24):
                    if self.btn_Ui[group][i].isChecked():
                        file.write('1\n')
                    else:
                        file.write('0\n')
        start_new_thread(self.udpLogReturn,
                         (LocalID, 'Paging Control -- 버튼 상태값이 저장되었습니다.'))
        self.statusBar().showMessage('버튼 상태값이 저장되었습니다.', 5000)

    # 버튼 상태 불러오기
    @Slot()
    def buttonStateLoad(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  버튼 상태값 블러오기")
        self.qdialog.Qui.Main_Message.setText("버튼 상태값을 불러 오시겠습니까?")

        if self.qdialog.exec_():
            self.buttonStateFileLoad()

    # Button Status Load From Files
    def buttonStateFileLoad(self):
        try:
            for group in range(4):
                with open(self.btn_State_FileName[group], 'r') as file:
                    line = file.read().splitlines()
                    for i in range(24):
                        if line[i] == '1':
                            self.btn_Ui[group][i].setChecked(True)
                            start_new_thread(
                                self.udpReturnThread, ('r,{},{},{},1,!'.format(LocalID, group+1, i+1),))
                        else:
                            self.btn_Ui[group][i].setChecked(False)
                            start_new_thread(
                                self.udpReturnThread, ('r,{},{},{},0,!'.format(LocalID, group+1, i+1),))
            if self.serialMode == 0:
                self.BleuRg_Action(0)
            elif self.serialMode == 1:
                self.DRG116_Action(0)  # DRG116 상태 갱신
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- 버튼 상태값 불러오기를 실행하였습니다.'))
            self.statusBar().showMessage('버튼 상태값 불러오기를 실행하였습니다.', 5000)

        except:
            pass

    # Return to Home
    @Slot()
    def setHome(self):
        self.Main_Menu_Buttons[0].setChecked(True)
        self.Main_View.setCurrentIndex(0)

    # Serial Mode Change
    def serialModeChange(self):
        self.serialMode = self.comboBox_Serial_Mode.currentIndex()
        if self.serialMode == 0:
            self.serNum2.close()
            sleep(.1)
            self.serNum2 = serial.Serial('/dev/ttyUSB0', 38400, timeout=1)
        elif self.serialMode == 1:
            self.serNum2.close()
            sleep(.1)
            self.serNum2 = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

    # Serial mode save to file
    @Slot()
    def serialModeSaveToFile(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  시리얼 통신 설정 변경")
        self.qdialog.Qui.Main_Message.setText("시리얼 통신 설정을 변경 하시겠습니까?")
        # OK
        if self.qdialog.exec_():
            with open("Serial.txt", 'w') as file:
                file.write(str(self.serialMode)+'\n')
                file.write(self.lineEdit_Bss_Reboot_Code.text()+'\n')
            start_new_thread(self.udpLogReturn, (LocalID,
                             'Paging Control -- Serial Mode 설정이 변경되었습니다.'))
            self.statusBar().showMessage('  Paging Serial Mode 설정이 변경되었습니다.', 5000)

    # Serial Mode Load from File
    def setSerialfrom_(self):
        try:
            with open('Serial.txt', 'r') as file:
                line = file.read().splitlines()
                self.serialMode = int(line[0])
                self.comboBox_Serial_Mode.setCurrentIndex(int(line[0]))
                self.lineEdit_Bss_Reboot_Code.setText(line[1])
        except:
            pass

    # IP Seve
    def serverIpAddressSave(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  IP 주소를 저장")
        self.qdialog.Qui.Main_Message.setText(
            "시스템 IP 주소를 저장하시겠습니까?\n재부팅 이후 적용 됩니다.")

        if self.qdialog.exec_():
            try:
                self.change_IP_Address(True)
                start_new_thread(
                    self.udpLogReturn, (LocalID, 'Paging Control -- IP가 변경되었습니다. {}'.format(' '.join(self.tcpServerAddress)),))
                self.statusBar().showMessage('  Paging IP 설정이 저장 되었습니다. 리부팅 이후 적용됩니다.', 5000)
            except:
                self.change_IP_Address(True)
                start_new_thread(self.udpLogReturn, (LocalID,
                                 'Paging Control -- IP 설정 저장 중 문제가 발생하였습니다.'))
                self.statusBar().showMessage('  Paging IP 설정 저장 중 문제가 발생하였습니다.', 5000)

    # IP Change
    def change_IP_Address(self, ipChange):
        if ipChange == True:
            for i in range(4):
                if self.lineEdit_IP[i].text() == '':
                    self.ip[i] = '0'
                else:
                    self.ip[i] = self.lineEdit_IP[i].text()

                if self.lineEdit_NM[i].text() == '' and i != 3:
                    self.nm[i] = '255'
                elif self.lineEdit_NM[i].text() == '' and i == 3:
                    self.nm[i] = '0'
                else:
                    self.nm[i] = self.lineEdit_NM[i].text()

                if self.lineEdit_GW[i].text() == '':
                    self.gw[i] = '0'
                else:
                    self.gw[i] = self.lineEdit_GW[i].text()

                self.clientIp[i] = self.lineEdit_Client[i].text()

            self.tcpServerAddress[1] = '.'.join(self.ip)
            if self.tcpServerAddress[1] == '0.0.0.0':
                self.tcpServerAddress[1] = '192.168.1.199'
            self.tcpServerAddress[2] = '.'.join(self.nm)
            self.tcpServerAddress[3] = '.'.join(self.gw)
            if self.lineEdit_Server_Port.text() == '':
                self.tcpServerAddress[4] = '8888'
            else:
                self.tcpServerAddress[4] = self.lineEdit_Server_Port.text()
            self.tcpServerAddress[5] = '.'.join(self.clientIp)
            self.tcpServerAddress[6] = self.lineEdit_Client_Port.text()
            self.tcpServerAddress[7] = self.lineEdit_Client_ID.text()

            with open('ipset.txt', 'w') as file:
                for i in range(8):
                    file.write(self.tcpServerAddress[i]+'\n')

            try:
                with open('/etc/dhcpcd.conf', 'w') as file:
                    file.write('interface eth0\nstatic ip_address={}/24\nstatic routers={}'.format(
                        self.tcpServerAddress[1], self.tcpServerAddress[3]))
            except:
                pass
        else:
            try:
                with open('ipset.txt', 'r') as file:
                    self.line = file.read().splitlines()
                    for i in range(8):
                        self.tcpServerAddress[i] = self.line[i]
                    self.ip = self.tcpServerAddress[1].split('.')
                    self.nm = self.tcpServerAddress[2].split('.')
                    self.gw = self.tcpServerAddress[3].split('.')
                    self.clientIp = self.tcpServerAddress[5].split('.')

                for i in range(4):
                    self.lineEdit_IP[i].setText(self.ip[i])
                    self.lineEdit_NM[i].setText(self.nm[i])
                    self.lineEdit_GW[i].setText(self.gw[i])
                    self.lineEdit_Client[i].setText(self.clientIp[i])

                self.lineEdit_Server_Port.setText(self.tcpServerAddress[4])
                self.lineEdit_Client_Port.setText(self.tcpServerAddress[6])
                self.lineEdit_Client_ID.setText(self.tcpServerAddress[7])
            except:
                pass
    # Network Module
    # TCP Server Indicator Event

    @Slot(bool)
    def serverConnectClient(self, state):
        if state == True:
            self.Main_Menu_Indcators[2].setChecked(True)
            self.tcpServerNetworkStatus = True
            start_new_thread(self.udpLogReturn,
                             (LocalID, '네트워크 클라이언트가 연결 되었습니다.'))
            self.statusBar().showMessage('네트워크 클라이언트가 연결되었습니다.', 5000)

        else:
            self.Main_Menu_Indcators[2].setChecked(False)
            self.tcpServerNetworkStatus = False
            start_new_thread(self.udpLogReturn(
                LocalID, '네트워크 클라이언트가 연결이 해제 되었습니다.'))
            self.statusBar().showMessage('네트워크 클라이언트가 연결이 해제 되었습니다.', 5000)
    # Network Indcator

    @Slot()
    def ind_Network_Check(self):
        if self.tcpServerNetworkStatus == True:
            self.Main_Menu_Indcators[2].setChecked(True)
        else:
            self.Main_Menu_Indcators[2].setChecked(False)

    def Communicate_State(self, state):
        self.Main_Menu_Indcators[1].setChecked(state)
        sleep(.5)
        self.Main_Menu_Indcators[1].setChecked(False)

    @Slot(bool)
    def Communicate_State_Start(self, state):
        start_new_thread(self.Communicate_State, (state,))

    # Server Data Parcing
    @Slot(str)
    def server_data_parcing(self, data):
        try:
            if data == 'recall':
                self.buttonStateFileLoad()
            elif data == 'save':
                self.buttonStateFileSave()
            else:
                self.set_RG_Btn = data.split(',')
                if self.set_RG_Btn[0] == 'r' and len(self.set_RG_Btn) == 4:
                    self.relay_Btn_Act_('Remote', int(self.set_RG_Btn[1]), int(
                        self.set_RG_Btn[2]), int(self.set_RG_Btn[3]))
                if self.set_RG_Btn[0] == 'play':
                    self.player_play.emit(int(self.set_RG_Btn[1])-1)
                elif self.set_RG_Btn[0] == 'stop':
                    self.player_stop.emit()
        except:
            self.tcpServerReturnString.emit(
                'Error Message {0}'.format(len(self.rg_btn_Status)))
            start_new_thread(self.udpLogReturn, (LocalID, '네트워크 명령이 잘못되었습니다.'))
            self.statusBar().showMessage('네트워크 명령이 잘못되었습니다.', 5000)

    # Button Event
    # interup

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            start_new_thread(self.udpLogReturn,
                             (LocalID, 'Paging Control -- 어플리케이션이 종료 되었습니다.'))
            sys.exit()
    # System reboot

    @Slot()
    def systemReboot(self):
        # dialog
        self.qdialog.Qui.Title_message.setText("  시스템 재부팅")
        self.qdialog.Qui.Main_Message.setText("시스템을 재부팅 하시겠습니까?")
        # ok
        if self.qdialog.exec_():
            start_new_thread(self.udpLogReturn,
                             (LocalID, 'Paging Control -- 시스템을 재부팅합니다.'))
            subprocess.run('sudo reboot', shell=True)

    @Slot()
    def main_Page_Change(self):
        self.mainPageNum = self.buttonGroup_MainMenu.checkedId()
        self.Main_View.setCurrentIndex(self.mainPageNum)

    @Slot(int)
    def setup_Page_Change(self, num):
        self.stackedWidget_Setup.setCurrentIndex(num)
    # Realy Group Button 1

    @Slot(int)
    def btn_Clicked_RG_1(self, btnNum):
        self.btn_Clicked(1, btnNum)
    # Realy Group Button 2

    @Slot(int)
    def btn_Clicked_RG_2(self, btnNum):
        self.btn_Clicked(2, btnNum)
    # Realy Group Button 3

    @Slot(int)
    def btn_Clicked_RG_3(self, btnNum):
        self.btn_Clicked(3, btnNum)
    # Realy Group Button 4

    @Slot(int)
    def btn_Clicked_RG_4(self, btnNum):
        self.btn_Clicked(4, btnNum)
    # Relay Group Button Action

    def btn_Clicked(self, id, btnNum):
        if btnNum == 24:
            self.relayChannel = 0
            self.relayValue = 1
        elif btnNum == 25:
            self.relayChannel = 0
            self.relayValue = 0
        else:
            self.relayChannel = btnNum + 1
            if self.btn_Ui[id-1][btnNum].isChecked():
                self.relayValue = 1
            else:
                self.relayValue = 0
        self.relay_Btn_Act_('Local', id, self.relayChannel, self.relayValue)
    # 버튼 및 릴레이 동작 함수

    def relay_Btn_Act_(self, _from, _relayGroup, _relayChannel, _relayValue):
        # 채널별 동작
        if _relayChannel != 0:
            self.btn_Ui[_relayGroup-1][_relayChannel-1].setChecked(_relayValue)
        # 전체 동작
        else:
            if _relayValue == 1:
                for i in range(24):
                    self.btn_Ui[_relayGroup-1][i].setChecked(True)
            elif _relayValue == 0:
                for i in range(24):
                    self.btn_Ui[_relayGroup-1][i].setChecked(False)

        # 릴레이 그룹에 전달
        if self.serialMode == 0:
            self.BleuRg_Action(_relayGroup)

        elif self.serialMode == 1:
            self.DRG116_Action(_relayGroup)

        # 서버 전달
        start_new_thread(self.udpLogReturn, (LocalID, 'Paging Control -- {} ID {} CH {} Value {}'.format(
            _from, _relayGroup, _relayChannel, _relayValue)))
        if _from == 'Local':
            start_new_thread(self.udpReturnThread, ('r,{},{},{},{},!'.format(
                LocalID, _relayGroup, _relayChannel, _relayValue), ))
            start_new_thread(self.Communicate_State, (True,))
    # BLUE RELAY 동작

    def BleuRg_Action(self, groupId):
        if groupId == 0:
            for group in range(4):
                for i in range(24):
                    if i == 0:
                        if self.btn_Ui[group][i].isChecked():
                            self.relayActionData = '1'
                        else:
                            self.relayActionData = '0'
                    else:
                        if self.btn_Ui[group][i].isChecked():
                            self.relayActionData = self.relayActionData + ',1'
                        else:
                            self.relayActionData = self.relayActionData + ',0'
                self.rtSerialData = blueRg(group+1, self.relayActionData)
                try:
                    self.serNum2.write(
                        binascii.unhexlify(self.rtSerialData.run()))
                    sleep(.1)
                except:
                    pass
        else:
            for i in range(24):
                if i == 0:
                    if self.btn_Ui[groupId-1][i].isChecked():
                        self.relayActionData = '1'
                    else:
                        self.relayActionData = '0'
                else:
                    if self.btn_Ui[groupId-1][i].isChecked():
                        self.relayActionData = self.relayActionData + ',1'
                    else:
                        self.relayActionData = self.relayActionData + ',0'
            self.rtSerialData = blueRg(groupId, self.relayActionData)
            try:
                self.serNum2.write(binascii.unhexlify(self.rtSerialData.run()))
            except:
                pass
    # DRG116 동작

    def DRG116_Action(self, groupId):
        if groupId == 0:
            for group in range(4):
                for i in range(16):
                    if i == 0:
                        if self.btn_Ui[group][i].isChecked():
                            self.relayActionData = '1'
                        else:
                            self.relayActionData = '0'
                    else:
                        if self.btn_Ui[group][i].isChecked():
                            self.relayActionData = self.relayActionData + ',1'
                        else:
                            self.relayActionData = self.relayActionData + ',0'
                self.rtSerialData = sovico_DRG116(
                    group+1, self.relayActionData)
                try:
                    self.serNum2.write(binascii.unhexlify(
                        self.rtSerialData.drg116()))
                    sleep(.1)
                except:
                    pass
        else:
            for i in range(16):
                if i == 0:
                    if self.btn_Ui[groupId-1][i].isChecked():
                        self.relayActionData = '1'
                    else:
                        self.relayActionData = '0'
                else:
                    if self.btn_Ui[groupId-1][i].isChecked():
                        self.relayActionData = self.relayActionData + ',1'
                    else:
                        self.relayActionData = self.relayActionData + ',0'
            self.rtSerialData = sovico_DRG116(groupId, self.relayActionData)
            try:
                self.serNum2.write(binascii.unhexlify(
                    self.rtSerialData.drg116()))
            except:
                pass
    # Bss Meter udp return

    @Slot()
    def bssMeterReturn(self):
        try:
            rtData = ','.join(bssLevelPresence)
            start_new_thread(self.udpReturnThread,
                             ('m,{},{},!'.format(LocalID, rtData), ))
            start_new_thread(self.Communicate_State, (True,))
        except:
            start_new_thread(self.udpReturnThread, ('error', ))
            start_new_thread(self.Communicate_State, (True,))

    def udpReturnThread(self, rtData):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.sendto(rtData.encode('utf-8'),
                         (clientServerIP, int(clientServerPort)))
        self.sock.close()

    def audioPlayButton_Clicked(self, channel):
        if channel == 8:
            self.player_stop.emit()
        else:
            self.player_play.emit(channel)

# TCP서버 클래스


class TCPServer_Socket(QThread):
    TCPServerReceiveString = Signal(str)
    TCPServerConnectClient = Signal(bool)
    TCPServerComm = Signal(bool)

    def __init__(self, parent=None):
        super(TCPServer_Socket, self).__init__(parent)
        global tcpServerPort
        self.clients = []
        self.print_Lock = threading.Lock()

    # Tcp Server Start
    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", tcpServerPort))
        print('Waiting Clients')
        server_socket.listen(50)

        while True:
            client, client_Addr = server_socket.accept()
            print('Client Connect to :', client_Addr[0], client_Addr[1])
            if client:
                self.clients.append(client)
                self.TCPServerConnectClient.emit(True)
            self.stringReturn('{} : Connected'.format(client_Addr))
            start_new_thread(self.tcp_Client_Thread, (client, client_Addr))
        server_socket.close()

    def tcp_Client_Thread(self, c, addr):
        while True:
            data = c.recv(1024)
            if not data:
                print(addr, 'Disconnect')
                self.clients.remove(c)
                if self.clients:
                    self.stringReturn('{} Disconnect'.format(addr))
                else:
                    self.TCPServerConnectClient.emit(False)
                break
            self.print_Lock.acquire()
            self.TCPServerReceiveString.emit(data.decode('utf-8'))
            self.TCPServerComm.emit(True)
            self.print_Lock.release()
        c.close()

    # TCP Server Return
    @Slot(str)
    def stringReturn(self, message):
        if self.clients:
            for client in self.clients:
                client.send(message.encode('utf-8'))
            self.TCPServerComm.emit(True)

# BSS Serial Data 갱신


class serial_BssMeterRT(QThread):
    def __init__(self, parent=None):
        super(serial_BssMeterRT, self).__init__(parent)
        global bssLevelPresence

        self.ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
        print('serial port 1 start')

    def run(self):
        while True:
            if self.ser.isOpen():
                try:
                    self.serResponse = self.ser.readline().decode()
                    if self.serResponse == '':
                        pass
                    else:
                        print(self.serResponse)
                        self.re_P = re.compile(r'(\d+),(\d)')
                        self.bluMeterPresence = self.re_P.search(
                            self.serResponse)
                        self.levelAddr = int(self.bluMeterPresence.group(1))
                        self.levelValue = self.bluMeterPresence.group(2)
                        print(self.bluMeterPresence.group(1),
                              self.bluMeterPresence.group(2))
                        bssLevelPresence[self.levelAddr-1] = self.levelValue
                except:
                    pass
            else:
                sleep(1)
                self.ser.close()
                try:
                    self.ser = serial.Serial('/dev/ttyAMA0', 115200, timeout=1)
                except:
                    pass

    @Slot(str)
    def bssReboot(self, data):
        if self.ser.isOpen():
            self.ser.write(binascii.unhexlify(data))

        else:
            self.ser.close()
            wait(.1)
            self.ser.open()
            self.ser.write(binascii.unhexlify(data))

# BSS Meter Data Return


class udpSendBssMeter(QThread):
    udpMeterRT = Signal()

    def __init__(self, parent=None):
        super(udpSendBssMeter, self).__init__(parent)

    def run(self):
        while True:
            sleep(5)
            self.udpMeterRT.emit()

# Audio Streamer Class


class audioStreamReceiver(QThread):
    player_State = Signal(str)
    play_on = Signal(bool)

    def __init__(self, parent=None):
        super(audioStreamReceiver, self).__init__(parent)
        self.audio_file = ['1.wav', '2.wav', '3.wav',
                           '4.wav', '5.wav', '6.wav', '7.wav', '8.wav']
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.audio_set_volume(100)
        self.Event_Manager = self.player.event_manager()
        self.Event_Manager.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songFinished)

    @Slot(int)
    def play(self, index):
        playmedia = "/home/page/paging/audio/" + \
            self.audio_file[index]  # Set audio file folder
        print(playmedia)
        if os.path.isfile(playmedia):
            self.media = self.instance.media_new(playmedia)
            self.player.set_media(self.media)
            self.player.play()
            self.player_State.emit('Local Event Play - {}'.format(playmedia))
            self.play_on.emit(True)
        else:
            self.player_State.emit('Local Event Play End')
            self.play_on.emit(False)

    @Slot()
    def stop(self):
        self.player.stop()
        self.player_State.emit('Local Event Stop')
        self.play_on.emit(False)

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.player.audio_set_volume(100)
        self.Event_Manager = self.player.event_manager()
        self.Event_Manager.event_attach(
            vlc.EventType.MediaPlayerEndReached, self.songFinished)

    def songFinished(self, data):
        self.player_State.emit('Local Event Play End')
        self.play_on.emit(False)


class EM_Alarm(QThread):
    em_Set = Signal(int, int)

    def __init__(self, parent=None):
        super(EM_Alarm, self).__init__(parent)
        self.pin17 = False
        self.pin18 = False
        self.pin27 = False
        self.pin22 = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN)
        GPIO.setup(18, GPIO.IN)
        GPIO.setup(27, GPIO.IN)
        GPIO.setup(22, GPIO.IN)

        self.em_Set.emit(3, 0)

    def run(self):
        try:
            while True:

                if GPIO.input(17) == False and self.pin17 == False:
                    self.pin17 = True
                    self.em_Set.emit(1, 17)
                elif GPIO.input(17) == True and self.pin17 == True:
                    self.pin17 = False
                    self.em_Set.emit(0, 17)

                if GPIO.input(18) == False and self.pin18 == False:
                    self.pin18 = True
                    self.em_Set.emit(True, 18)
                elif GPIO.input(18) == True and self.pin18 == True:
                    self.pin18 = False
                    self.em_Set.emit(False, 18)

                if GPIO.input(27) == False and self.pin27 == False:
                    self.pin27 = True
                    self.em_Set.emit(True, 27)
                elif GPIO.input(27) == True and self.pin27 == True:
                    self.pin27 = False
                    self.em_Set.emit(False, 27)

                if GPIO.input(22) == False and self.pin22 == False:
                    self.pin22 = True
                    self.em_Set.emit(True, 22)
                elif GPIO.input(22) == True and self.pin22 == True:
                    self.pin22 = False
                    self.em_Set.emit(False, 22)
                sleep(1)
        except:
            self.em_Set.emit(2, 0)


if __name__ == "__main__":
    osPlatform = platform.system()
    print('현제 운영 시스템은 {} 입니다.'.format(osPlatform))
    app = QApplication(sys.argv)
    main = Main_UI()
    sys.exit(app.exec_())
