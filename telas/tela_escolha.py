# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\gabri\OneDrive\Área de Trabalho\progamas_atual\python\P.O.O2\P.O.O2 TRABALHO\tela_escolha.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_escolha(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 90, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.voltar_escolha = QtWidgets.QPushButton(self.centralwidget)
        self.voltar_escolha.setGeometry(QtCore.QRect(0, 540, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.voltar_escolha.setFont(font)
        self.voltar_escolha.setObjectName("voltar_escolha")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(200, 220, 351, 107))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.prestador_de_servicos = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.prestador_de_servicos.setFont(font)
        self.prestador_de_servicos.setObjectName("prestador_de_servicos")
        self.verticalLayout.addWidget(self.prestador_de_servicos)
        self.cliente_escolha = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.cliente_escolha.setFont(font)
        self.cliente_escolha.setObjectName("cliente_escolha")
        self.verticalLayout.addWidget(self.cliente_escolha)
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
        self.label.setText(_translate("MainWindow", "Deseja cadastrar no sistema como?"))
        self.voltar_escolha.setText(_translate("MainWindow", "voltar"))
        self.prestador_de_servicos.setText(_translate("MainWindow", "Prestador de serviço"))
        self.cliente_escolha.setText(_translate("MainWindow", "Cliente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_escolha()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
