# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gabri\OneDrive\Área de Trabalho\progamas_atual\python\P.O.O2\P.O.O2 TRABALHO\tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Tela_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.digite_cpf_login = QtWidgets.QLineEdit(self.centralwidget)
        self.digite_cpf_login.setGeometry(QtCore.QRect(190, 200, 281, 41))
        self.digite_cpf_login.setText("")
        self.digite_cpf_login.setObjectName("digite_cpf_login")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.logar_login = QtWidgets.QPushButton(self.centralwidget)
        self.logar_login.setGeometry(QtCore.QRect(310, 300, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logar_login.setFont(font)
        self.logar_login.setObjectName("logar_login")
        self.voltar_login = QtWidgets.QPushButton(self.centralwidget)
        self.voltar_login.setGeometry(QtCore.QRect(0, 530, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.voltar_login.setFont(font)
        self.voltar_login.setObjectName("voltar_login")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sistema de serviços"))
        self.label_2.setText(_translate("MainWindow", "Digite seu CPF:"))
        self.logar_login.setText(_translate("MainWindow", "LOGAR"))
        self.voltar_login.setText(_translate("MainWindow", "voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
