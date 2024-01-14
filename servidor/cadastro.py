import mysql.connector as mysql
import socket
import threading
import pickle

host = ''
port = 8007
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10)

class Cadastro:
    
    def __init__(self):
        self.conta = []
        self.verifica = False

    def login(self,senha,cpf):
        self.de_cria()
        self.conta = self.busca_login(senha,cpf)

        if self.conta == None:
            return None,"F","F"
        else:
            if self.verifica == True:
                return self.conta[1],"T","T"        
            else: 
                return self.conta[1],"T","F"
        
    def busca_login(self,senha,cpf):
                
        conect = mysql.connect(host='localhost', database='sistema_de_servico', user='root', password='Ripanlong807!')
        cursor = conect.cursor()

        cursor.execute("SELECT * FROM clientes WHERE cpf_C  = %s AND senha = %s", (cpf, senha))
        resultados = cursor.fetchone()

        if resultados == None:            
            cursor.execute("SELECT * FROM servicos WHERE cpf = %s AND senha = %s", (cpf, senha))
            resultados = cursor.fetchone()
            
            if resultados != None:
                self.verifica =  True

        conect.close()
        if resultados == []:
            return None
        else:
            return resultados      



    ########################CADASTRO############################


    def de_cria(self):
        conect = mysql.connect(host='localhost', user='root', password='Ripanlong807!')
        cursor = conect.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_de_servico")    

        conect = mysql.connect(host='localhost', database='sistema_de_servico', user='root', password='Ripanlong807!')
        cursor = conect.cursor()

        sql_servicos = """CREATE TABLE IF NOT EXISTS servicos(id integer PRIMARY KEY AUTO_INCREMENT, Nome text NOT NULL, Senha text NOT NULL, local text NOT NULL, cpf int NOT null, especializacao text NOT NULL, area text NOT NULL); """
        cursor.execute(sql_servicos)

        sql_clientes = """CREATE TABLE IF NOT EXISTS clientes(id integer PRIMARY KEY AUTO_INCREMENT, nome text NOT NULL, senha text NOT NULL, endereco text NOT NULL, cpf_c int NOT null, nascimento text NOT NULL); """
        cursor.execute(sql_clientes)
        
        sql_escolhidos = """CREATE TABLE IF NOT EXISTS servicos_escolhidos(cliente_id integer, servico_id integer,validacao text NOT NULL, FOREIGN KEY (cliente_id) REFERENCES clientes(id), FOREIGN KEY (servico_id) REFERENCES servicos(id), PRIMARY KEY (cliente_id, servico_id));"""
        cursor.execute(sql_escolhidos)
                
        conect.close()

    def cadastrar_pessoa(self,nome,senha,endereco,cpf_C,nascimento):
        A = "F"
        self.de_cria()
        conect = mysql.connect(host='localhost', database='sistema_de_servico', user='root', password='Ripanlong807!')
        cursor = conect.cursor()
                
        existe1 = self.busca(cpf_C,senha,0)

        if existe1==None:
            try:
                cursor.execute('INSERT INTO clientes (nome, senha, endereco, cpf_C,nascimento) VALUES (%s, %s, %s, %s, %s)', (nome, senha, endereco, int(cpf_C), nascimento))
                conect.commit()

                A = "T"
            except:
                print("Banco de dados ja existente!")
                A = "F"
            finally:
                if conect:
                    conect.close()
        return A

    def cadastrar_servico(self,Nome,Senha,local,cpf,especializacao,area):
        A = "F"
        self.de_cria()
        conect = mysql.connect(host='localhost', database='sistema_de_servico', user='root', password='Ripanlong807!')
        cursor = conect.cursor() 

        existe = self.busca(cpf,Senha,0)
        if existe==None:
            try:
                cursor.execute('INSERT INTO servicos (Nome, Senha, local, cpf,especializacao, area) VALUES (%s, %s, %s, %s, %s, %s)', (Nome, Senha, local, int(cpf),especializacao, area))
                conect.commit()
                A = "T"
                
            except ZeroDivisionError as erro:
                print("Banco de dados ja existente! {erro}")
                A = "F"
            finally:
                if conect:
                    conect.close()
        return A
        


    ########################CADASTRO############################




    def apagar_conta(self):
        conn = mysql.connect(
            host='localhost',
            user='root',
            password='Ripanlong807!',
            database='sistema_de_servico'
        )

        cursor = conn.cursor()
        if self.verifica == False:
            comando_sql = "DELETE FROM clientes WHERE cpf_C = %s"
            id_para_apagar = self.conta[4]
            cursor.execute("DELETE FROM servicos_escolhidos WHERE cliente_id = %s", (self.conta[0],))
        else:
            comando_sql = "DELETE FROM servicos WHERE cpf = %s"
            id_para_apagar = self.conta[5]
            cursor.execute("DELETE FROM servicos_escolhidos WHERE servico_id = %s", (self.conta[0],))
        
        cursor.execute(comando_sql, (id_para_apagar,))

        conn.commit()
        conn.close()
        self.conta = []
        self.verifica = False
                       
                       
                          
    def busca(self,cpf,senha,x):
        conect = mysql.connect(host='localhost', database='sistema_de_servico', user='root', password='Ripanlong807!')
        cursor = conect.cursor()
        
        cursor.execute("SELECT * FROM servicos WHERE cpf  = %s AND senha = %s", (cpf, senha))
        resultados = cursor.fetchone()
        if (resultados == [] and x == 0):
            cursor.execute("SELECT * FROM clientes WHERE cpf_C  = %s AND senha = %s", (cpf, senha))
            resultados = cursor.fetchone()
        conect.close()
        return resultados
    
        
#############ALTERAR DADOS#########################
        
                
    def alterar_U(self,novo_nome,nova_senha,novo_endereco,nova_nascimento):
        try:
            conn = mysql.connect(
                host='localhost',
                user='root',
                password='Ripanlong807!',
                database='sistema_de_servico'
            )
            cursor = conn.cursor()
            comando_sql = "UPDATE clientes SET nome=%s,senha =%s, endereco=%s, nascimento=%s WHERE cpf_C=%s"
            cursor.execute(comando_sql, (novo_nome, nova_senha, novo_endereco, nova_nascimento, self.conta[4]))

            conn.commit()
            conn.close()
            self.conta = []
            return "T"
        except:
            self.conta = []
            return "F"
        
    def alterar_S(self,novo_nome,nova_senha,novo_local,nova_especializacao,nova_area):
        try:
            conn = mysql.connect(
                host='localhost',
                user='root',
                password='Ripanlong807!',
                database='sistema_de_servico'
            )

            cursor = conn.cursor()
            comando_sql = "UPDATE servicos SET nome=%s,senha=%s, local=%s, especializacao=%s, area=%s WHERE cpf=%s"
            cursor.execute(comando_sql, (novo_nome, nova_senha, novo_local, nova_especializacao, nova_area, self.conta[4]))

            conn.commit()
            conn.close()
            self.conta = []
            return "T"
        except:
            self.conta = []
            return "F"


#############ALTERAR DADOS#########################



##############VER_SERVICOS#########################

    def esolhar_servico(self):
        try:
            connec = mysql.connect(
                host='localhost',
                user='root',
                password='Ripanlong807!',
                database='sistema_de_servico'
            )
            cursor = connec.cursor()

            cursor.execute("SELECT * FROM servicos")                
            novos_servicos = cursor.fetchall()
            
        except mysql.Error as err:
            print(f"Erro no MySQL: {err}")

        finally:
            if connec.is_connected():
                connec.close()
                
        if novos_servicos is not None:
            return novos_servicos

    def popular_2(self):
        try:
            servicos = []
            con = mysql.connect(
                host='localhost',
                user='root',
                password='Ripanlong807!',
                database='sistema_de_servico'
            )
            cursor = con.cursor()

            cursor.execute("SELECT servico_id FROM servicos_escolhidos WHERE cliente_id = %s", (self.conta[0],))
            ids = cursor.fetchall()

            for id_servico in ids:
                cursor.execute("SELECT * FROM servicos WHERE id = %s", (id_servico[0],))
                servico = cursor.fetchone()
                servicos.append(servico)
        
        except Exception as e:
            print(f"Erro: {e}")
            return None
        finally:
            cursor.close()
            con.close()
            return servicos

    def adicionar(self, servico_id):
        conn = mysql.connect(
            host='localhost',
            user='root',
            password='Ripanlong807!',
            database='sistema_de_servico'
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM servicos_escolhidos WHERE cliente_id = %s AND servico_id = %s", (self.conta[0], servico_id))
        existe_associacao = cursor.fetchone()

        if not existe_associacao:
            cursor.execute("INSERT INTO servicos_escolhidos (cliente_id, servico_id,validacao) VALUES (%s, %s,%s)", (self.conta[0], servico_id,'F'))

        conn.commit()
        conn.close()


    def remove(self,id):
        conn = mysql.connect(
            host='localhost',
            user='root',
            password='Ripanlong807!',
            database='sistema_de_servico'
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM servicos_escolhidos WHERE cliente_id = %s AND servico_id = %s",(self.conta[0],id))
        conn.commit()
        conn.close()

##############VER_SERVICOS#########################


###############VER_PEDIDOS#########################
    def pedidos(self):
        saida = []
        try:
            conn = mysql.connect(
                host='localhost',
                user='root',
                password='Ripanlong807!',
                database='sistema_de_servico'
            )
            cursor = conn.cursor()

            cursor.execute("SELECT cliente_id FROM servicos_escolhidos WHERE servico_id = %s", (self.conta[0],))
            ids = cursor.fetchall()
            cursor.execute("SELECT validacao FROM servicos_escolhidos WHERE servico_id = %s", (self.conta[0],))
            validacao = cursor.fetchall()
            print("foi ate aqui")
            for cliente_id in ids:
                cursor.execute("SELECT * FROM clientes WHERE id = %s", cliente_id)
                cliente_info = cursor.fetchone()
                if cliente_info:
                    saida.append(cliente_info)

    
        except Exception as e:
            print(f"Erro ao acessar o banco de dados2: {e}")
            return [],[]

        finally:
            cursor.close()
            conn.close()
            return saida,validacao

###############VER_PEDIDOS#########################


###############NOTIFICAÇÕES########################

    def modificando(self,id):
        try:
            conn = mysql.connect(
                host='localhost',
                user='root',
                password='Ripanlong807!',
                database='sistema_de_servico'
            )
#validacao
            cursor = conn.cursor()
            comando_sql = "UPDATE servicos_escolhidos SET validacao=%s WHERE cliente_id=%s"
            cursor.execute(comando_sql, ('T',id))

            conn.commit()
            self.conta = []
            
        except Exception as e:
            print(f"Erro ao acessar o banco de dados: {e}")

        finally:
            cursor.close()
            conn.close()



    def reset(self):
        self.conta = []
        self.verifica = False




#SV
#criar uma classe com a função sv.

def server(con):

    """
    Função utilizada para atender a comunicação com clientes.

    A função em questao faz a utilização da classe cadastro, ela recebe mensagens enviadas pelo cliente
    e faz a comparação delas em varios ifs e elifs dentro de um while true para poder receber varios clientes
    e funcionar indenpendetemente, caso não encontre um caso ela da pass e nao faz nada,
    cada if compara a mensagem enviada pelo cliente e caso se encaixe entra em uma função especifica da 
    classe cadastro e realiza uma ação especifica no banco de dados enviado os resultados dessa ação novamente
    para o cliente.

    Parameters
    ----------
    con : socket
        O objeto de soquete que representa a conexão com o cliente.

    Raises
    ------
    Exception
        Qualquer exceção que ocorra durante a execução das comparações antes ditas.

    """


    x = True
    print(f"Cliente se conectou")
    cadastro = Cadastro()

    while x:
        try:

            recebe = con.recv(1024)
            mensagem = recebe.decode() 
            comando = mensagem.split(',')
            if recebe.decode() == 'bye' or recebe.decode() == '' or recebe.decode() == None:
                print("cliente desconectado")
                x = False
            elif recebe.decode() == 'Apagar':
                cadastro.apagar_conta()
                
            elif recebe.decode() == 'reset':
                cadastro.reset()
                
            elif recebe.decode() == "populando_lista_2":
                a = cadastro.popular_2()
                data = pickle.dumps(a)
                con.send(data)
                
            elif comando[0] == "cadastro_U":
                veri = cadastro.cadastrar_pessoa(comando[1], comando[2], comando[3], comando[4], comando[5])
                con.send(veri.encode())
            
            elif comando[0] == "cadastro_S":
                veri = cadastro.cadastrar_servico(comando[1], comando[2], comando[3], comando[4], comando[5], comando[6])
                con.send(veri.encode())
            
            elif comando[0] == "Login":
                A = cadastro.login(comando[1], comando[2])
                con.send(str(A).encode())

            elif comando[0] == "alterar_U":
                veri = cadastro.alterar_U(comando[1], comando[2], comando[3], comando[4])
                con.send(veri.encode())
                
            elif comando[0] == "alterar_S":
                veri = cadastro.alterar_S(comando[1], comando[2], comando[3], comando[4], comando[5])
                con.send(veri.encode())
            
            elif comando[0] == "escolha":
                servicos = cadastro.esolhar_servico()
                data_serialized = pickle.dumps(servicos)
                con.send(data_serialized)
                
            elif comando[0] == "busca":
                servicos = cadastro.busca(int(comando[1]),comando[2],1)
                if servicos != []:
                    a = 1
                    cadastro.adicionar(servicos[0])
                else:
                    a = 0
                con.send(str(a).encode())
                
            elif comando[0] == "remove":
                cadastro.remove(int(comando[1]))
                
            elif comando[0] == "pedidos":
                a = cadastro.pedidos()
                data = pickle.dumps(a)
                con.send(data)
                   
            elif comando[0] == "modificar_validade":
                cadastro.modificando(comando[1])
                                
            elif x:
                pass
            
        except Exception as e:
            print(f"Erro na comunicação: {e}")
            break
        
    con.close()

def main():
    print('Aguardando conexões...')

    while True:
        con, addr = serv_socket.accept() 
        client_thread = threading.Thread(target=server, args=(con,))
        client_thread.start()
if __name__ == "__main__":
    main()