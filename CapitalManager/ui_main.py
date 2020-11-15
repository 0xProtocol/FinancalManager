# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 678)
        MainWindow.setStyleSheet(u"background-color:rgb(0, 0, 0)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(1, 255, 1);")
        self.frameleft = QFrame(self.centralwidget)
        self.frameleft.setObjectName(u"frameleft")
        self.frameleft.setGeometry(QRect(10, 40, 131, 571))
        self.frameleft.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
" border-top: 2px solid blue; \n"
" border-left: 2px solid blue; \n"
" border-right: 2px solid blue; \n"
" border-bottom: 2px solid blue; ")
        self.frameleft.setFrameShape(QFrame.StyledPanel)
        self.frameleft.setFrameShadow(QFrame.Raised)
        self.btnDashboard = QPushButton(self.frameleft)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setGeometry(QRect(15, 100, 101, 21))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.btnDashboard.setFont(font)
        self.btnDashboard.setAutoFillBackground(False)
        self.btnDashboard.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/BrokenSword.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDashboard.setIcon(icon)
        self.btnDashboard.setIconSize(QSize(20, 20))
        self.btnFormular = QPushButton(self.frameleft)
        self.btnFormular.setObjectName(u"btnFormular")
        self.btnFormular.setGeometry(QRect(15, 140, 101, 21))
        self.btnFormular.setFont(font)
        self.btnFormular.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/atom-beta.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFormular.setIcon(icon1)
        self.btnFormular.setIconSize(QSize(20, 20))
        self.btnStocks = QPushButton(self.frameleft)
        self.btnStocks.setObjectName(u"btnStocks")
        self.btnStocks.setGeometry(QRect(15, 220, 101, 21))
        self.btnStocks.setFont(font)
        self.btnStocks.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/setroubleshoot_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStocks.setIcon(icon2)
        self.btnStocks.setIconSize(QSize(20, 20))
        self.btnCompanyFormular = QPushButton(self.frameleft)
        self.btnCompanyFormular.setObjectName(u"btnCompanyFormular")
        self.btnCompanyFormular.setGeometry(QRect(15, 180, 101, 21))
        self.btnCompanyFormular.setFont(font)
        self.btnCompanyFormular.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/flare.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCompanyFormular.setIcon(icon3)
        self.btnCompanyFormular.setIconSize(QSize(20, 20))
        self.widget_3 = QWidget(self.frameleft)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(5, 5, 121, 81))
        self.widget_3.setStyleSheet(u"QWidget\n"
"{\n"
"  border-image:url(:/newPrefix/logomoney.jpg)0 0 0 0 stretch stretch;\n"
" border-width: 0px;\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; \n"
"}")
        self.btnForex = QPushButton(self.frameleft)
        self.btnForex.setObjectName(u"btnForex")
        self.btnForex.setGeometry(QRect(13, 260, 101, 21))
        self.btnForex.setFont(font)
        self.btnForex.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        self.btnForex.setIcon(icon2)
        self.btnForex.setIconSize(QSize(20, 20))
        self.btnFutures = QPushButton(self.frameleft)
        self.btnFutures.setObjectName(u"btnFutures")
        self.btnFutures.setGeometry(QRect(15, 300, 101, 21))
        self.btnFutures.setFont(font)
        self.btnFutures.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        self.btnFutures.setIcon(icon2)
        self.btnFutures.setIconSize(QSize(20, 20))
        self.btnCrypto = QPushButton(self.frameleft)
        self.btnCrypto.setObjectName(u"btnCrypto")
        self.btnCrypto.setGeometry(QRect(10, 340, 101, 21))
        self.btnCrypto.setFont(font)
        self.btnCrypto.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        self.btnCrypto.setIcon(icon2)
        self.btnCrypto.setIconSize(QSize(20, 20))
        self.btnSettings = QPushButton(self.frameleft)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setGeometry(QRect(10, 500, 101, 21))
        self.btnSettings.setFont(font)
        self.btnSettings.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        self.btnSettings.setIcon(icon2)
        self.btnSettings.setIconSize(QSize(20, 20))
        self.btnVersion = QPushButton(self.frameleft)
        self.btnVersion.setObjectName(u"btnVersion")
        self.btnVersion.setGeometry(QRect(11, 540, 111, 21))
        self.btnVersion.setFont(font)
        self.btnVersion.setStyleSheet(u"QPushButton {\n"
"color: rgb(88, 1, 200);\n"
"border-radius:0;\n"
"border:0;\n"
"background-color: rgb(0, 0, 0);\n"
"text-align:right;\n"
"qproperty-icon: url(:/newPrefix/icons.png);\n"
"qproperty-iconSize: 20px 20px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(24, 27, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color:#333;\n"
"}")
        self.btnVersion.setIcon(icon2)
        self.btnVersion.setIconSize(QSize(20, 20))
        self.btnDashboard.raise_()
        self.btnFormular.raise_()
        self.btnCompanyFormular.raise_()
        self.widget_3.raise_()
        self.btnStocks.raise_()
        self.btnForex.raise_()
        self.btnFutures.raise_()
        self.btnCrypto.raise_()
        self.btnSettings.raise_()
        self.btnVersion.raise_()
        self.framdown = QFrame(self.centralwidget)
        self.framdown.setObjectName(u"framdown")
        self.framdown.setGeometry(QRect(10, 619, 1041, 51))
        self.framdown.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
" border-top: 2px solid blue; \n"
" border-left: 2px solid blue; \n"
" border-right: 2px solid blue; \n"
" border-bottom: 2px solid blue; ")
        self.framdown.setFrameShape(QFrame.StyledPanel)
        self.framdown.setFrameShadow(QFrame.Raised)
        self.frmDashboard = QFrame(self.centralwidget)
        self.frmDashboard.setObjectName(u"frmDashboard")
        self.frmDashboard.setGeometry(QRect(150, 110, 901, 501))
        self.frmDashboard.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
" border-top: 2px solid blue; \n"
" border-left: 2px solid blue; \n"
" border-right: 2px solid blue; \n"
" border-bottom: 2px solid blue; ")
        self.frmDashboard.setFrameShape(QFrame.StyledPanel)
        self.frmDashboard.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frmDashboard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 170, 281, 101))
        self.frmCompanyFormular = QFrame(self.centralwidget)
        self.frmCompanyFormular.setObjectName(u"frmCompanyFormular")
        self.frmCompanyFormular.setGeometry(QRect(150, 110, 901, 501))
        self.frmCompanyFormular.setStyleSheet(u"background-color:rgb(0,0, 0);\n"
" border-top: 2px solid blue; \n"
" border-left: 2px solid blue; \n"
" border-right: 2px solid blue; \n"
" border-bottom: 2px solid blue; ")
        self.frmCompanyFormular.setFrameShape(QFrame.StyledPanel)
        self.frmCompanyFormular.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frmCompanyFormular)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(650, 580, 101, 31))
        self.comboBox_3 = QComboBox(self.frmCompanyFormular)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(10, 10, 171, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.comboBox_3.setFont(font1)
        self.comboBox_3.setStyleSheet(u"background-color: rgb(10,10,10);\n"
"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.label_5 = QLabel(self.frmCompanyFormular)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 40, 121, 81))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(18)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lineEdit = QLineEdit(self.frmCompanyFormular)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 70, 141, 21))
        font3 = QFont()
        font3.setPointSize(14)
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}\n"
"QLineEdit:hover { border: 2px solid rgb(48,50,62);}QLineEdit:focus{border:2px solid rgb(48,50,60)n}")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.btnSend = QPushButton(self.frmCompanyFormular)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setGeometry(QRect(800, 470, 91, 21))
        self.btnSend.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}")
        self.btn_maximize = QPushButton(self.centralwidget)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(985, 10, 13, 13))
        self.btn_maximize.setMinimumSize(QSize(13, 13))
        self.btn_maximize.setMaximumSize(QSize(13, 13))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 6px;	\n"
"	background-color: rgb(126, 248, 54);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")
        self.btn_maximize.setIconSize(QSize(10, 10))
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(1025, 10, 14, 14))
        self.btn_close.setMinimumSize(QSize(14, 14))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 6px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close.setIconSize(QSize(14, 14))
        self.btn_minimize = QPushButton(self.centralwidget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(945, 10, 13, 13))
        self.btn_minimize.setMinimumSize(QSize(13, 13))
        self.btn_minimize.setMaximumSize(QSize(13, 13))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 6px;		\n"
"	background-color: rgb(243, 213,11 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize.setIconSize(QSize(10, 10))
        self.frameup = QFrame(self.centralwidget)
        self.frameup.setObjectName(u"frameup")
        self.frameup.setGeometry(QRect(0, 0, 1061, 36))
        self.frameup.setStyleSheet(u"background-color: rgb(24, 27, 40);")
        self.frameup.setFrameShape(QFrame.StyledPanel)
        self.frameup.setFrameShadow(QFrame.Raised)
        self.lblcapitalmanager = QLabel(self.frameup)
        self.lblcapitalmanager.setObjectName(u"lblcapitalmanager")
        self.lblcapitalmanager.setGeometry(QRect(20, -7, 171, 51))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.lblcapitalmanager.setFont(font4)
        self.lblcapitalmanager.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.frametop = QFrame(self.centralwidget)
        self.frametop.setObjectName(u"frametop")
        self.frametop.setGeometry(QRect(150, 40, 901, 61))
        self.frametop.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
" border-top: 2px solid blue; \n"
" border-left: 2px solid blue; \n"
" border-right: 2px solid blue; \n"
" border-bottom: 2px solid blue; ")
        self.frametop.setFrameShape(QFrame.StyledPanel)
        self.frametop.setFrameShadow(QFrame.Raised)
        self.lblname = QLabel(self.frametop)
        self.lblname.setObjectName(u"lblname")
        self.lblname.setGeometry(QRect(710, 10, 181, 41))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setWeight(50)
        self.lblname.setFont(font5)
        self.lblname.setLayoutDirection(Qt.LeftToRight)
        self.lblname.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblname.setTextFormat(Qt.AutoText)
        self.lblname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frmFormular = QFrame(self.centralwidget)
        self.frmFormular.setObjectName(u"frmFormular")
        self.frmFormular.setGeometry(QRect(150, 110, 901, 501))
        self.frmFormular.setStyleSheet(u"background-color:rgb(0,0, 0);\n"
" border-top: 2px solid blue; \n"
" border-left: 2px solid blue; \n"
" border-right: 2px solid blue; \n"
" border-bottom: 2px solid blue; ")
        self.frmFormular.setFrameShape(QFrame.StyledPanel)
        self.frmFormular.setFrameShadow(QFrame.Raised)
        self.frameAccountStatistic = QFrame(self.frmFormular)
        self.frameAccountStatistic.setObjectName(u"frameAccountStatistic")
        self.frameAccountStatistic.setGeometry(QRect(10, 220, 721, 271))
        self.frameAccountStatistic.setFrameShape(QFrame.StyledPanel)
        self.frameAccountStatistic.setFrameShadow(QFrame.Raised)
        self.pbAccount1 = QProgressBar(self.frameAccountStatistic)
        self.pbAccount1.setObjectName(u"pbAccount1")
        self.pbAccount1.setGeometry(QRect(160, 97, 431, 20))
        self.pbAccount1.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbAccount1.setValue(0)
        self.lblAccount2 = QLabel(self.frameAccountStatistic)
        self.lblAccount2.setObjectName(u"lblAccount2")
        self.lblAccount2.setGeometry(QRect(35, 127, 91, 21))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.lblAccount2.setFont(font6)
        self.lblAccount2.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblAccount3 = QLabel(self.frameAccountStatistic)
        self.lblAccount3.setObjectName(u"lblAccount3")
        self.lblAccount3.setGeometry(QRect(35, 157, 91, 21))
        self.lblAccount3.setFont(font6)
        self.lblAccount3.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblAccount1 = QLabel(self.frameAccountStatistic)
        self.lblAccount1.setObjectName(u"lblAccount1")
        self.lblAccount1.setGeometry(QRect(35, 97, 91, 21))
        self.lblAccount1.setFont(font6)
        self.lblAccount1.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.pbAccount2 = QProgressBar(self.frameAccountStatistic)
        self.pbAccount2.setObjectName(u"pbAccount2")
        self.pbAccount2.setGeometry(QRect(160, 127, 431, 20))
        self.pbAccount2.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbAccount2.setValue(0)
        self.lblTotal = QLabel(self.frameAccountStatistic)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setGeometry(QRect(30, 237, 91, 21))
        self.lblTotal.setFont(font6)
        self.lblTotal.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblTotal.setAlignment(Qt.AlignCenter)
        self.lblMainAccount = QLabel(self.frameAccountStatistic)
        self.lblMainAccount.setObjectName(u"lblMainAccount")
        self.lblMainAccount.setGeometry(QRect(20, 62, 121, 21))
        self.lblMainAccount.setFont(font6)
        self.lblMainAccount.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblAccount4 = QLabel(self.frameAccountStatistic)
        self.lblAccount4.setObjectName(u"lblAccount4")
        self.lblAccount4.setGeometry(QRect(35, 187, 91, 21))
        self.lblAccount4.setFont(font6)
        self.lblAccount4.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.pbAccount4 = QProgressBar(self.frameAccountStatistic)
        self.pbAccount4.setObjectName(u"pbAccount4")
        self.pbAccount4.setGeometry(QRect(160, 187, 431, 20))
        self.pbAccount4.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbAccount4.setValue(0)
        self.pbMainAccount = QProgressBar(self.frameAccountStatistic)
        self.pbMainAccount.setObjectName(u"pbMainAccount")
        self.pbMainAccount.setGeometry(QRect(160, 67, 431, 20))
        self.pbMainAccount.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbMainAccount.setMaximum(100)
        self.pbMainAccount.setValue(0)
        self.pbTotal = QProgressBar(self.frameAccountStatistic)
        self.pbTotal.setObjectName(u"pbTotal")
        self.pbTotal.setGeometry(QRect(160, 240, 431, 20))
        self.pbTotal.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(44, 2, 100, 255));\n"
"}")
        self.pbTotal.setValue(100)
        self.pbAccount3 = QProgressBar(self.frameAccountStatistic)
        self.pbAccount3.setObjectName(u"pbAccount3")
        self.pbAccount3.setGeometry(QRect(160, 157, 431, 20))
        self.pbAccount3.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbAccount3.setValue(0)
        self.btnSend_2 = QPushButton(self.frameAccountStatistic)
        self.btnSend_2.setObjectName(u"btnSend_2")
        self.btnSend_2.setGeometry(QRect(620, 240, 91, 21))
        self.btnSend_2.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}")
        self.lblAccountStatistic = QLabel(self.frameAccountStatistic)
        self.lblAccountStatistic.setObjectName(u"lblAccountStatistic")
        self.lblAccountStatistic.setGeometry(QRect(10, 10, 161, 28))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(16)
        font7.setBold(False)
        font7.setWeight(50)
        self.lblAccountStatistic.setFont(font7)
        self.lblAccountStatistic.setStyleSheet(u"color: rgb(88, 150, 250);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblAccountStatistic.setFrameShape(QFrame.NoFrame)
        self.lblAccountStatistic.setLineWidth(1)
        self.frame = QFrame(self.frmFormular)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 721, 201))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnSpend = QPushButton(self.frame)
        self.btnSpend.setObjectName(u"btnSpend")
        self.btnSpend.setGeometry(QRect(620, 170, 91, 21))
        self.btnSpend.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}")
        self.cbspendmoney = QComboBox(self.frame)
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.setObjectName(u"cbspendmoney")
        self.cbspendmoney.setGeometry(QRect(10, 60, 121, 31))
        self.cbspendmoney.setFont(font)
        self.cbspendmoney.setStyleSheet(u"background-color: rgb(10,10,10);\n"
"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.cbspendmoney.setEditable(False)
        self.lespend = QLineEdit(self.frame)
        self.lespend.setObjectName(u"lespend")
        self.lespend.setGeometry(QRect(160, 110, 141, 21))
        self.lespend.setFont(font3)
        self.lespend.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}\n"
"QLineEdit:hover { border: 2px solid rgb(48,50,62);}QLineEdit:focus{border:2px solid rgb(48,50,60)n}")
        self.lespend.setAlignment(Qt.AlignCenter)
        self.lblSpendMoney = QLabel(self.frame)
        self.lblSpendMoney.setObjectName(u"lblSpendMoney")
        self.lblSpendMoney.setGeometry(QRect(10, 110, 151, 21))
        self.lblSpendMoney.setFont(font6)
        self.lblSpendMoney.setStyleSheet(u"color: rgb(88, 1, 200);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.lblSpendMoney_2 = QLabel(self.frame)
        self.lblSpendMoney_2.setObjectName(u"lblSpendMoney_2")
        self.lblSpendMoney_2.setGeometry(QRect(10, 10, 131, 28))
        self.lblSpendMoney_2.setFont(font7)
        self.lblSpendMoney_2.setStyleSheet(u"color: rgb(88, 150, 250);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.pbSpendMoney = QProgressBar(self.frame)
        self.pbSpendMoney.setObjectName(u"pbSpendMoney")
        self.pbSpendMoney.setGeometry(QRect(160, 140, 431, 20))
        self.pbSpendMoney.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbSpendMoney.setMaximum(100)
        self.pbSpendMoney.setValue(0)
        self.pbSpendMoneyEuro = QProgressBar(self.frame)
        self.pbSpendMoneyEuro.setObjectName(u"pbSpendMoneyEuro")
        self.pbSpendMoneyEuro.setGeometry(QRect(160, 170, 431, 20))
        self.pbSpendMoneyEuro.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.pbSpendMoneyEuro.setMaximum(100)
        self.pbSpendMoneyEuro.setValue(0)
        self.frameHistory = QFrame(self.frmFormular)
        self.frameHistory.setObjectName(u"frameHistory")
        self.frameHistory.setGeometry(QRect(740, 10, 151, 481))
        self.frameHistory.setFrameShape(QFrame.StyledPanel)
        self.frameHistory.setFrameShadow(QFrame.Raised)
        self.lblHistory = QLabel(self.frameHistory)
        self.lblHistory.setObjectName(u"lblHistory")
        self.lblHistory.setGeometry(QRect(10, 10, 91, 28))
        self.lblHistory.setFont(font7)
        self.lblHistory.setStyleSheet(u"color: rgb(88, 150, 250);\n"
" border-top: 0px solid blue; \n"
" border-left: 0px solid blue; \n"
" border-right: 0px solid blue; \n"
" border-bottom: 0px solid blue; ")
        self.listwidgethistory = QListWidget(self.frameHistory)
        self.listwidgethistory.setObjectName(u"listwidgethistory")
        self.listwidgethistory.setGeometry(QRect(10, 40, 131, 431))
        self.listwidgethistory.setStyleSheet(u"color: rgb(255, 0, 0);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.frmCompanyFormular.raise_()
        self.frmDashboard.raise_()
        self.frameup.raise_()
        self.frameleft.raise_()
        self.btn_minimize.raise_()
        self.btn_maximize.raise_()
        self.btn_close.raise_()
        self.frametop.raise_()
        self.framdown.raise_()
        self.frmFormular.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnDashboard.setText(QCoreApplication.translate("MainWindow", u"Dashboard ", None))
        self.btnFormular.setText(QCoreApplication.translate("MainWindow", u"Formular    ", None))
        self.btnStocks.setText(QCoreApplication.translate("MainWindow", u"Stocks         ", None))
        self.btnCompanyFormular.setText(QCoreApplication.translate("MainWindow", u"Company   ", None))
        self.btnForex.setText(QCoreApplication.translate("MainWindow", u"Forex          ", None))
        self.btnFutures.setText(QCoreApplication.translate("MainWindow", u"Futures       ", None))
        self.btnCrypto.setText(QCoreApplication.translate("MainWindow", u"Crypto       ", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings     ", None))
        self.btnVersion.setText(QCoreApplication.translate("MainWindow", u"Version         ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"frmDashboard", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"lblcompany", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Account_991050", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"3000", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
        self.lblcapitalmanager.setText(QCoreApplication.translate("MainWindow", u"Capital Manager", None))
        self.lblname.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.lblAccount2.setText(QCoreApplication.translate("MainWindow", u"Account 2", None))
        self.lblAccount3.setText(QCoreApplication.translate("MainWindow", u"Account 3", None))
        self.lblAccount1.setText(QCoreApplication.translate("MainWindow", u"Account 1", None))
        self.lblTotal.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.lblMainAccount.setText(QCoreApplication.translate("MainWindow", u"Main Account", None))
        self.lblAccount4.setText(QCoreApplication.translate("MainWindow", u"Account 4", None))
        self.pbMainAccount.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.btnSend_2.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.lblAccountStatistic.setText(QCoreApplication.translate("MainWindow", u"General Overview", None))
        self.btnSpend.setText(QCoreApplication.translate("MainWindow", u"Spend", None))
        self.cbspendmoney.setItemText(0, QCoreApplication.translate("MainWindow", u"Main Account", None))
        self.cbspendmoney.setItemText(1, QCoreApplication.translate("MainWindow", u"Account 1", None))
        self.cbspendmoney.setItemText(2, QCoreApplication.translate("MainWindow", u"Account 2", None))
        self.cbspendmoney.setItemText(3, QCoreApplication.translate("MainWindow", u"Account 3", None))
        self.cbspendmoney.setItemText(4, QCoreApplication.translate("MainWindow", u"Account 4", None))

        self.cbspendmoney.setCurrentText(QCoreApplication.translate("MainWindow", u"Main Account", None))
        self.lespend.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.lblSpendMoney.setText(QCoreApplication.translate("MainWindow", u"Spend Money", None))
        self.lblSpendMoney_2.setText(QCoreApplication.translate("MainWindow", u"Spend Money", None))
        self.pbSpendMoney.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.pbSpendMoneyEuro.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.lblHistory.setText(QCoreApplication.translate("MainWindow", u"History", None))
    # retranslateUi

