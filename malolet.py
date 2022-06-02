import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sborinf


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 323)
        MainWindow.setStyleSheet("background-color: rgb(95, 94, 123);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 0, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setObjectName("label_2")
        self.pushButtonyes = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonyes.setGeometry(QtCore.QRect(280, 210, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonyes.setFont(font)
        self.pushButtonyes.setStyleSheet("background-color: rgb(73, 89, 123);")
        self.pushButtonyes.setObjectName("pushButtonyes")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(73, 89, 123);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 541, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Согласие с условиями"))
        self.label.setText(_translate("MainWindow", "Подтверждение несовершеннолетия"))
        self.label_2.setText(_translate("MainWindow", "Подтверждая несовершенолетие пользователя вы удтверждаете"))
        self.pushButtonyes.setText(_translate("MainWindow", "ДА"))
        self.pushButton_2.setText(_translate("MainWindow", "НЕТ"))
        self.label_3.setText(_translate("MainWindow", "что вы проходите тест по согласию родителей или под их присмотром."))

    #функционал кнопок
        self.pushButton_2.clicked.connect(lambda: self.back1())
        self.pushButtonyes.clicked.connect(lambda: self.openwind())

    def back1(self):
        sys.exit()


    def openwind(self):
        os.startfile("chapt1.py")
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
