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
        self.label.setGeometry(QtCore.QRect(70, 58, 481, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 139, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.YES1 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES1.setGeometry(QtCore.QRect(200, 109, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES1.setFont(font)
        self.YES1.setStyleSheet("color: rgb(255, 255, 255);")
        self.YES1.setObjectName("YES1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.YES1)
        self.NO1 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO1.setGeometry(QtCore.QRect(250, 109, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO1.setFont(font)
        self.NO1.setStyleSheet("color: rgb(255, 255, 255);")
        self.NO1.setObjectName("NO1")
        self.buttonGroup.addButton(self.NO1)
        self.NO2 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO2.setGeometry(QtCore.QRect(250, 189, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO2.setFont(font)
        self.NO2.setStyleSheet("color: rgb(255, 255, 255);")
        self.NO2.setObjectName("NO2")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.NO2)
        self.YES2 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES2.setGeometry(QtCore.QRect(200, 189, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES2.setFont(font)
        self.YES2.setStyleSheet("color: rgb(255, 255, 255);")
        self.YES2.setObjectName("YES2")
        self.buttonGroup_2.addButton(self.YES2)
        self.NO3 = QtWidgets.QRadioButton(self.centralwidget)
        self.NO3.setGeometry(QtCore.QRect(250, 249, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NO3.setFont(font)
        self.NO3.setStyleSheet("color: rgb(255, 255, 255);")
        self.NO3.setObjectName("NO3")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.NO3)
        self.YES3 = QtWidgets.QRadioButton(self.centralwidget)
        self.YES3.setGeometry(QtCore.QRect(200, 249, 41, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.YES3.setFont(font)
        self.YES3.setStyleSheet("color: rgb(255, 255, 255);")
        self.YES3.setObjectName("YES3")
        self.buttonGroup_3.addButton(self.YES3)
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
        self.label_11.setGeometry(QtCore.QRect(40, 209, 481, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 79, 481, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 160, 491, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
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
        self.pushButton.clicked.connect(self.last)
        self.pushButton_2.clicked.connect(self.close)
        self.YES1.toggled.connect(self.yes1)
        self.YES2.toggled.connect(self.yes2)
        self.YES3.toggled.connect(self.yes3)
        self.NO1.toggled.connect(self.no1)
        self.NO2.toggled.connect(self.no2)
        self.NO3.toggled.connect(self.no3)


    def yes1(self):
        global neitral
        neitral = neitral + 1
        self.NO1.setEnabled(False)

    def yes2(self):
        global extra
        extra = extra + 1
        self.NO2.setEnabled(False)

    def yes3(self):
        global neitral
        neitral = neitral + 1
        self.NO3.setEnabled(False)









    def no1(self):
        self.YES1.setEnabled(False)

    def no2(self):
        self.YES2.setEnabled(False)

    def no3(self):
        self.YES3.setEnabled(False)






    def last(self):
        file_1.write(str(znak))
        file_1.write(str(extra))
        file_2.write(str(znak))
        file_2.write(str(neitral))
        file_3.write(str(znak))
        file_3.write(str(false))
        os.startfile("itog.py")
        sys.exit()


    def close(self):
        f.truncate(0)
        g.truncate(0)
        h.truncate(0)
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Часть 10"))
        self.label.setText(_translate("MainWindow", "Часто ли вы чувствуете себя неловко в обществе "))
        self.label_7.setText(_translate("MainWindow", "Когда обстоятельства против вас, обычно вы думаете"))
        self.YES1.setText(_translate("MainWindow", "ДА"))
        self.NO1.setText(_translate("MainWindow", "НЕТ"))
        self.NO2.setText(_translate("MainWindow", "НЕТ"))
        self.YES2.setText(_translate("MainWindow", "ДА"))
        self.NO3.setText(_translate("MainWindow", "НЕТ"))
        self.YES3.setText(_translate("MainWindow", "ДА"))
        self.pushButton.setText(_translate("MainWindow", "ЗАВЕРШИТЬ"))
        self.pushButton_2.setText(_translate("MainWindow", "ОТМЕНА"))
        self.label_11.setText(_translate("MainWindow", "Часто ли у вас сосет под ложечкой перед важным делом?"))
        self.label_2.setText(_translate("MainWindow", " людей выше вас по положению?"))
        self.label_8.setText(_translate("MainWindow", "тем не менее, что стоит еще что-либо предпринять?"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())