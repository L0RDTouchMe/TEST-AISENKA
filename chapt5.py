import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
file_1 = open("extra.txt", "a")
file_2 = open("neitral.txt", "a")
file_3 = open("false.txt", "a")
znak="+"
extra=0
false=0
neitral=0
f = open('extra.txt', 'r+')
g = open('false.txt', 'r+')
h = open('neitral.txt', 'r+')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 591)
        MainWindow.setMinimumSize(QtCore.QSize(540, 591))
        MainWindow.setMaximumSize(QtCore.QSize(540, 591))
        MainWindow.setStyleSheet("background-color: rgb(95, 94, 123);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 290, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.YES1 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES1.setGeometry(QtCore.QRect(200, 80, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES1.setFont(font)
        self.YES1.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.YES1.setObjectName("YES1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.YES1)
        self.NO1 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO1.setGeometry(QtCore.QRect(250, 80, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO1.setFont(font)
        self.NO1.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.NO1.setObjectName("NO1")
        self.buttonGroup.addButton(self.NO1)
        self.NO2 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO2.setGeometry(QtCore.QRect(250, 140, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO2.setFont(font)
        self.NO2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.NO2.setObjectName("NO2")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.NO2)
        self.YES2 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES2.setGeometry(QtCore.QRect(200, 140, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES2.setFont(font)
        self.YES2.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.YES2.setObjectName("YES2")
        self.buttonGroup_2.addButton(self.YES2)
        self.NO3 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO3.setGeometry(QtCore.QRect(250, 200, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO3.setFont(font)
        self.NO3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.NO3.setObjectName("NO3")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.NO3)
        self.YES3 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES3.setGeometry(QtCore.QRect(200, 200, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES3.setFont(font)
        self.YES3.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.YES3.setObjectName("YES3")
        self.buttonGroup_3.addButton(self.YES3)
        self.NO4 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO4.setGeometry(QtCore.QRect(250, 260, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO4.setFont(font)
        self.NO4.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.NO4.setObjectName("NO4")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.NO4)
        self.YES4 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES4.setGeometry(QtCore.QRect(200, 260, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES4.setFont(font)
        self.YES4.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.YES4.setObjectName("YES4")
        self.buttonGroup_4.addButton(self.YES4)
        self.NO5 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO5.setGeometry(QtCore.QRect(250, 320, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO5.setFont(font)
        self.NO5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.NO5.setObjectName("NO5")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.NO5)
        self.YES5 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES5.setGeometry(QtCore.QRect(200, 320, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES5.setFont(font)
        self.YES5.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.YES5.setObjectName("YES5")
        self.buttonGroup_5.addButton(self.YES5)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 350, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.NO6 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO6.setGeometry(QtCore.QRect(250, 400, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO6.setFont(font)
        self.NO6.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.NO6.setObjectName("NO6")
        self.buttonGroup_6 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.buttonGroup_6.addButton(self.NO6)
        self.YES6 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES6.setGeometry(QtCore.QRect(200, 397, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES6.setFont(font)
        self.YES6.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.YES6.setObjectName("YES6")
        self.buttonGroup_6.addButton(self.YES6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 490, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 490, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 170, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(50, 370, 441, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.funcional()



    def funcional(self):
        self.pushButton.clicked.connect(lambda: self.last())
        self.pushButton_2.clicked.connect(lambda: self.close())
        self.YES1.toggled.connect(self.yes1)
        self.YES2.toggled.connect(self.yes2)
        self.YES3.toggled.connect(self.yes3)
        self.YES4.toggled.connect(self.yes4)
        self.YES5.toggled.connect(self.yes5)
        self.YES6.toggled.connect(self.yes6)
        self.NO1.toggled.connect(self.no1)
        self.NO2.toggled.connect(self.no2)
        self.NO3.toggled.connect(self.no3)
        self.NO4.toggled.connect(self.no4)
        self.NO5.toggled.connect(self.no5)
        self.NO6.toggled.connect(self.no6)

    def yes1(self):
        global extra
        extra = extra + 1
        self.NO1.setEnabled(False)

    def yes2(self):
        global neitral
        neitral = neitral + 1
        self.NO2.setEnabled(False)

    def yes3(self):
        global extra
        extra = extra + 1
        self.NO3.setEnabled(False)

    def yes4(self):
        global neitral
        neitral = neitral + 1
        self.NO4.setEnabled(False)

    def yes5(self):
        self.NO5.setEnabled(False)

    def yes6(self):
        self.NO6.setEnabled(False)
#30








    def no1(self):
        self.YES1.setEnabled(False)

    def no2(self):
        self.YES2.setEnabled(False)

    def no3(self):
        self.YES3.setEnabled(False)

    def no4(self):
        self.YES4.setEnabled(False)

    def no5(self):
        global extra
        extra = extra + 1
        self.YES5.setEnabled(False)

    def no6(self):
        global false
        false = false + 1
        self.YES6.setEnabled(False)






    def last(self):
        os.startfile("chapt6.py")
        file_1.write(str(znak))
        file_1.write(str(extra))
        file_2.write(str(znak))
        file_2.write(str(neitral))
        file_3.write(str(znak))
        file_3.write(str(false))
        sys.exit()

    def close(self):
        f.truncate(0)
        g.truncate(0)
        h.truncate(0)
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Часть 5"))
        self.label.setText(_translate("MainWindow", "Часто ли вы бываете погружены в свои мысли?"))
        self.label_3.setText(_translate("MainWindow", "Часто ли вы думаете о своей работе?"))
        self.label_5.setText(_translate("MainWindow", "Очень ли вы любите вкусно поесть?"))
        self.label_7.setText(_translate("MainWindow", "Полностью ли вы свободны от всяких предрассудков?"))
        self.YES1.setText(_translate("MainWindow", "ДА"))
        self.NO1.setText(_translate("MainWindow", "НЕТ"))
        self.NO2.setText(_translate("MainWindow", "НЕТ"))
        self.YES2.setText(_translate("MainWindow", "ДА"))
        self.NO3.setText(_translate("MainWindow", "НЕТ"))
        self.YES3.setText(_translate("MainWindow", "ДА"))
        self.NO4.setText(_translate("MainWindow", "НЕТ"))
        self.YES4.setText(_translate("MainWindow", "ДА"))
        self.NO5.setText(_translate("MainWindow", "НЕТ"))
        self.YES5.setText(_translate("MainWindow", "ДА"))
        self.label_9.setText(_translate("MainWindow", "Нуждаетесь ли вы в дружески расположенном"))
        self.NO6.setText(_translate("MainWindow", "НЕТ"))
        self.YES6.setText(_translate("MainWindow", "ДА"))
        self.pushButton.setText(_translate("MainWindow", "ДАЛЕЕ"))
        self.pushButton_2.setText(_translate("MainWindow", "ОТМЕНА"))
        self.label_11.setText(_translate("MainWindow", "Нравятся ли вам первоапрельские шутки?"))
        self.label_10.setText(_translate("MainWindow", "человеке, чтобы выговориться, когда вы раздражены?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())