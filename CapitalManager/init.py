import datetime
import json
import sys

from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QListWidgetItem, QGraphicsDropShadowEffect, QApplication
from yahoo_fin import stock_info as si
from ui_main import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen
from StocksGraph import get_data

counter = 0
Accounts = []


# Main Window
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    netsalary = 0
    Account1 = 0
    Account2 = 0
    Account3 = 0
    Account4 = 0
    currencycounter = 0
    euroboolean = 0

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ReadConfig()
        self.ui.btnDashboard.clicked.connect(self.btnDashboard_Clicked)
        self.btnDashboard_Clicked()
        self.ui.btnFormular.clicked.connect(self.btnFormular_Clicked)
        self.ui.btnSettings.clicked.connect(self.btnSettings_Clicked)
        self.ui.btnCompanyFormular.clicked.connect(self.btnCompanyFormular_Clicked)
        self.ui.btnSend.clicked.connect(self.btnSend_Clicked)
        self.ui.btnSend_2.clicked.connect(self.btnSend_2_Clicked)
        self.ui.btnSpend.clicked.connect(self.btnSpend_Clicked)
        self.ui.btn_close.clicked.connect(self.btnClose)
        self.ui.btn_maximize.clicked.connect(self.btnMaximize)
        self.ui.btn_minimize.clicked.connect(self.btnMinimize)
        self.ui.cbspendmoney.currentIndexChanged.connect(self.cbspendmoneychanged)
        self.ui.btnCurrency.clicked.connect(self.btncurrencyclicked)
        self.ui.lbldate.setText(datetime.datetime.today().strftime('%d-%b-%Y'))
        self.ui.btnGetStock.clicked.connect(self.btngetstock)
        self.ui.btnStocks.clicked.connect(self.btnStocks_Clicked)

    def GetStock(self):
        stockprice = si.get_live_price(self.ui.lblstockname.text())
        stockprice = format(stockprice, '.2f')
        self.ui.lblpricestocks_2.setText(str(stockprice) + " €")

    def btngetstock(self):
        self.GetStock()
        #get_data("TKA.DE")

    def btncurrencyclicked(self):
        if (MainWindow.currencycounter % 2 == 1):
            self.ui.btnCurrency.setStyleSheet(u"QPushButton {\n"
                                              "	border: none;\n"
                                              "	border-radius: 6px;		\n"
                                              "	background-color: rgb(0, 150, 240);\n"
                                              "}\n"
                                              "QPushButton:hover {		\n"
                                              "		background-color: rgb(0, 200, 255);\n"
                                              "}")
            self.ui.lblcurrency.setText("%")
            MainWindow.euroboolean = 0
        else:
            self.ui.btnCurrency.setStyleSheet(u"QPushButton {\n"
                                              "	border: none;\n"
                                              "	border-radius: 6px;		\n"
                                              "	background-color: rgb(200, 0, 0);\n"
                                              "}\n"
                                              "QPushButton:hover {		\n"
                                              "		background-color: rgb(255, 0,0);\n"
                                              "}")
            self.ui.lblcurrency.setText("€")
            MainWindow.euroboolean = 1
        MainWindow.currencycounter += 1

    def addItems(self, item):
        self.ui.listwidgethistory.addItem(item)

    def cbspendmoneychanged(self):
        if self.ui.cbspendmoney.currentText() == "Account 1":
            self.ui.pbSpendMoney.setValue((MainWindow.Account1 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account1) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account1 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        elif self.ui.cbspendmoney.currentText() == "Account 2":
            self.ui.pbSpendMoney.setValue((MainWindow.Account2 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account2) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account2 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        elif self.ui.cbspendmoney.currentText() == "Account 3":
            self.ui.pbSpendMoney.setValue((MainWindow.Account3 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account3) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account3 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        elif self.ui.cbspendmoney.currentText() == "Account 4":
            self.ui.pbSpendMoney.setValue((MainWindow.Account4 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account4) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account4 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        else:
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.netsalary) + " €")
            self.ui.pbSpendMoney.setValue((MainWindow.netsalary) /
                                          (
                                                  MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4) * 100)
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.netsalary / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)

    def btnClose(self):
        sys.exit(app.exec_())

    def btnMaximize(self):
        # self.showMaximized()
        print("max")

    def btnMinimize(self):
        self.showMinimized()

    def SaveConfig(self):
        config = {'key1': f'{MainWindow.netsalary}', 'key2': f'{MainWindow.Account1}', 'key3': f'{MainWindow.Account2}',
                  'key4': f'{MainWindow.Account3}', 'key5': f'{MainWindow.Account4}'}
        with open('config.json', 'w') as f:
            json.dump(config, f)

    def ReadConfig(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
        MainWindow.netsalary = float(config['key1'])
        MainWindow.Account1 = float(config['key2'])
        MainWindow.Account2 = float(config['key3'])
        MainWindow.Account3 = float(config['key4'])
        MainWindow.Account4 = float(config['key5'])

    def btnDashboard_Clicked(self):
        self.ui.frmDashboard.raise_()
        a1 = MainWindow.Account1 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)
        a2 = MainWindow.Account2 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)
        a3 = MainWindow.Account3 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)
        a4 = MainWindow.Account4 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)
        a5 = 0
        self.ui.frameQuickOverview.setStyleSheet(u"QFrame{\n"
                                                 "	border-radius: 65px;	\n"
                                                 f"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{0} rgba(0, 255,0, 255),stop:{a1} rgba(0, 255,0, 255) ,stop:{a1 + 0.001} rgba(0, 0, 255, 255),stop:{a1 + a2} rgba(0, 0, 255, 255), stop:{a1 + a2 + 0.001} rgba(255, 0, 0, 255), stop:{a1 + a2 + a3} rgba(255, 0, 0, 255), stop:{a1 + a2 + a3 + 0.001} rgba(150, 10, 250, 255));\n"
                                                 "\n"
                                                 " border-top: 0px solid blue; \n"
                                                 " border-left: 0px solid blue; \n"
                                                 " border-right: 0px solid blue; \n"
                                                 " border-bottom: 0px solid blue; \n"
                                                 " background-image: url(:/newPrefix/black.jpeg); \n"
                                                 "\n"
                                                 "}")
        self.ui.lblname.setText("Dashboard")
        print("btndash")

    def btnFormular_Clicked(self):
        self.ui.frmFormular.raise_()
        self.ui.lblname.setText("Formular")
        print("btnformular")

    def btnSettings_Clicked(self):
        # self.ui.framemid.raise_()
        self.ui.lblname.setText("Settings")
        print("btnsettings")

    def btnCompanyFormular_Clicked(self):
        self.ui.frmCompanyFormular.raise_()
        self.ui.lblname.setText("Company Formular")
        print("btncompanyformular")

    def btnStocks_Clicked(self):
        self.ui.frmStocks.raise_()

    def btnSend_Clicked(self):
        MainWindow.netsalary = MainWindow.netsalary + float(self.ui.lineEdit.text())
        item = QListWidgetItem()
        item.setForeground(QColor('#00ff00'))
        item.setText("Main Account: + " + self.ui.lineEdit.text())
        self.ui.listwidgethistory.addItem(item)
        print(MainWindow.netsalary)

        MainWindow.Account1 = MainWindow.Account1 + MainWindow.netsalary * 0.10;
        item1 = QListWidgetItem()
        item1.setForeground(QColor('#ff0000'))
        item1.setText("Main Account: - " + str(MainWindow.Account1))
        self.ui.listwidgethistory.addItem(item1)
        item2 = QListWidgetItem()
        item2.setForeground(QColor('#00ff00'))
        item2.setText("Account 1: + " + str(MainWindow.Account1))
        self.ui.listwidgethistory.addItem(item2)
        print(MainWindow.Account1)

        MainWindow.Account2 = MainWindow.Account2 + MainWindow.netsalary * 0.20;
        item3 = QListWidgetItem()
        item3.setForeground(QColor('#ff0000'))
        item3.setText("Main Account: - " + str(MainWindow.Account2))
        self.ui.listwidgethistory.addItem(item3)
        item3 = QListWidgetItem()
        item3.setForeground(QColor('#00ff00'))
        item3.setText("Account 2: + " + str(MainWindow.Account2))
        self.ui.listwidgethistory.addItem(item3)
        print(MainWindow.Account2)

        MainWindow.Account3 = MainWindow.Account3 + MainWindow.netsalary * 0.15;
        item4 = QListWidgetItem()
        item4.setForeground(QColor('#ff0000'))
        item4.setText("Main Account: - " + str(MainWindow.Account3))
        self.ui.listwidgethistory.addItem(item4)
        item5 = QListWidgetItem()
        item5.setForeground(QColor('#00ff00'))
        item5.setText("Account 3: + " + str(MainWindow.Account3))
        self.ui.listwidgethistory.addItem(item5)
        print(MainWindow.Account3)

        MainWindow.Account4 = MainWindow.Account4 + float(format(MainWindow.netsalary * 0.55, ".2f"));
        item6 = QListWidgetItem()
        item6.setForeground(QColor('#ff0000'))
        item6.setText("Main Account: - " + str(MainWindow.Account4))
        self.ui.listwidgethistory.addItem(item6)
        item7 = QListWidgetItem()
        item7.setForeground(QColor('#00ff00'))
        item7.setText("Account 4: + " + str(MainWindow.Account4))
        self.ui.listwidgethistory.addItem(item7)
        print(MainWindow.Account4)

        MainWindow.netsalary = 0
        Accounts.append(MainWindow.netsalary)
        Accounts.append(MainWindow.Account1)
        Accounts.append(MainWindow.Account2)
        Accounts.append(MainWindow.Account3)
        Accounts.append(MainWindow.Account4)
        Accounts[0] = MainWindow.netsalary
        Accounts[1] = MainWindow.Account1
        Accounts[2] = MainWindow.Account2
        Accounts[3] = MainWindow.Account3
        Accounts[4] = MainWindow.Account4
        self.ProgressBarValuesrefresh()

        self.SaveConfig()
        print("Money sent!")

    def btnSend_2_Clicked(self):
        if MainWindow.euroboolean == 1:
            self.ui.pbAccount1.setFormat(str(MainWindow.Account1) + " €")
            self.ui.pbAccount2.setFormat(str(MainWindow.Account2) + " €")
            self.ui.pbAccount3.setFormat(str(MainWindow.Account3) + " €")
            self.ui.pbAccount4.setFormat(str(MainWindow.Account4) + " €")
            self.ui.pbMainAccount.setFormat(str(MainWindow.netsalary) + " €")
            self.ui.pbTotal.setFormat(
                str(MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4) + " €")
            self.ProgressBarValuesrefresh()
        else:
            self.ui.pbAccount1.setFormat("%p%")
            self.ui.pbAccount2.setFormat("%p%")
            self.ui.pbAccount3.setFormat("%p%")
            self.ui.pbAccount4.setFormat("%p%")
            self.ui.pbMainAccount.setFormat("%p%")
            self.ui.pbTotal.setFormat("%p%")
            self.ProgressBarValuesrefresh()
        print("Get")

    def btnSpend_Clicked(self):
        print(self.ui.cbspendmoney.currentText())
        if self.ui.cbspendmoney.currentText() == "Account 1":
            MainWindow.Account1 = MainWindow.Account1 - (float(self.ui.lespend.text()))
            self.ui.pbSpendMoney.setValue((MainWindow.Account1 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account1) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account1 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.addItems("Account 1: - " + self.ui.lespend.text())
        elif self.ui.cbspendmoney.currentText() == "Account 2":
            MainWindow.Account2 = MainWindow.Account2 - (float(self.ui.lespend.text()))
            self.ui.pbSpendMoney.setValue((MainWindow.Account2 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account2) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account2 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.addItems("Account 2: - " + self.ui.lespend.text())
        elif self.ui.cbspendmoney.currentText() == "Account 3":
            MainWindow.Account3 = MainWindow.Account3 - (float(self.ui.lespend.text()))
            self.ui.pbSpendMoney.setValue((MainWindow.Account3 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account3) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account3 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.addItems("Account 3: - " + self.ui.lespend.text())
        elif self.ui.cbspendmoney.currentText() == "Account 4":
            MainWindow.Account4 = MainWindow.Account4 - (float(self.ui.lespend.text()))
            self.ui.pbSpendMoney.setValue((MainWindow.Account4 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.Account4) + " €")
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.Account4 / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.addItems("Account 4: - " + self.ui.lespend.text())
        else:
            MainWindow.netsalary = MainWindow.netsalary - (float(self.ui.lespend.text()))
            self.ui.pbSpendMoneyEuro.setFormat(str(MainWindow.netsalary) + " €")
            self.ui.pbSpendMoney.setValue(
                (MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4) /
                (MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4) * 100)
            self.ui.pbSpendMoneyEuro.setValue((MainWindow.netsalary / (
                    MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
            self.addItems("Main Account: - " + self.ui.lespend.text())
        self.SaveConfig()
        print("Spend")

    def ProgressBarValuesrefresh(self):
        self.ui.pbAccount1.setValue((MainWindow.Account1 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        self.ui.pbAccount2.setValue((MainWindow.Account2 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        self.ui.pbAccount3.setValue((MainWindow.Account3 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        self.ui.pbAccount4.setValue((MainWindow.Account4 / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        self.ui.pbMainAccount.setValue((MainWindow.netsalary / (
                MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4)) * 100)
        self.ui.pbTotal.setValue(
            (MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4) /
            (MainWindow.Account1 + MainWindow.Account2 + MainWindow.Account3 + MainWindow.Account4) * 100)


# SPLASH SCREEN
class SplashScreen(QtWidgets.QMainWindow, Ui_SplashScreen):

    def __init__(self, *args, obj=None, **kwargs):
        super(SplashScreen, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>THE</strong> FUTURE")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000,
                                 lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.ui.label_description.setText("READY TO RUMBLE")
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SplashScreen()
    window.show()
    app.exec()
