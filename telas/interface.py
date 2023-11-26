import sys
import mysql.connector as mysql
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QListView
from PyQt5.QtCore import QStringListModel, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import socket
import pickle

from tela_inicial import Tela_inicial
from tela_login import Tela_Login
from tela_cadastro_servicos import Tela_cadastro_servicos
# from tela_buscar import Tela_Buscar
# from tela_cadastro import Tela_Cadastro 
from cadastro_cliente import Tela_cadastro_cliente
from tela_cliente import Tela_cliente
from tela_prestador_servico import Tela_prestador_servico
from tela_escolha_servico import Tela_escolha_servico
from alterar_dados_cliente import Alterar_dados_cliente
from altera_dados_prestador_serviços import *
from ver_pedidos import Ver_pedidos

        
ip =  'localhost'
port = 8007
addr = ((ip,port))
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(addr)


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()


        self.tela_inicial = Tela_inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro_servico = Tela_cadastro_servicos()
        self.tela_cadastro_servico.setupUi(self.stack1)

        self.tela_cadastro_cliente = Tela_cadastro_cliente()
        self.tela_cadastro_cliente.setupUi(self.stack2)

        self.tela_cliente = Tela_cliente()
        self.tela_cliente.setupUi(self.stack3)

        self.tela_prestador_servico = Tela_prestador_servico()
        self.tela_prestador_servico.setupUi(self.stack4)

        self.tela_escolha_servico = Tela_escolha_servico()
        self.tela_escolha_servico.setupUi(self.stack5)

        self.alterar_dados_cliente = Alterar_dados_cliente()
        self.alterar_dados_cliente.setupUi(self.stack6)

        self.altera_dados_prestador_serviços = altera_dados_prestador_serviços()
        self.altera_dados_prestador_serviços.setupUi(self.stack7)
        
        self.ver_pedidos = Ver_pedidos()
        self.ver_pedidos.setupUi(self.stack8)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        

class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)
        
        #TELA_INICIAL
        self.tela_inicial.LOGIN_USUARIO.clicked.connect(self.botao_login)
        self.tela_inicial.SAIR.clicked.connect(self.sair)
        self.tela_inicial.CLIENTE_CADASTRAR.clicked.connect(self.abrirTelaCadastro_Cliente)
        self.tela_inicial.PRESTADOR_CADASTRAR.clicked.connect(self.abirtelaCadastro_Servico)
        
        
        #TELA_CADASTRO_SERVICO
        self.tela_cadastro_servico.VOLTAR_SERVICO_CADASTRO.clicked.connect(self.botaoVoltar_inicio)
        self.tela_cadastro_servico.CONFIRM_CADASTRO_SERVICO.clicked.connect(self.botaoCadastra_servico)
        
        
        #TELA_CADASTRO_CLIENTE
        self.tela_cadastro_cliente.pushButton_2.clicked.connect(self.botaoVoltar_inicio)        
        self.tela_cadastro_cliente.pushButton.clicked.connect(self.botaoCadastra_cliente)

        
        #TELA_CLIENTE
        self.tela_cliente.pushButton.clicked.connect(self.botaoalterar_dados_cliente)
        self.tela_cliente.pushButton_2.clicked.connect(self.abrirTelaesolhar_servico)
        self.tela_cliente.pushButton_3.clicked.connect(self.botao_apagar_conta)
        self.tela_cliente.pushButton_4.clicked.connect(self.botaoVoltar_inicio)

        # TELA ALTERAR DADOS CLIENTE (BOTAS VOLTAR)
        self.alterar_dados_cliente.pushButton_2.clicked.connect(self.botaoVolta_cliente)
        self.alterar_dados_cliente.pushButton.clicked.connect(self.alterar_dados_cliente_banco)
        
        
        #TELA_PRESTADOR_SERVIÇO
        self.tela_prestador_servico.pushButton.clicked.connect(self.botao_alterar_dados_prestador)
        self.tela_prestador_servico.pushButton_3.clicked.connect(self.botao_apagar_conta)
        self.tela_prestador_servico.pushButton_4.clicked.connect(self.botaoVoltar_inicio)
        self.tela_prestador_servico.pushButton_6.clicked.connect(self.Abrir_pedidos)

        # TELA ALTERAR DADOS SERVICO(BOTAO VOLTAR)
        self.altera_dados_prestador_serviços.pushButton.clicked.connect(self.botaoVolta_prestador)
        self.altera_dados_prestador_serviços.pushButton_2.clicked.connect(self.alterar_dados_prestador_banco)

        # self.tela_prestador_servico.pushButton_5.clicked.connect(self.botao_limpar)
        # self.tela_prestador_servico.pushButton_6.clicked.connect(self.botao_Ver_serviços)

        #TELA_ESCOLHA_SERVICO
        self.tela_escolha_servico.pushButton_2.clicked.connect(self.botaoVolta_cliente)
        
        #TLE_VER_PEDIDOS
        self.ver_pedidos.pushButton.clicked.connect(self.botaoVolta_prestador)
        
        self.verifica = False

    #####CADASTRO#####
    def botaoCadastra_cliente(self):
        nome = self.tela_cadastro_cliente.lineEdit_5.text()
        senha = self.tela_cadastro_cliente.lineEdit.text()
        endereco = self.tela_cadastro_cliente.lineEdit_2.text()
        cpf_C = self.tela_cadastro_cliente.lineEdit_3.text()
        nascimento = self.tela_cadastro_cliente.lineEdit_4.text()
        if not(nome == '' or senha == '' or endereco == '' or cpf_C == '' or nascimento == ''):
            menssagem =  f'cadastro_U,{nome},{senha},{endereco},{cpf_C},{nascimento}'
            cliente_socket.send(menssagem.encode())
            recebida = cliente_socket.recv(1024).decode()
            print(recebida)
            if (recebida == "T"):
                QMessageBox.information(None,'POOII', 'Cadastro realizado com sucesso!')
            else:
                QMessageBox.information(None,'POOII', 'O CPF informado já está cadastrado na base de dados!')
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
        self.tela_cadastro_cliente.lineEdit.setText('')
        self.tela_cadastro_cliente.lineEdit_2.setText('')
        self.tela_cadastro_cliente.lineEdit_3.setText('')
        self.tela_cadastro_cliente.lineEdit_4.setText('')
        self.tela_cadastro_cliente.lineEdit_5.setText('')
        self.QtStack.setCurrentIndex(0)

    def botaoCadastra_servico(self):
        
        Nome = self.tela_cadastro_servico.NOME_cadastro_servico_2.text()
        Senha = self.tela_cadastro_servico.ESPECIALIZACAO_cadastro_servico_2.text()
        local = self.tela_cadastro_servico.LOCAL_cadastro_servico.text()
        cpf = self.tela_cadastro_servico.CPF_cadastro_servico.text()
        especializacao = self.tela_cadastro_servico.ESPECIALIZACAO_cadastro_servico.text()
        area = self.tela_cadastro_servico.AREA_cadastro_servico.text()
        
        if not(Nome == '' or Senha == '' or local == '' or cpf == '' or especializacao == '' or area == ''):
            menssagem =  f'cadastro_S,{Nome},{Senha},{local},{cpf},{especializacao},{area}'
            cliente_socket.send(menssagem.encode())
            recebida = cliente_socket.recv(1024).decode()
            
            if (recebida == "T"):
                QMessageBox.information(None,'POOII', 'Cadastro realizado com sucesso!')
            else:
                QMessageBox.information(None,'POOII', 'Dados ja utilizados!')
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')

        self.tela_cadastro_servico.NOME_cadastro_servico_2.setText('')
        self.tela_cadastro_servico.ESPECIALIZACAO_cadastro_servico_2.setText('')
        self.tela_cadastro_servico.LOCAL_cadastro_servico.setText('')
        self.tela_cadastro_servico.CPF_cadastro_servico.setText('')
        self.tela_cadastro_servico.ESPECIALIZACAO_cadastro_servico.setText('')
        self.tela_cadastro_servico.AREA_cadastro_servico.setText('')
        self.QtStack.setCurrentIndex(0)



    ##########################

    def botao_login(self):

        CPF = self.tela_inicial.CPF_LOGIN.text()
        SENHA = self.tela_inicial.SENHA_LOGIN.text()

        if not(CPF == '' or SENHA == ''):
            menssagem =  f'Login,{SENHA},{CPF}'
            cliente_socket.send(menssagem.encode())
            recebida = cliente_socket.recv(1024).decode()
            comando = recebida[1:-1].split(",")
            comando = [item.strip() for item in comando]
            for i in range(len(comando)):
                try:
                    comando[i] = eval(comando[i])
                except:
                    pass
                
            Nome,caso_existe,self.verifica = comando[0],comando[1],comando[2]
            if(caso_existe == "T"):
                QMessageBox.information(None,'POOII', 'Login realizado com sucesso!')   
                if(self.verifica=="T"):
                    self.QtStack.setCurrentIndex(4)
                    self.tela_prestador_servico.label_4.setText(f'logado como {Nome}')

                else:
                    self.QtStack.setCurrentIndex(3)
                    self.tela_cliente.label_4.setText(f'logado como {Nome} ')

            else:
                QMessageBox.information(None,'POOII', 'Conta não encontrada!')                
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')

        self.tela_inicial.CPF_LOGIN.setText('')
        self.tela_inicial.SENHA_LOGIN.setText('')

    def botaoalterar_dados(self):
        pass
    
    def botao_apagar_conta(self):
        menssagem =  'Apagar'
        cliente_socket.send(menssagem.encode())
        self.QtStack.setCurrentIndex(0)

    def botao_buscar_servico(self):
        pass    
            
    def botaoVoltar_inicio(self):
        self.QtStack.setCurrentIndex(0)
        self.verifica = False

    def abirtelaCadastro_Servico(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaCadastro_Cliente(self):
        self.QtStack.setCurrentIndex(2)

    def botaoVolta_cliente(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaesolhar_servico(self):
        
        mensagem = "escolha"
        cliente_socket.send(mensagem.encode())
        
        recebida = cliente_socket.recv(1024)
        received_data = pickle.loads(recebida)
        listview = self.tela_escolha_servico.listView
        listview.clicked.connect(self.item_clicado)
        self.popular_lista(received_data)
        self.QtStack.setCurrentIndex(5)


    def popular_lista(self, received_data):
        listview = self.tela_escolha_servico.listView
        model = QStandardItemModel()
        listview.setModel(model)
        #software carpentry
        for row, servico in enumerate(received_data):
            cpf = servico[4]
            senha = servico[2]
            dados_servico = f"Nome: {servico[1]}  Local: {servico[3]}  Especialização: {servico[5]}  Área: {servico[6]}"

            item = QStandardItem(dados_servico)

            item.setData(cpf, Qt.UserRole + 1)
            item.setData(senha, Qt.UserRole + 2)


            model.setItem(row, 0, item)

        listview.clicked.connect(self.item_clicado)

    def item_clicado(self,index):
        if index.isValid():
            item = index.model().itemFromIndex(index)

            cpf = item.data(Qt.UserRole + 1)
            senha = item.data(Qt.UserRole + 2)
            mensagem = f"busca,{cpf},{senha}"
            cliente_socket.send(mensagem.encode())

            print(f"CPF clicado: {cpf} senha: {senha}")
            
            
    def botaoalterar_dados_cliente(self):
        self.QtStack.setCurrentIndex(6)
        
    def botaoVolta_cliente(self):
        self.QtStack.setCurrentIndex(3)

    def botaoVolta_prestador(self):
        self.QtStack.setCurrentIndex(4)

    def botao_alterar_dados_cliente(self):
        self.QtStack.setCurrentIndex(5)

    def botao_alterar_dados_prestador(self):
        self.QtStack.setCurrentIndex(7)
        
    def Abrir_pedidos(self):
        self.QtStack.setCurrentIndex(8)
        
    def alterar_dados_cliente_banco(self):
        
        novo_nome = self.alterar_dados_cliente.lineEdit.text()
        nova_senha = self.alterar_dados_cliente.lineEdit_2.text()
        novo_endereco = self.alterar_dados_cliente.lineEdit_3.text()
        novo_cpf = self.alterar_dados_cliente.lineEdit_4.text()
        nova_nascimento = self.alterar_dados_cliente.lineEdit_5.text()
        if not(novo_nome == '' or nova_senha == '' or novo_endereco == '' or novo_cpf == '' or nova_nascimento == ''): 
            menssagem =  f'alterar_U,{novo_nome},{nova_senha},{novo_endereco},{novo_cpf},{nova_nascimento}'
            cliente_socket.send(menssagem.encode())
            recebida = cliente_socket.recv(1024).decode()
            
            if recebida == "T":
                QMessageBox.information(None, 'POOII', 'Dados do cliente alterados com sucesso!')
            else:
                QMessageBox.information(None, 'POOII', 'Falha ao alterar os dados!!')
            self.alterar_dados_cliente.lineEdit.setText('')
            self.alterar_dados_cliente.lineEdit_2.setText('')
            self.alterar_dados_cliente.lineEdit_3.setText('')
            self.alterar_dados_cliente.lineEdit_4.setText('')
            self.alterar_dados_cliente.lineEdit_5.setText('')
            self.verifica = False
            self.QtStack.setCurrentIndex(0)



    def alterar_dados_prestador_banco(self):
 
        novo_nome = self.altera_dados_prestador_serviços.lineEdit.text()
        nova_senha = self.altera_dados_prestador_serviços.lineEdit_2.text()
        novo_local = self.altera_dados_prestador_serviços.lineEdit_3.text()
        novo_cpf = self.altera_dados_prestador_serviços.lineEdit_4.text()
        nova_especializacao = self.altera_dados_prestador_serviços.lineEdit_5.text()
        nova_area = self.altera_dados_prestador_serviços.lineEdit_6.text()
        if not(novo_nome == '' or nova_senha == '' or novo_local == '' or novo_cpf == '' or nova_especializacao == '' or nova_area == ''): 
            menssagem =  f'alterar_S,{novo_nome},{nova_senha},{novo_local},{novo_cpf},{nova_especializacao},{nova_area}'
            cliente_socket.send(menssagem.encode())
            recebida = cliente_socket.recv(1024).decode()
            if recebida == "T":
                QMessageBox.information(None, 'POOII', 'Dados alterados com sucesso!')
            else:
                QMessageBox.information(None, 'POOII', 'Falha ao alterar os dados!!')
                
            self.altera_dados_prestador_serviços.lineEdit.setText('')
            self.altera_dados_prestador_serviços.lineEdit_2.setText('')
            self.altera_dados_prestador_serviços.lineEdit_3.setText('')
            self.altera_dados_prestador_serviços.lineEdit_4.setText('')
            self.altera_dados_prestador_serviços.lineEdit_5.setText('')
            self.altera_dados_prestador_serviços.lineEdit_6.setText('')
            self.verifica = False
            self.QtStack.setCurrentIndex(0)



    def sair(self):
        mensagem = "bye"
        cliente_socket.send(mensagem.encode())
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())