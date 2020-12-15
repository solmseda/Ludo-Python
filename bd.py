import mysql.connector
from mysql.connector import Error

def criarDataBase():
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')

        sql = "CREATE DATABASE Modular"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print(cursor.rowcount, "Tabela Criada")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")


def criarTabela():
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')
        sql = "CREATE TABLE Partida ( n_partida int not null PRIMARY KEY AUTO_INCREMENT, jogador_1 varchar(30), jogador_2 varchar(30), jogador_3 varchar(30), jogador_4 varchar(30), vencedor varchar(30) not null)"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print(cursor.rowcount, "Tabela Criada")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")

def inserePartida(jogadoresLista, vencedor):
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')
        cursor = connection.cursor()
        quant = len(jogadoresLista)
        if (quant == 2):
            cursor.execute("INSERT INTO Partida (Jogador_1, Jogador_2, vencedor) VALUES (%s,%s,%s)" , (jogadoresLista[0] , jogadoresLista[1], vencedor))
        elif (quant == 3):
            cursor.execute("INSERT INTO Partida (Jogador_1, Jogador_2, vencedor) VALUES (%s,%s,%s,%s)" , (jogadoresLista[0] , jogadoresLista[1], jogadoresLista[2], vencedor))
        elif (quant == 4):
            cursor.execute("INSERT INTO Partida (Jogador_1, Jogador_2, vencedor) VALUES (%s,%s,%s,%s,%s)" , (jogadoresLista[0] , jogadoresLista[1], jogadoresLista[2], jogadoresLista[3], vencedor))
        
        connection.commit()

        print(cursor.rowcount, "Partida Inserida")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")

def recuperaPartida():
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')
        sql = "SELECT * FROM Partida"
        cursor = connection.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        print(rs)
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")

    

def descreve():
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')

        sql = "DESCRIBE Partida"
        cursor = connection.cursor()
        cursor.execute(sql)

        print(cursor.rowcount, "Tabela Criada")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")

def dropPartida():
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')

        sql = "DROP TABLE Partida"
        cursor = connection.cursor()
        cursor.execute(sql)

        print(cursor.rowcount, "Tabela Apagada")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")



