from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import malolet

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 332)
        MainWindow.setMinimumSize(QtCore.QSize(605, 332))
        MainWindow.setMaximumSize(QtCore.QSize(605, 332))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(95, 94, 123);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 52, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 92, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 132, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(440, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.spinBox.setObjectName("spinBox")
        self.textEditname = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditname.setGeometry(QtCore.QRect(220, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditname.setFont(font)
        self.textEditname.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEditname.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.textEditname.setObjectName("textEditname")
        self.textEditfamily = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditfamily.setGeometry(QtCore.QRect(220, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditfamily.setFont(font)
        self.textEditfamily.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEditfamily.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.textEditfamily.setObjectName("textEditfamily")
        self.textEditotchestvo = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditotchestvo.setGeometry(QtCore.QRect(220, 130, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEditotchestvo.setFont(font)
        self.textEditotchestvo.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.textEditotchestvo.setObjectName("textEditotchestvo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 210, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(73, 89, 123);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setIconSize(QtCore.QSize(512, 515))
        self.pushButton.setObjectName("pushButton")
        self.errorlabel = QtWidgets.QLabel(self.centralwidget)
        self.errorlabel.setGeometry(QtCore.QRect(160, 180, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.errorlabel.setFont(font)
        self.errorlabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.errorlabel.setText("")
        self.errorlabel.setObjectName("errorlabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.funcional()


    def funcional(self):
        self.pushButton.clicked.connect(self.button)

    def button(self):
        name = self.textEditname.toPlainText()
        family = self.textEditfamily.toPlainText()
        otchestvo = self.textEditotchestvo.toPlainText()
        age = int(self.spinBox.value())
        if name == "" or family == "" or otchestvo == "" :
            self.errorlabel.setText("Все окна обязательны для заполнения")
            print(name, family, otchestvo)

        elif name != "" or family != "" or otchestvo != "" :

            if age<18 :
                os.startfile("malolet.py")
                sys.exit()


            if age >= 18 :
                os.startfile("chapt1.py")
                sys.exit()






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Сбор персональных данных"))
        self.label.setText(_translate("MainWindow", "Введите ваше имя"))
        self.label_2.setText(_translate("MainWindow", "Введите вашу фамилию"))
        self.label_3.setText(_translate("MainWindow", "Введите ваше отчество"))
        self.label_4.setText(_translate("MainWindow", "Сколько вам полных лет"))
        self.pushButton.setText(_translate("MainWindow", "Далее"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
