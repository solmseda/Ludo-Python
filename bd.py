#Sol - 10 horas

import mysql.connector
from mysql.connector import Error
from jogadorPeca import *



def criarDataBase():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='root')

        sql = "CREATE DATABASE Modular"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print(cursor.rowcount+1, "Banco de Dados criado")
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
        sql = "CREATE TABLE Partida ( n_partida int not null PRIMARY KEY AUTO_INCREMENT, vencedor varchar(30) not null, corVencedor varchar(10) not null, numeroJogadores varchar(3) not null, jogador_1 varchar(30) not null, jogador_2 varchar(30) not null, jogador_3 varchar(30), jogador_4 varchar(30), corJogador_1 varchar(10) not null, corJogador_2 varchar(10) not null, corJogador_3 varchar(10), corJogador_4 varchar(10))"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

        print(cursor.rowcount+1, "Tabela Criada")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")


def inserePartida(Vencedor,corVencedor):
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')
        cursor = connection.cursor()
        quant = len(Jogadores)
        if (quant == 2):
            cursor.execute("INSERT INTO Partida (Vencedor, corVencedor, numeroJogadores, Jogador_1, Jogador_2, Jogador_3, Jogador_4, CorJogador_1, CorJogador_2, CorJogador_3, CorJogador_4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (Vencedor, corVencedor, str(quant), nomeJogador(Jogadores[0]) , nomeJogador(Jogadores[1]), "" , "" , corJogador(Jogadores[0]) , corJogador(Jogadores[1]) , "" , ""))
        elif (quant == 3):
            cursor.execute("INSERT INTO Partida (Vencedor, corVencedor, numeroJogadores, Jogador_1, Jogador_2, Jogador_3, Jogador_4, CorJogador_1, CorJogador_2, CorJogador_3, CorJogador_4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (Vencedor, corVencedor, str(quant), nomeJogador(Jogadores[0]) , nomeJogador(Jogadores[1]), nomeJogador(Jogadores[2]) , "" , corJogador(Jogadores[0]) , corJogador(Jogadores[1]) , corJogador(Jogadores[2]) , ""))
        elif (quant == 4):
            cursor.execute("INSERT INTO Partida (Vencedor, corVencedor, numeroJogadores, Jogador_1, Jogador_2, Jogador_3, Jogador_4, CorJogador_1, CorJogador_2, CorJogador_3, CorJogador_4) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (Vencedor, corVencedor, str(quant), nomeJogador(Jogadores[0]) , nomeJogador(Jogadores[1]), nomeJogador(Jogadores[2]) , nomeJogador(Jogadores[3]) , corJogador(Jogadores[0]) , corJogador(Jogadores[1]) , corJogador(Jogadores[2]) , corJogador(Jogadores[3])))
        
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
    try:
        return rs
    except:
        return None



def dropPartida():
    try:
        connection = mysql.connector.connect(host='localhost', database='Modular', user='root', password='root')

        sql = "DROP TABLE Partida"
        cursor = connection.cursor()
        cursor.execute(sql)

        print(cursor.rowcount+1, "Tabela Apagada")
        cursor.close()

    except Error as e:
        print("Erro de conexão", e)
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexão encerrada")




