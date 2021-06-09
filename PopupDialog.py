# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, Slot, Signal

class Ui_DialogQuestion(object):
    def setupUi(self, Dialog):
        self.messageFont = QtGui.QFont()
        self.messageFont.setFamily("나눔고딕")
        self.messageFont.setPointSize(12)

        self.btnFont = QtGui.QFont()
        self.btnFont.setFamily("나눔고딕")
        self.btnFont.setPointSize(10)
        self.btnFont.setBold(True)

        self.titleFont = QtGui.QFont()
        self.titleFont.setFamily("나눔고딕")
        self.titleFont.setPointSize(12)
        self.titleFont.setBold(True)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        Dialog.move(200, 115)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 361, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_Ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_Ok.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_Ok.setFont(self.btnFont)
        self.btn_Ok.setObjectName("btn_Ok")
        self.horizontalLayout.addWidget(self.btn_Ok)
        self.btn_Cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_Cancel.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_Cancel.setFont(self.btnFont)
        self.btn_Cancel.setObjectName("btn_Cancel")
        self.horizontalLayout.addWidget(self.btn_Cancel)

        self.Title_bar = QtWidgets.QWidget(Dialog)
        self.Title_bar.setObjectName("Title_bar")
        self.Title_message = QtWidgets.QLabel(self.Title_bar)
        self.Title_message.setFont(self.titleFont)
        self.Title_message.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.Title_message.setStyleSheet("QLabel{background-color:rgb(72,72,72); Color:white;}")
        self.Title_message.setObjectName("Title_message")

        self.Main_Message = QtWidgets.QLabel(Dialog)
        self.Main_Message.setGeometry(QtCore.QRect(30, 60, 341, 91))
        self.Main_Message.setFont(self.messageFont)
        self.Main_Message.setObjectName("Main_Message")

        self.retranslateUi(Dialog)
        self.btn_Ok.clicked.connect(Dialog.accept)
        self.btn_Cancel.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_Ok.setText(_translate("Dialog", "확인"))
        self.btn_Cancel.setText(_translate("Dialog", "취소"))
        self.Title_message.setText(_translate("Dialog", "메세지 이름"))
        self.Main_Message.setText(_translate("Dialog", "시스템 메세지"))


class Ui_DialogInfo(object):
    def setupUi(self, Dialog):
        self.messageFont = QtGui.QFont()
        self.messageFont.setFamily("나눔고딕")
        self.messageFont.setPointSize(12)

        self.btnFont = QtGui.QFont()
        self.btnFont.setFamily("나눔고딕")
        self.btnFont.setPointSize(10)
        self.btnFont.setBold(True)

        self.titleFont = QtGui.QFont()
        self.titleFont.setFamily("나눔고딕")
        self.titleFont.setPointSize(14)
        self.titleFont.setBold(True)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        Dialog.move(200, 115)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 361, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_Ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_Ok.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_Ok.setFont(self.btnFont)
        self.btn_Ok.setObjectName("btn_Ok")
        self.horizontalLayout.addWidget(self.btn_Ok)

        self.Title_bar = QtWidgets.QWidget(Dialog)
        self.Title_bar.setObjectName("Title_bar")
        self.Title_message = QtWidgets.QLabel(self.Title_bar)
        self.Title_message.setFont(self.titleFont)
        self.Title_message.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.Title_message.setStyleSheet("QLabel{background-color:rgb(72, 72, 72); Color:white;}")
        self.Title_message.setFont(self.titleFont)
        self.Title_message.setObjectName("Title_message")

        self.Main_Message = QtWidgets.QLabel(Dialog)
        self.Main_Message.setGeometry(QtCore.QRect(30, 90, 341, 31))
        self.Main_Message.setObjectName("Main_Message")
        self.Main_Message.setFont(self.messageFont)
        self.Main_Message.setObjectName("Main_Message")


        self.retranslateUi(Dialog)
        self.btn_Ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_Ok.setText(_translate("Dialog", "확인"))
        self.Title_message.setText(_translate("Dialog", "메세지 이름"))
        self.Main_Message.setText(_translate("Dialog", "시스템 메세지"))

class Ui_DialogEM(object):
    def setupUi(self, Dialog):
        self.messageFont = QtGui.QFont()
        self.messageFont.setFamily("나눔고딕")
        self.messageFont.setPointSize(12)

        self.btnFont = QtGui.QFont()
        self.btnFont.setFamily("나눔고딕")
        self.btnFont.setPointSize(10)
        self.btnFont.setBold(True)

        self.titleFont = QtGui.QFont()
        self.titleFont.setFamily("나눔고딕")
        self.titleFont.setPointSize(14)
        self.titleFont.setBold(True)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        Dialog.move(200, 115)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 361, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_Ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_Ok.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_Ok.setFont(self.btnFont)
        self.btn_Ok.setObjectName("btn_Ok")
        self.horizontalLayout.addWidget(self.btn_Ok)

        self.Title_bar = QtWidgets.QWidget(Dialog)
        self.Title_bar.setObjectName("Title_bar")

        self.Title_message = QtWidgets.QLabel(self.Title_bar)
        self.Title_message.setFont(self.titleFont)
        self.Title_message.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.Title_message.setStyleSheet("QLabel{background-color:red; Color:white;}")
        self.Title_message.setObjectName("Title_message")

        self.Main_Message = QtWidgets.QLabel(Dialog)
        self.Main_Message.setGeometry(QtCore.QRect(30, 90, 341, 31))
        self.Main_Message.setObjectName("Main_Message")
        self.Main_Message.setFont(self.messageFont)
        self.Main_Message.setObjectName("Main_Message")


        self.retranslateUi(Dialog)
        self.btn_Ok.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_Ok.setText(_translate("Dialog", "확인"))
        self.Title_message.setText(_translate("Dialog", "EM 발생"))
        self.Main_Message.setText(_translate("Dialog", "화재가 발생하였습니다."))

class Ui_DialogKeypad_ip(object):
    def setupUi(self, Dialog):
        #_translate = QtCore.QCoreApplication.translate
        #Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #self.Title_message.setText(_translate("Dialog", "IP 입력"))

        self.keypadFont = QtGui.QFont()
        self.keypadFont.setFamily("나눔고딕")
        self.keypadFont.setPointSize(8)

        self.textEditFont = QtGui.QFont()
        self.textEditFont.setFamily("나눔고딕")
        self.textEditFont.setPointSize(12)
        #self.textEditFont.setBold(True)

        self.titleFont = QtGui.QFont()
        self.titleFont.setFamily("나눔고딕")
        self.titleFont.setPointSize(14)
        self.titleFont.setBold(True)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.move(200, 50)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        #Dialog.setStyleSheet("QDialog {background-color:#202020}")

        self.TextEditBox = QtWidgets.QWidget(Dialog)
        self.TextEditBox.setGeometry(QtCore.QRect(50, 60, 300, 50))
        self.TextEditBox.setObjectName("TextEditBox")


        self.textEditHLayout = QtWidgets.QHBoxLayout(self.TextEditBox)
        self.textEditHLayout.setContentsMargins(0,0,0,0)

        self.text_Ip1 = QtWidgets.QLineEdit(self.TextEditBox)
        self.text_Ip2 = QtWidgets.QLineEdit(self.TextEditBox)
        self.text_Ip3 = QtWidgets.QLineEdit(self.TextEditBox)
        self.text_Ip4 = QtWidgets.QLineEdit(self.TextEditBox)


        self.text_Inputs = [self.text_Ip1,self.text_Ip2,self.text_Ip3,self.text_Ip4]
        for i,v in enumerate(self.text_Inputs):
        	v.setFont(self.textEditFont)
        	v.setAlignment(QtCore.Qt.AlignCenter)
        	v.setMaxLength(3)
        	v.setMinimumSize(QtCore.QSize(0,40))
        	self.textEditHLayout.addWidget(v)

        self.KeypadBox = QtWidgets.QWidget(Dialog)
        self.KeypadBox.setGeometry(QtCore.QRect(50,120, 300,250))

        self.gridLayout = QtWidgets.QGridLayout(self.KeypadBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        

        self.btn_1 = QtWidgets.QPushButton('1',self.KeypadBox)
        self.btn_2 = QtWidgets.QPushButton('2',self.KeypadBox)
        self.btn_3 = QtWidgets.QPushButton('3',self.KeypadBox)
        self.btn_4 = QtWidgets.QPushButton('4',self.KeypadBox)
        self.btn_5 = QtWidgets.QPushButton('5',self.KeypadBox)
        self.btn_6 = QtWidgets.QPushButton('6',self.KeypadBox)
        self.btn_7 = QtWidgets.QPushButton('7',self.KeypadBox)
        self.btn_8 = QtWidgets.QPushButton('8',self.KeypadBox)
        self.btn_9 = QtWidgets.QPushButton('9',self.KeypadBox)
        self.btn_0 = QtWidgets.QPushButton('0',self.KeypadBox)
        self.btn_clear = QtWidgets.QPushButton('CLEAR',self.KeypadBox)
        self.btn_ok = QtWidgets.QPushButton('확인',self.KeypadBox)
        self.btn_cancel = QtWidgets.QPushButton('취소',self.KeypadBox)
        self.btn_bs = QtWidgets.QPushButton('DEL',self.KeypadBox)
        self.btn_dot = QtWidgets.QPushButton('NEXT',self.KeypadBox)


        self.buttons = [self.btn_0,self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6,self.btn_7,self.btn_8,self.btn_9,self.btn_cancel,self.btn_clear,self.btn_ok,self.btn_dot,self.btn_bs]
        for i,v in enumerate(self.buttons):
	        v.setMinimumSize(QtCore.QSize(0, 50))
	        v.setFont(self.keypadFont)
        self.gridLayout.addWidget(self.btn_1, 0,0)
        self.gridLayout.addWidget(self.btn_2, 0,1)
        self.gridLayout.addWidget(self.btn_3, 0,2)
        self.gridLayout.addWidget(self.btn_4, 1,0)
        self.gridLayout.addWidget(self.btn_5, 1,1)
        self.gridLayout.addWidget(self.btn_6, 1,2)
        self.gridLayout.addWidget(self.btn_7, 2,0)
        self.gridLayout.addWidget(self.btn_8, 2,1)
        self.gridLayout.addWidget(self.btn_9, 2,2)
        self.gridLayout.addWidget(self.btn_0, 2,3)
        self.gridLayout.addWidget(self.btn_bs, 1,3)
        self.gridLayout.addWidget(self.btn_dot, 3,0)


        self.gridLayout.addWidget(self.btn_clear,0,3)
        self.gridLayout.addWidget(self.btn_ok,3,2)
        self.gridLayout.addWidget(self.btn_cancel,3,3)


        self.Title_bar = QtWidgets.QWidget(Dialog)
        self.Title_bar.setObjectName("Title_bar")

        self.Title_message = QtWidgets.QLabel(self.Title_bar)
        self.Title_message.setFont(self.titleFont)
        self.Title_message.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.Title_message.setStyleSheet("QLabel{background-color:rgb(72, 72, 72); Color:white;}")
        self.Title_message.setObjectName("Title_message")

        #self.retranslateUi(Dialog)
        self.btn_ok.clicked.connect(Dialog.accept)
        self.btn_cancel.clicked.connect(Dialog.reject)
        self.text_Ip1.selectionChanged.connect(lambda: self.textBoxOnClicked(1))
        self.text_Ip2.selectionChanged.connect(lambda: self.textBoxOnClicked(2))
        self.text_Ip3.selectionChanged.connect(lambda: self.textBoxOnClicked(3))
        self.text_Ip4.selectionChanged.connect(lambda: self.textBoxOnClicked(4))

        self.btn_0.clicked.connect(lambda: self.keypadInputs('0'))
        self.btn_1.clicked.connect(lambda: self.keypadInputs('1'))
        self.btn_2.clicked.connect(lambda: self.keypadInputs('2'))
        self.btn_3.clicked.connect(lambda: self.keypadInputs('3'))
        self.btn_4.clicked.connect(lambda: self.keypadInputs('4'))
        self.btn_5.clicked.connect(lambda: self.keypadInputs('5'))
        self.btn_6.clicked.connect(lambda: self.keypadInputs('6'))
        self.btn_7.clicked.connect(lambda: self.keypadInputs('7'))
        self.btn_8.clicked.connect(lambda: self.keypadInputs('8'))
        self.btn_9.clicked.connect(lambda: self.keypadInputs('9'))
        self.btn_clear.clicked.connect(self.keypadClear)
        self.btn_bs.clicked.connect(self.keypadbs)
        self.btn_dot.clicked.connect(self.keypadNext)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.textBoxOnClicked(1)

    def textBoxOnClicked(self,num):
    	print('OK',num)
    	self.currentTextedit = num
    	for i,v in enumerate(self.text_Inputs):
    		if i == self.currentTextedit - 1:
    			v.setStyleSheet("QLineEdit{background-color: #FBEFF2}")
    		else:
    			v.setStyleSheet("QLineEdit{background-color: white}")


    def keypadInputs(self, numText):
    	self.currentText = self.text_Inputs[self.currentTextedit-1].text()
    	if len(self.currentText) == 3 and self.currentTextedit < 4:
    		self.textBoxOnClicked(self.currentTextedit + 1)
    	self.currentText = self.text_Inputs[self.currentTextedit-1].text() + numText
    	self.text_Inputs[self.currentTextedit-1].setText(self.currentText)
    	if len(self.currentText) == 3 and self.currentTextedit < 4:
    		self.textBoxOnClicked(self.currentTextedit + 1)


    def keypadClear(self):
    	if self.currentTextedit == 1:
    		self.text_Ip1.clear()
    	elif self.currentTextedit == 2:
    		self.text_Ip2.clear()
    	elif self.currentTextedit == 3:
    		self.text_Ip3.clear()
    	elif self.currentTextedit == 4:
    		self.text_Ip4.clear()

    def keypadbs(self):
    	self.currentText = self.text_Inputs[self.currentTextedit-1].text()
    	if len(self.currentText) == 0 and self.currentTextedit > 1:
    		self.textBoxOnClicked(self.currentTextedit - 1)
    	self.currentText = self.text_Inputs[self.currentTextedit-1].text()
    	self.currentTextLength = len(self.currentText)-1
    	self.text_Inputs[self.currentTextedit-1].setText(self.currentText[:self.currentTextLength])

    def keypadNext(self):
    	if self.currentTextedit < 4:
    		self.textBoxOnClicked(self.currentTextedit + 1)

class Ui_DialogKeypad_Port(object):
    def setupUi(self, Dialog):
        self.keypadFont = QtGui.QFont()
        self.keypadFont.setFamily("나눔고딕")
        self.keypadFont.setPointSize(8)

        self.textEditFont = QtGui.QFont()
        self.textEditFont.setFamily("나눔고딕")
        self.textEditFont.setPointSize(12)
        #self.textEditFont.setBold(True)

        self.titleFont = QtGui.QFont()
        self.titleFont.setFamily("나눔고딕")
        self.titleFont.setPointSize(14)
        self.titleFont.setBold(True)

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.move(200, 50)
        Dialog.setWindowFlags(Qt.FramelessWindowHint)
        #Dialog.setStyleSheet("QDialog {background-color:#202020}")

        self.TextEditBox = QtWidgets.QWidget(Dialog)
        self.TextEditBox.setGeometry(QtCore.QRect(50, 60, 300, 50))
        self.TextEditBox.setObjectName("TextEditBox")


        self.textEditHLayout = QtWidgets.QHBoxLayout(self.TextEditBox)
        self.textEditHLayout.setContentsMargins(0,0,0,0)

        self.text_Port = QtWidgets.QLineEdit(self.TextEditBox)

        self.text_Port.setFont(self.textEditFont)
        self.text_Port.setAlignment(QtCore.Qt.AlignCenter)
        self.text_Port.setMaxLength(5)
        self.text_Port.setMinimumSize(QtCore.QSize(0,40))
        self.textEditHLayout.addWidget(self.text_Port)

        self.KeypadBox = QtWidgets.QWidget(Dialog)
        self.KeypadBox.setGeometry(QtCore.QRect(50,120, 300,250))

        self.gridLayout = QtWidgets.QGridLayout(self.KeypadBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        

        self.btn_1 = QtWidgets.QPushButton('1',self.KeypadBox)
        self.btn_2 = QtWidgets.QPushButton('2',self.KeypadBox)
        self.btn_3 = QtWidgets.QPushButton('3',self.KeypadBox)
        self.btn_4 = QtWidgets.QPushButton('4',self.KeypadBox)
        self.btn_5 = QtWidgets.QPushButton('5',self.KeypadBox)
        self.btn_6 = QtWidgets.QPushButton('6',self.KeypadBox)
        self.btn_7 = QtWidgets.QPushButton('7',self.KeypadBox)
        self.btn_8 = QtWidgets.QPushButton('8',self.KeypadBox)
        self.btn_9 = QtWidgets.QPushButton('9',self.KeypadBox)
        self.btn_0 = QtWidgets.QPushButton('0',self.KeypadBox)
        self.btn_clear = QtWidgets.QPushButton('CLEAR',self.KeypadBox)
        self.btn_ok = QtWidgets.QPushButton('확인',self.KeypadBox)
        self.btn_cancel = QtWidgets.QPushButton('취소',self.KeypadBox)
        self.btn_bs = QtWidgets.QPushButton('DEL',self.KeypadBox)

        self.buttons = [self.btn_0,self.btn_1,self.btn_2,self.btn_3,self.btn_4,self.btn_5,self.btn_6,self.btn_7,self.btn_8,self.btn_9,self.btn_cancel,self.btn_clear,self.btn_ok,self.btn_bs]
        for i,v in enumerate(self.buttons):
	        v.setMinimumSize(QtCore.QSize(0, 50))
	        v.setFont(self.keypadFont)
        self.gridLayout.addWidget(self.btn_1, 0,0)
        self.gridLayout.addWidget(self.btn_2, 0,1)
        self.gridLayout.addWidget(self.btn_3, 0,2)
        self.gridLayout.addWidget(self.btn_4, 1,0)
        self.gridLayout.addWidget(self.btn_5, 1,1)
        self.gridLayout.addWidget(self.btn_6, 1,2)
        self.gridLayout.addWidget(self.btn_7, 2,0)
        self.gridLayout.addWidget(self.btn_8, 2,1)
        self.gridLayout.addWidget(self.btn_9, 2,2)
        self.gridLayout.addWidget(self.btn_0, 2,3)
        self.gridLayout.addWidget(self.btn_bs, 1,3)

        self.gridLayout.addWidget(self.btn_clear,0,3)
        self.gridLayout.addWidget(self.btn_ok,3,2)
        self.gridLayout.addWidget(self.btn_cancel,3,3)


        self.Title_bar = QtWidgets.QWidget(Dialog)
        self.Title_bar.setObjectName("Title_bar")

        self.Title_message = QtWidgets.QLabel(self.Title_bar)
        self.Title_message.setFont(self.titleFont)
        self.Title_message.setGeometry(QtCore.QRect(0, 0, 401, 40))
        self.Title_message.setStyleSheet("QLabel{background-color:rgb(72, 72, 72); Color:white;}")
        self.Title_message.setObjectName("Title_message")

        #self.retranslateUi(Dialog)
        self.btn_ok.clicked.connect(Dialog.accept)
        self.btn_cancel.clicked.connect(Dialog.reject)
        self.btn_0.clicked.connect(lambda: self.keypadInputs('0'))
        self.btn_1.clicked.connect(lambda: self.keypadInputs('1'))
        self.btn_2.clicked.connect(lambda: self.keypadInputs('2'))
        self.btn_3.clicked.connect(lambda: self.keypadInputs('3'))
        self.btn_4.clicked.connect(lambda: self.keypadInputs('4'))
        self.btn_5.clicked.connect(lambda: self.keypadInputs('5'))
        self.btn_6.clicked.connect(lambda: self.keypadInputs('6'))
        self.btn_7.clicked.connect(lambda: self.keypadInputs('7'))
        self.btn_8.clicked.connect(lambda: self.keypadInputs('8'))
        self.btn_9.clicked.connect(lambda: self.keypadInputs('9'))
        self.btn_clear.clicked.connect(self.keypadClear)
        self.btn_bs.clicked.connect(self.keypadbs)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def keypadInputs(self, numText):
    	self.currentText = self.text_Port.text() + numText
    	self.text_Port.setText(self.currentText)


    def keypadClear(self):
   		self.text_Port.clear()

    def keypadbs(self):
    	self.currentText = self.text_Port.text()
    	self.currentTextLength = len(self.currentText)-1
    	self.text_Port.setText(self.currentText[:self.currentTextLength])

    def keypadNext(self):
    	if self.currentTextedit < 4:
    		self.textBoxOnClicked(self.currentTextedit + 1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DialogKeypad_Port()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

