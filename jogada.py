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


dadoRolado = False
numJogada = 0
JogadorDaVez = None
valoresDado = []


def rolaDado():
    global dadoRolado
    dadoRolado = True
    num = random.randint(1, 6)
    exec("interface.tabuleiro."+interface.tabuleiro.sender().objectName()+".setText('"+str(num)+"')")
    valoresDado.append(num)


def novaJogada():
    global JogadorDaVez
    global numJogada
    JogadorDaVez = Jogadores[numJogada % len(Jogadores)]

    interface.tabuleiro.diceGreen.hide()
    interface.tabuleiro.diceGreen.setText("")
    interface.tabuleiro.diceGreen.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    interface.tabuleiro.greenLayout.setStyleSheet('')
    interface.tabuleiro.diceYellow.hide()
    interface.tabuleiro.diceYellow.setText("")
    interface.tabuleiro.diceYellow.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    interface.tabuleiro.yellowLayout.setStyleSheet('')
    interface.tabuleiro.diceRed.hide()
    interface.tabuleiro.diceRed.setText("")
    interface.tabuleiro.diceRed.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    interface.tabuleiro.redLayout.setStyleSheet('')
    interface.tabuleiro.diceBlue.hide()
    interface.tabuleiro.diceBlue.setText("")
    interface.tabuleiro.diceBlue.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    interface.tabuleiro.blueLayout.setStyleSheet('')

    global dadoRolado
    dadoRolado = False
    numJogada += 1

    if corJogador(JogadorDaVez) == "Verde":
        interface.tabuleiro.diceGreen.show()
        interface.tabuleiro.diceGreen.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.greenLayout.setStyleSheet('QWidget#greenLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(JogadorDaVez) == "Amarelo":
        interface.tabuleiro.diceYellow.show()
        interface.tabuleiro.diceYellow.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.yellowLayout.setStyleSheet('QWidget#yellowLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(JogadorDaVez) == "Vermelho":
        interface.tabuleiro.diceRed.show()
        interface.tabuleiro.diceRed.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.redLayout.setStyleSheet('QWidget#redLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(JogadorDaVez) == "Azul":
        interface.tabuleiro.diceBlue.show()
        interface.tabuleiro.diceBlue.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.blueLayout.setStyleSheet('QWidget#blueLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')



def validaJogada(JogadorDaVez, valoresDado):
    if dadoRolado == True:
        peca = 0
        global numJogada
        for posicaoPeca in posicaoPecas(JogadorDaVez):
            if interface.tabuleiro.sender().objectName() == "space_"+str(posicaoPeca):
                movimentaPeca(JogadorDaVez, peca, valoresDado[numJogada-1])
            peca += 1



def movimentaPeca(JogadorDaVez, peca, dado):

    if corJogador(JogadorDaVez) == "Verde":
        if posicaoPecas(JogadorDaVez,peca) in range(77,81):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 2
                interface.tabuleiro.space_2.setStyleSheet('image: url(:/Imagens/tokenGreen.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = posicaoPecas(JogadorDaVez,peca)+dado
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);');")

    elif corJogador(JogadorDaVez) == "Amarelo":
        if posicaoPecas(JogadorDaVez,peca) in range(89,93):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 41
                interface.tabuleiro.space_41.setStyleSheet('image: url(:/Imagens/tokenYellow.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = posicaoPecas(JogadorDaVez,peca)+dado
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);');")

    elif corJogador(JogadorDaVez) == "Vermelho":
        if posicaoPecas(JogadorDaVez,peca) in range(81,85):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 15
                interface.tabuleiro.space_15.setStyleSheet('image: url(:/Imagens/tokenRed.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = posicaoPecas(JogadorDaVez,peca)+dado
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenRed.png);');")
        
    elif corJogador(JogadorDaVez) == "Azul":
        if posicaoPecas(JogadorDaVez,peca) in range(85,89):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 28
                interface.tabuleiro.space_28.setStyleSheet('image: url(:/Imagens/tokenBlue.png);')
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = posicaoPecas(JogadorDaVez,peca)+dado
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);');")

    print(Jogadores)
    novaJogada()


interface.tabuleiro.diceBlue.clicked.connect(rolaDado)
interface.tabuleiro.diceRed.clicked.connect(rolaDado)
interface.tabuleiro.diceGreen.clicked.connect(rolaDado)
interface.tabuleiro.diceYellow.clicked.connect(rolaDado)



for cont in range(1,93):
    exec("interface.tabuleiro.space_"+str(cont)+".clicked.connect(lambda: validaJogada(JogadorDaVez,valoresDado))")