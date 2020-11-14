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
        MainWindow.resize(1056, 678)
        MainWindow.setStyleSheet(u"background-color:rgb(0, 0, 0)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(1, 255, 1);")
        self.frameleft = QFrame(self.centralwidget)
        self.frameleft.setObjectName(u"frameleft")
        self.frameleft.setGeometry(QRect(0, -10, 181, 681))
        self.frameleft.setStyleSheet(u"background-color:rgb(0, 0, 0)")
        self.frameleft.setFrameShape(QFrame.StyledPanel)
        self.frameleft.setFrameShadow(QFrame.Raised)
        self.btnDashboard = QPushButton(self.frameleft)
        self.btnDashboard.setObjectName(u"btnDashboard")
        self.btnDashboard.setGeometry(QRect(40, 120, 91, 91))
        self.btnDashboard.setAutoFillBackground(False)
        self.btnDashboard.setStyleSheet(u"QPushButton {\n"
"	background-position: top left;\n"
"    border-image url(:/newPrefix/BrokenSword.ico) 1 100 0 0 stretch stretch;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/BrokenSword.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnDashboard.setIcon(icon)
        self.btnDashboard.setIconSize(QSize(90, 90))
        self.btnFormular = QPushButton(self.frameleft)
        self.btnFormular.setObjectName(u"btnFormular")
        self.btnFormular.setGeometry(QRect(40, 230, 91, 91))
        self.btnFormular.setStyleSheet(u"QPushButton {\n"
"	background-position: top left;\n"
"    border-image url(:/newPrefix/BrokenSword.ico) 1 100 0 0 stretch stretch;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}url(:/newPrefix/atom-beta.ico)")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/atom-beta.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnFormular.setIcon(icon1)
        self.btnFormular.setIconSize(QSize(90, 90))
        self.btnSettings = QPushButton(self.frameleft)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setGeometry(QRect(40, 530, 91, 91))
        self.btnSettings.setStyleSheet(u"QPushButton {\n"
"	background-position: top left;\n"
"    border-image url(:/newPrefix/setroubleshoot_icon.ico)1 100 0 0 stretch stretch;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(0,0,0)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}url(:/newPrefix/atom-beta.ico)")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/setroubleshoot_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSettings.setIcon(icon2)
        self.btnSettings.setIconSize(QSize(90, 90))
        self.lblcapitalmanager = QLabel(self.frameleft)
        self.lblcapitalmanager.setObjectName(u"lblcapitalmanager")
        self.lblcapitalmanager.setGeometry(QRect(10, 20, 171, 51))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblcapitalmanager.setFont(font)
        self.lblcapitalmanager.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.btnCompanyFormular = QPushButton(self.frameleft)
        self.btnCompanyFormular.setObjectName(u"btnCompanyFormular")
        self.btnCompanyFormular.setGeometry(QRect(40, 340, 91, 91))
        self.btnCompanyFormular.setStyleSheet(u"QPushButton {\n"
"	background-position: top left;\n"
"    border-image url(:/newPrefix/BrokenSword.ico) 1 100 0 0 stretch stretch;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}url(:/newPrefix/atom-beta.ico)")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/flare.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCompanyFormular.setIcon(icon3)
        self.btnCompanyFormular.setIconSize(QSize(90, 90))
        self.framdown = QFrame(self.centralwidget)
        self.framdown.setObjectName(u"framdown")
        self.framdown.setGeometry(QRect(0, 619, 1051, 51))
        self.framdown.setStyleSheet(u"background-color:rgb(0, 85, 55)")
        self.framdown.setFrameShape(QFrame.StyledPanel)
        self.framdown.setFrameShadow(QFrame.Raised)
        self.frmDashboard = QFrame(self.centralwidget)
        self.frmDashboard.setObjectName(u"frmDashboard")
        self.frmDashboard.setGeometry(QRect(180, 50, 871, 561))
        self.frmDashboard.setStyleSheet(u"background-color:rgb(50, 0, 0)")
        self.frmDashboard.setFrameShape(QFrame.StyledPanel)
        self.frmDashboard.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frmDashboard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 180, 281, 101))
        self.frmFormular = QFrame(self.centralwidget)
        self.frmFormular.setObjectName(u"frmFormular")
        self.frmFormular.setGeometry(QRect(180, 50, 871, 561))
        self.frmFormular.setStyleSheet(u"background-color:rgb(0,50, 0)")
        self.frmFormular.setFrameShape(QFrame.StyledPanel)
        self.frmFormular.setFrameShadow(QFrame.Raised)
        self.lblSpendMoney = QLabel(self.frmFormular)
        self.lblSpendMoney.setObjectName(u"lblSpendMoney")
        self.lblSpendMoney.setGeometry(QRect(20, 150, 151, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.lblSpendMoney.setFont(font1)
        self.lblSpendMoney.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.cbspendmoney = QComboBox(self.frmFormular)
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.addItem("")
        self.cbspendmoney.setObjectName(u"cbspendmoney")
        self.cbspendmoney.setGeometry(QRect(20, 130, 121, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.cbspendmoney.setFont(font2)
        self.cbspendmoney.setStyleSheet(u"background-color: rgb(10,10,10);\n"
"color: rgb(88, 1, 200);")
        self.cbspendmoney.setEditable(False)
        self.btnSend_2 = QPushButton(self.frmFormular)
        self.btnSend_2.setObjectName(u"btnSend_2")
        self.btnSend_2.setGeometry(QRect(780, 540, 91, 21))
        self.btnSend_2.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}")
        self.pbMainAccount = QProgressBar(self.frmFormular)
        self.pbMainAccount.setObjectName(u"pbMainAccount")
        self.pbMainAccount.setGeometry(QRect(150, 350, 431, 20))
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
        self.pbAccount2 = QProgressBar(self.frmFormular)
        self.pbAccount2.setObjectName(u"pbAccount2")
        self.pbAccount2.setGeometry(QRect(150, 410, 431, 20))
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
        self.pbAccount3 = QProgressBar(self.frmFormular)
        self.pbAccount3.setObjectName(u"pbAccount3")
        self.pbAccount3.setGeometry(QRect(150, 440, 431, 20))
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
        self.pbAccount4 = QProgressBar(self.frmFormular)
        self.pbAccount4.setObjectName(u"pbAccount4")
        self.pbAccount4.setGeometry(QRect(150, 470, 431, 20))
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
        self.pbAccount1 = QProgressBar(self.frmFormular)
        self.pbAccount1.setObjectName(u"pbAccount1")
        self.pbAccount1.setGeometry(QRect(150, 380, 431, 20))
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
        self.lblMainAccount = QLabel(self.frmFormular)
        self.lblMainAccount.setObjectName(u"lblMainAccount")
        self.lblMainAccount.setGeometry(QRect(10, 345, 121, 21))
        self.lblMainAccount.setFont(font1)
        self.lblMainAccount.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lblAccount1 = QLabel(self.frmFormular)
        self.lblAccount1.setObjectName(u"lblAccount1")
        self.lblAccount1.setGeometry(QRect(22, 380, 91, 21))
        self.lblAccount1.setFont(font1)
        self.lblAccount1.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lblAccount2 = QLabel(self.frmFormular)
        self.lblAccount2.setObjectName(u"lblAccount2")
        self.lblAccount2.setGeometry(QRect(22, 410, 91, 21))
        self.lblAccount2.setFont(font1)
        self.lblAccount2.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lblAccount4 = QLabel(self.frmFormular)
        self.lblAccount4.setObjectName(u"lblAccount4")
        self.lblAccount4.setGeometry(QRect(22, 470, 91, 21))
        self.lblAccount4.setFont(font1)
        self.lblAccount4.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lblAccount3 = QLabel(self.frmFormular)
        self.lblAccount3.setObjectName(u"lblAccount3")
        self.lblAccount3.setGeometry(QRect(22, 440, 91, 21))
        self.lblAccount3.setFont(font1)
        self.lblAccount3.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lespend = QLineEdit(self.frmFormular)
        self.lespend.setObjectName(u"lespend")
        self.lespend.setGeometry(QRect(170, 172, 141, 21))
        font3 = QFont()
        font3.setPointSize(14)
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
        self.btnSpend = QPushButton(self.frmFormular)
        self.btnSpend.setObjectName(u"btnSpend")
        self.btnSpend.setGeometry(QRect(330, 171, 91, 21))
        self.btnSpend.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}")
        self.lblTotal = QLabel(self.frmFormular)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setGeometry(QRect(20, 520, 91, 21))
        self.lblTotal.setFont(font1)
        self.lblTotal.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lblTotal.setAlignment(Qt.AlignCenter)
        self.pbTotal = QProgressBar(self.frmFormular)
        self.pbTotal.setObjectName(u"pbTotal")
        self.pbTotal.setGeometry(QRect(150, 523, 431, 20))
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
        self.frmCompanyFormular = QFrame(self.centralwidget)
        self.frmCompanyFormular.setObjectName(u"frmCompanyFormular")
        self.frmCompanyFormular.setGeometry(QRect(180, 50, 871, 561))
        self.frmCompanyFormular.setStyleSheet(u"background-color:rgb(0,0, 0)")
        self.frmCompanyFormular.setFrameShape(QFrame.StyledPanel)
        self.frmCompanyFormular.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frmCompanyFormular)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(751, 0, 120, 611))
        self.frame.setStyleSheet(u"background-color:rgb(0, 45, 0)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frmCompanyFormular)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(650, 580, 101, 31))
        self.comboBox_2 = QComboBox(self.frmCompanyFormular)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(10, 20, 171, 22))
        font4 = QFont()
        font4.setPointSize(12)
        self.comboBox_2.setFont(font4)
        self.comboBox_2.setStyleSheet(u"background-color: rgb(10,10,10);\n"
"color: rgb(88, 1, 200);")
        self.frame_2 = QFrame(self.frmCompanyFormular)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 70, 751, 491))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 45, 141, 21))
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
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 121, 81))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(18)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.btnSend = QPushButton(self.frame_2)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setGeometry(QRect(650, 470, 91, 21))
        self.btnSend.setStyleSheet(u"QPushButton{\n"
"border: 2px solid rgb(37,39,48);\n"
"border-radius: 10px;\n"
"color: #FFF;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"background-color: rgb(34,36,44);\n"
"color:rgb(0,0,255);\n"
"}")
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_3.raise_()
        self.comboBox_2.raise_()
        self.frametop = QFrame(self.centralwidget)
        self.frametop.setObjectName(u"frametop")
        self.frametop.setGeometry(QRect(180, 0, 871, 51))
        self.frametop.setStyleSheet(u"background-color:rgb(0, 40, 20)")
        self.frametop.setFrameShape(QFrame.StyledPanel)
        self.frametop.setFrameShadow(QFrame.Raised)
        self.lblname = QLabel(self.frametop)
        self.lblname.setObjectName(u"lblname")
        self.lblname.setGeometry(QRect(670, 0, 181, 51))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setWeight(50)
        self.lblname.setFont(font6)
        self.lblname.setLayoutDirection(Qt.LeftToRight)
        self.lblname.setStyleSheet(u"color: rgb(88, 1, 200);")
        self.lblname.setTextFormat(Qt.AutoText)
        self.lblname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frmDashboard.raise_()
        self.frameleft.raise_()
        self.framdown.raise_()
        self.frametop.raise_()
        self.frmCompanyFormular.raise_()
        self.frmFormular.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnDashboard.setText("")
        self.btnFormular.setText("")
        self.btnSettings.setText("")
        self.lblcapitalmanager.setText(QCoreApplication.translate("MainWindow", u"Capital Manager", None))
        self.btnCompanyFormular.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"frmDashboard", None))
        self.lblSpendMoney.setText(QCoreApplication.translate("MainWindow", u"Spend Money", None))
        self.cbspendmoney.setItemText(0, QCoreApplication.translate("MainWindow", u"Main Account", None))
        self.cbspendmoney.setItemText(1, QCoreApplication.translate("MainWindow", u"Account 1", None))
        self.cbspendmoney.setItemText(2, QCoreApplication.translate("MainWindow", u"Account 2", None))
        self.cbspendmoney.setItemText(3, QCoreApplication.translate("MainWindow", u"Account 3", None))
        self.cbspendmoney.setItemText(4, QCoreApplication.translate("MainWindow", u"Account 4", None))

        self.cbspendmoney.setCurrentText(QCoreApplication.translate("MainWindow", u"Main Account", None))
        self.btnSend_2.setText(QCoreApplication.translate("MainWindow", u"Get", None))
        self.pbMainAccount.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.lblMainAccount.setText(QCoreApplication.translate("MainWindow", u"Main Account", None))
        self.lblAccount1.setText(QCoreApplication.translate("MainWindow", u"Account 1", None))
        self.lblAccount2.setText(QCoreApplication.translate("MainWindow", u"Account 2", None))
        self.lblAccount4.setText(QCoreApplication.translate("MainWindow", u"Account 4", None))
        self.lblAccount3.setText(QCoreApplication.translate("MainWindow", u"Account 3", None))
        self.lespend.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.btnSpend.setText(QCoreApplication.translate("MainWindow", u"Spend", None))
        self.lblTotal.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"lblcompany", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Account_991050", None))

        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"3000", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.lblname.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
    # retranslateUi

