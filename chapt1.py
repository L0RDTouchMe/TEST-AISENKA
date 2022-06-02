
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
file_1 = open("extra.txt", "a")
file_2 = open("neitral.txt", "a")
file_3 = open("false.txt", "a")
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
        MainWindow.setStyleSheet("background-color: rgb(95, 94, 123);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 81, 511, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 231, 481, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 321, 511, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 101, 491, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.YES1 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES1.setGeometry(QtCore.QRect(200, 50, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES1.setFont(font)
        self.YES1.setObjectName("YES1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.YES1)
        self.NO1 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO1.setGeometry(QtCore.QRect(250, 50, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO1.setFont(font)
        self.NO1.setObjectName("NO1")
        self.buttonGroup.addButton(self.NO1)
        self.NO2 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO2.setGeometry(QtCore.QRect(250, 130, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO2.setFont(font)
        self.NO2.setObjectName("NO2")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.NO2)
        self.YES2 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES2.setGeometry(QtCore.QRect(200, 130, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES2.setFont(font)
        self.YES2.setObjectName("YES2")
        self.buttonGroup_2.addButton(self.YES2)
        self.NO3 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO3.setGeometry(QtCore.QRect(250, 200, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO3.setFont(font)
        self.NO3.setObjectName("NO3")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.NO3)
        self.YES3 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES3.setGeometry(QtCore.QRect(200, 200, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES3.setFont(font)
        self.YES3.setObjectName("YES3")
        self.buttonGroup_3.addButton(self.YES3)
        self.NO4 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO4.setGeometry(QtCore.QRect(250, 280, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO4.setFont(font)
        self.NO4.setObjectName("NO4")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.NO4)
        self.YES4 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES4.setGeometry(QtCore.QRect(200, 280, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES4.setFont(font)
        self.YES4.setObjectName("YES4")
        self.buttonGroup_4.addButton(self.YES4)
        self.NO5 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO5.setGeometry(QtCore.QRect(250, 360, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO5.setFont(font)
        self.NO5.setObjectName("NO5")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.NO5)
        self.YES5 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES5.setGeometry(QtCore.QRect(200, 360, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES5.setFont(font)
        self.YES5.setObjectName("YES5")
        self.buttonGroup_5.addButton(self.YES5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 250, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 341, 511, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 400, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 421, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.NO6 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO6.setGeometry(QtCore.QRect(250, 440, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO6.setFont(font)
        self.NO6.setObjectName("NO6")
        self.buttonGroup_6 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.buttonGroup_6.addButton(self.NO6)
        self.YES6 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES6.setGeometry(QtCore.QRect(200, 440, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES6.setFont(font)
        self.YES6.setObjectName("YES6")
        self.buttonGroup_6.addButton(self.YES6)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 490, 75, 41))
        self.pushButton.setStyleSheet("background-color: rgb(73, 89, 123);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 490, 75, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(73, 89, 123);")
        self.pushButton_2.setObjectName("pushButton_2")
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
        extra = extra+1
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
        global false
        false = false + 1
        self.NO6.setEnabled(False)









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
        self.YES6.setEnabled(False)






    def last(self):
        os.startfile("chapt2.py")
        file_1.write(str(extra))
        file_2.write(str(neitral))
        file_3.write(str(false))
        sys.exit()
    def close(self):
        f.truncate(0)
        g.truncate(0)
        h.truncate(0)
        sys.exit()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Часть 1"))
        self.label.setText(_translate("MainWindow", "Нравится ли вам оживление и суета вокруг вас?"))
        self.label_2.setText(_translate("MainWindow", "Часто ли у вас бывает беспокойное чувство,"))
        self.label_3.setText(_translate("MainWindow", "Чувствуете ли вы себя иногда счастливым,"))
        self.label_4.setText(_translate("MainWindow", "Вы из тех людей, которые не лезут за словом в карман?"))
        self.label_5.setText(_translate("MainWindow", "Держитесь ли вы обычно в тени на вечеринках"))
        self.label_7.setText(_translate("MainWindow", " что вам что-нибудь хочется, а вы не знаете что?"))
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
        self.label_6.setText(_translate("MainWindow", " а иногда печальным без какой-либо причины?"))
        self.label_8.setText(_translate("MainWindow", "или в компании?"))
        self.label_9.setText(_translate("MainWindow", "Всегда ли в детстве вы делали немедленно"))
        self.label_10.setText(_translate("MainWindow", " и безропотно то, что вам приказывали?"))
        self.NO6.setText(_translate("MainWindow", "НЕТ"))
        self.YES6.setText(_translate("MainWindow", "ДА"))
        self.pushButton.setText(_translate("MainWindow", "ДАЛЕЕ"))
        self.pushButton_2.setText(_translate("MainWindow", "ОТМЕНА"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
