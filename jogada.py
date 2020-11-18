# Autores: Eduardo Sardenberg e Victor Nielsen (1711600 e 1811545)
# Horas Trabalhadas ao todo: 8 horas e meia
"""	
Horas Trabalhadas - Sol Castilho de Moraes Sêda
11/11/2020 -> INICIO: 13:20
14/11/2020 -> INICIO: 14:00 - TERMINO: 19:00
15/11/2020 -> INICIO: 13:00 - TERMINO: 23:00

"""

import random
from jogadorPeca import *
from PyQt5.QtCore import pyqtSlot
from main import interface


numJogada = 0
JogadorDaVez = None
valoresDado = []


def rolaDado():
    dadoRolado = True
    num = random.randint(1, 6)
    print(num)
    valoresDado.append(num)


def novaJogada(Jogador):
    global JogadorDaVez
    JogadorDaVez = Jogador
    if corJogador(Jogador) == "Verde":
        interface.tabuleiro.diceGreen.show()
        interface.tabuleiro.diceGreen.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.greenLayout.setStyleSheet('QWidget#greenLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(Jogador) == "Amarelo":
        interface.tabuleiro.diceYellow.show()
        interface.tabuleiro.diceYellow.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.yellowLayout.setStyleSheet('QWidget#yellowLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(Jogador) == "Vermelho":
        interface.tabuleiro.diceRed.show()
        interface.tabuleiro.diceRed.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.redLayout.setStyleSheet('QWidget#redLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(Jogador) == "Azul":
        interface.tabuleiro.diceBlue.show()
        interface.tabuleiro.diceBlue.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.blueLayout.setStyleSheet('QWidget#blueLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')



def validaJogada(JogadorDaVez, valoresDado):
    peca = 0
    global numJogada
    for posicaoPeca in posicaoPecas(JogadorDaVez):
        if interface.tabuleiro.sender().objectName() == "space_"+str(posicaoPeca):
            movimentaPeca(JogadorDaVez, peca, valoresDado[numJogada])
        peca += 1



def movimentaPeca(JogadorDaVez, peca, dado):

    if corJogador(JogadorDaVez) == "Verde":
        if posicaoPecas(JogadorDaVez,peca) in range(77,81):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                interface.tabuleiro.space_2.setStyleSheet('image: url(:/Imagens/tokenGreen.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca)+dado)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);');")

    elif corJogador(JogadorDaVez) == "Amarelo":
        if posicaoPecas(JogadorDaVez,peca) in range(89,93):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                interface.tabuleiro.space_41.setStyleSheet('image: url(:/Imagens/tokenYellow.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca)+dado)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);');")

    elif corJogador(JogadorDaVez) == "Vermelho":
        if posicaoPecas(JogadorDaVez,peca) in range(81,85):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                interface.tabuleiro.space_15.setStyleSheet('image: url(:/Imagens/tokenRed.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca)+dado)+".setStyleSheet('image: url(:/Imagens/tokenRed.png);');")
        
    elif corJogador(JogadorDaVez) == "Azul":
        if posicaoPecas(JogadorDaVez,peca) in range(85,89):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                interface.tabuleiro.space_28.setStyleSheet('image: url(:/Imagens/tokenBlue.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca)+dado)+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);');")


interface.tabuleiro.diceBlue.clicked.connect(rolaDado)
interface.tabuleiro.diceRed.clicked.connect(rolaDado)
interface.tabuleiro.diceGreen.clicked.connect(rolaDado)
interface.tabuleiro.diceYellow.clicked.connect(rolaDado)



for cont in range(1,93):
    exec("interface.tabuleiro.space_"+str(cont)+".clicked.connect(lambda: validaJogada(JogadorDaVez,valoresDado))")