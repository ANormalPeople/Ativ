import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QVBoxLayout, QListView
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import socket
import pickle

from tela_inicial import Tela_inicial
from tela_cadastro_servicos import Tela_cadastro_servicos
from cadastro_cliente import Tela_cadastro_cliente
from tela_cliente import Tela_cliente
from tela_prestador_servico import Tela_prestador_servico
from tela_escolha_servico import Tela_escolha_servico
from alterar_dados_cliente import Alterar_dados_cliente
from altera_dados_prestador_serviços import Altera_dados_prestador_serviços
from ver_pedidos import Ver_pedidos

class Cliente:
    
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.addr = ((ip,port))
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
    
    def conectar_servidor(self):
        """Utilizado para fazer a conexão com o servidor
        
        """
        try:
            self.cliente_socket.connect(self.addr)
            print("Conectado ao servidor.")
            self.show_main = Main(self.cliente_socket)
        except Exception as e:
            print(f"Erro ao conectar ao servidor: {e}")


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

        self.altera_dados_prestador_serviços = Altera_dados_prestador_serviços()
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
    def __init__(self,cliente_socket):
        self.cliente_socket = cliente_socket
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
        self.altera_dados_prestador_serviços.pushButton_2.clicked.connect(self.botaoVolta_prestador)
        self.altera_dados_prestador_serviços.pushButton.clicked.connect(self.alterar_dados_prestador_banco)

        # self.tela_prestador_servico.pushButton_5.clicked.connect(self.botao_limpar)
        # self.tela_prestador_servico.pushButton_6.clicked.connect(self.botao_Ver_serviços)

        #TELA_ESCOLHA_SERVICO
        self.tela_escolha_servico.pushButton_2.clicked.connect(self.botaoVolta_cliente)
        
        #TLE_VER_PEDIDOS
        self.ver_pedidos.pushButton.clicked.connect(self.botaoVolta_prestador)

    #####CADASTRO#####
    def botaoCadastra_cliente(self):
        nome = self.tela_cadastro_cliente.lineEdit_5.text()
        senha = self.tela_cadastro_cliente.lineEdit.text()
        endereco = self.tela_cadastro_cliente.lineEdit_2.text()
        cpf_C = self.tela_cadastro_cliente.lineEdit_3.text()
        nascimento = self.tela_cadastro_cliente.lineEdit_4.text()
        if not self.numero(cpf_C):
            QMessageBox.information(None,'POOII', 'CPF invalido!!')

        elif not(nome == '' or senha == '' or endereco == '' or cpf_C == '' or nascimento == ''):
            menssagem =  f'cadastro_U,{nome},{senha},{endereco},{cpf_C},{nascimento}'
            self.cliente_socket.send(menssagem.encode())
            recebida = self.cliente_socket.recv(1024).decode()
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
        
        if not self.numero(cpf):
            QMessageBox.information(None,'POOII', 'CPF invalido!!')
        
        elif not(Nome == '' or Senha == '' or local == '' or cpf == '' or especializacao == '' or area == ''):
            menssagem =  f'cadastro_S,{Nome},{Senha},{local},{cpf},{especializacao},{area}'
            self.cliente_socket.send(menssagem.encode())
            recebida = self.cliente_socket.recv(1024).decode()
            
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
            self.cliente_socket.send(menssagem.encode())
            recebida = self.cliente_socket.recv(1024).decode()
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
                    self.popular_noficiacoes()

                else:
                    print("entrou aqui")
                    self.QtStack.setCurrentIndex(3)
                    self.tela_cliente.label_4.setText(f'logado como {Nome} ')

            else:
                QMessageBox.information(None,'POOII', 'Conta não encontrada!')                
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')

        self.tela_inicial.CPF_LOGIN.setText('')
        self.tela_inicial.SENHA_LOGIN.setText('')
        self.verifica = "F" 
        
        
          
#########AREA DAS NOTIFICAÇÕES##########    
    
    def popular_noficiacoes(self):
        listview = self.tela_prestador_servico.listView
        model = QStandardItemModel()
        listview.setModel(model)
        self.tela_prestador_servico.listView.clicked.connect(self.item_clicado_notificacao)
        mensagem = "pedidos"
        self.cliente_socket.send(mensagem.encode())
        data_recebida = self.cliente_socket.recv(1024)
        if data_recebida:
            data,valida = pickle.loads(data_recebida)
        else:
            data,valida = [],[]
        i = 0
        for row, servicos in enumerate(data):
            if(valida[i] == ('F',)):
                id = servicos[0]
                data = f"Pedido recebido de {servicos[1]}"            
                item = QStandardItem(data)            
                item.setData(id, Qt.UserRole + 1)
                model.setItem(row, 0, item)
            i += 1
        

    def item_clicado_notificacao(self, index: QModelIndex):
        if index.isValid():
            reply = QMessageBox.question(self,'Alerta!',f'Deseja aceitar esse servico?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            if reply == QMessageBox.Yes:
                item = index.model().itemFromIndex(index)
                id = item.data(Qt.UserRole + 1)
                mensagem = f"modificar_validade,{id}"
                self.cliente_socket.send(mensagem.encode())
                self.popular_noficiacoes()
                # recive = cliente_socket.recv(1024).decode
                
##################################################
                
                
                
                
    def botao_apagar_conta(self):
        reply = QMessageBox.question(self,'Alerta!',f'Tem certeza que deseja apagar esta conta?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            menssagem =  'Apagar'
            self.cliente_socket.send(menssagem.encode())
            self.QtStack.setCurrentIndex(0)

    def botaoVoltar_inicio(self):
        self.QtStack.setCurrentIndex(0)
        mensagem = "reset"
        self.cliente_socket.send(mensagem.encode())

    def abirtelaCadastro_Servico(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaCadastro_Cliente(self):
        self.QtStack.setCurrentIndex(2)

    def botaoVolta_cliente(self):
        self.QtStack.setCurrentIndex(3)

    def abrirTelaesolhar_servico(self):
        mensagem = "escolha"
        self.cliente_socket.send(mensagem.encode())
        
        recebida = self.cliente_socket.recv(1024)
        received_data = pickle.loads(recebida)

        self.item_clicado_F = None

        self.tela_escolha_servico.listView_2.clicked.connect(self.armazenar_item)

        self.tela_escolha_servico.pushButton_3.clicked.connect(self.acao_botao)
        self.tela_escolha_servico.listView.clicked.connect(self.item_clicado)
        self.popular_lista(received_data)

        self.popular_lista_2()

        self.QtStack.setCurrentIndex(5)

    def popular_lista(self, received_data):
        listview = self.tela_escolha_servico.listView
        model = QStandardItemModel()
        listview.setModel(model)
        for row, servico in enumerate(received_data):
            cpf = servico[4]
            senha = servico[2]
            dados_servico = f"Nome: {servico[1]}  Local: {servico[3]}  Especialização: {servico[5]}  Área: {servico[6]}"

            item = QStandardItem(dados_servico)

            item.setData(cpf, Qt.UserRole + 1)
            item.setData(senha, Qt.UserRole + 2)

            model.setItem(row, 0, item)

    def popular_lista_2(self):
        listview_2 = self.tela_escolha_servico.listView_2
        model = QStandardItemModel()
        listview_2.setModel(model)

        mensagem = "populando_lista_2"
        self.cliente_socket.send(mensagem.encode())
        recebida = self.cliente_socket.recv(1024)
        data = pickle.loads(recebida)

        for row, servicos in enumerate(data):
            id = servicos[0]
            data = f"Nome: {servicos[1]}"
            
            item = QStandardItem(data)
            
            item.setData(id, Qt.UserRole + 1)
            
            model.setItem(row, 0, item)

    def item_clicado(self, index: QModelIndex):
        if index.isValid():
            reply = QMessageBox.question(self,'Alerta!',f'Deseja selecionar esse servico?',QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            if reply == QMessageBox.Yes:
                item = index.model().itemFromIndex(index)

                cpf = item.data(Qt.UserRole + 1)
                senha = item.data(Qt.UserRole + 2)
                mensagem = f"busca,{cpf},{senha}"
                self.cliente_socket.send(mensagem.encode())            
                msg = self.cliente_socket.recv(1024).decode()
                self.popular_lista_2()
            
    
    # 1 tirar o alterar cpf do alterar dados
    # 2 deixar o botao de apagar conta no final da lista para igualar com o do cliente
    # 3 botar uma opção de aceitar ou recusar os pedidos enviados pelo cliente na tela podendo ser dois botoes um "ACEITAR" e outro
    # "RECUSAR" que quando apertados junto com a lista aceitem ou recusem o pedido ou abrir uma mini tela ao clicar em um valor
    # na lista que da a descrição do pedido e 2 opções 1 para aceitar e outra para recusar eles
    
    ##ARMAZENAR O ID NA LISTA2 PARA ASSIM PODER FAZER A REMOÇÃO CORRETAMETNE

    def armazenar_item(self, index: QModelIndex):
        self.true = False
        if index.isValid():
            self.true = True
            item = self.tela_escolha_servico.listView_2.model().itemFromIndex(index)
            self.item_clicado_F = item


    def acao_botao(self):
        if self.item_clicado_F is not None and self.true == True:
            id = self.item_clicado_F.data(Qt.UserRole + 1)
            mensagem = f"remove,{id}"
            self.cliente_socket.send(mensagem.encode())
            self.true = False
            self.popular_lista_2()
                
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
        mensagem = "pedidos"
        self.cliente_socket.send(mensagem.encode())
        data_recebida = self.cliente_socket.recv(1024)
        if data_recebida:
            data,valida = pickle.loads(data_recebida)
        else:
            data,valida = [],[]
        print(data,valida)    
        self.popular_pedidos(data,valida)
        self.QtStack.setCurrentIndex(8)
        
    def popular_pedidos(self,received_data,validacao):
        listview = self.ver_pedidos.listView
        model = QStandardItemModel()
        listview.setModel(model)
        i = 0
        for row, servico in enumerate(received_data):
            if(validacao[i] == ('T',)):

                dados_servico = f"Nome: {servico[1]}"

                item = QStandardItem(dados_servico)

                model.setItem(row, 0, item)
            i += 1
        
    def alterar_dados_cliente_banco(self):
        
        novo_nome = self.alterar_dados_cliente.lineEdit.text()
        nova_senha = self.alterar_dados_cliente.lineEdit_2.text()
        novo_endereco = self.alterar_dados_cliente.lineEdit_3.text()
        nova_nascimento = self.alterar_dados_cliente.lineEdit_4.text()
        if not(novo_nome == '' or nova_senha == '' or novo_endereco == '' or nova_nascimento == ''): 
            menssagem =  f'alterar_U,{novo_nome},{nova_senha},{novo_endereco},{nova_nascimento}'
            self.cliente_socket.send(menssagem.encode())
            recebida = self.cliente_socket.recv(1024).decode()
            
            if recebida == "T":
                QMessageBox.information(None, 'POOII', 'Dados do cliente alterados com sucesso!')
            else:
                QMessageBox.information(None, 'POOII', 'Falha ao alterar os dados!!')
            self.alterar_dados_cliente.lineEdit.setText('')
            self.alterar_dados_cliente.lineEdit_2.setText('')
            self.alterar_dados_cliente.lineEdit_3.setText('')
            self.alterar_dados_cliente.lineEdit_4.setText('')
            self.verifica = False
            self.QtStack.setCurrentIndex(0)

    def alterar_dados_prestador_banco(self):
 
        novo_nome = self.altera_dados_prestador_serviços.lineEdit.text()
        nova_senha = self.altera_dados_prestador_serviços.lineEdit_2.text()
        novo_local = self.altera_dados_prestador_serviços.lineEdit_3.text()
        nova_especializacao = self.altera_dados_prestador_serviços.lineEdit_4.text()
        nova_area = self.altera_dados_prestador_serviços.lineEdit_5.text()
        if not(novo_nome == '' or nova_senha == '' or novo_local == '' or nova_especializacao == '' or nova_area == ''): 
            menssagem =  f'alterar_S,{novo_nome},{nova_senha},{novo_local},{nova_especializacao},{nova_area}'
            self.cliente_socket.send(menssagem.encode())
            recebida = self.cliente_socket.recv(1024).decode()
            if recebida == "T":
                QMessageBox.information(None, 'POOII', 'Dados alterados com sucesso!')
            else:
                QMessageBox.information(None, 'POOII', 'Falha ao alterar os dados!!')
                
            self.altera_dados_prestador_serviços.lineEdit.setText('')
            self.altera_dados_prestador_serviços.lineEdit_2.setText('')
            self.altera_dados_prestador_serviços.lineEdit_3.setText('')
            self.altera_dados_prestador_serviços.lineEdit_4.setText('')
            self.altera_dados_prestador_serviços.lineEdit_5.setText('')
            self.verifica = False
            self.QtStack.setCurrentIndex(0)

    def sair(self):
        mensagem = "bye"
        self.cliente_socket.send(mensagem.encode())
        app.quit()
        
    def numero(self,cpf):
        a = str(cpf)
        if a.isnumeric():
            return True
        else:
            return False

#######PARTE_DA_CONEXAO###############

if __name__ == '__main__':
    app = QApplication(sys.argv)  
    cliente = Cliente('localhost', 8007)
    cliente.conectar_servidor()
    sys.exit(app.exec_())
    
#####################################