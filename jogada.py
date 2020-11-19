# Autores: Todos do grupo (1711600 e 1811545)
# Horas Trabalhadas ao todo: 40 horas
#Victor -- 20 horas
#Sol -- 10 horas
#Eduardo -- 10 horas


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
    exec("interface.tabuleiro."+interface.tabuleiro.sender().objectName()+".setDisabled(True)")
    valoresDado.append(num)


def novaJogada(repetida):
    global JogadorDaVez
    global numJogada
    JogadorDaVez = Jogadores[numJogada % len(Jogadores)]
    if repetida:
        JogadorDaVez = Jogadores[(numJogada-1) % len(Jogadores)]

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
        interface.tabuleiro.diceGreen.setDisabled(False)
        interface.tabuleiro.diceGreen.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.greenLayout.setStyleSheet('QWidget#greenLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(JogadorDaVez) == "Amarelo":
        interface.tabuleiro.diceYellow.show()
        interface.tabuleiro.diceYellow.setDisabled(False)
        interface.tabuleiro.diceYellow.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.yellowLayout.setStyleSheet('QWidget#yellowLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(JogadorDaVez) == "Vermelho":
        interface.tabuleiro.diceRed.show()
        interface.tabuleiro.diceRed.setDisabled(False)
        interface.tabuleiro.diceRed.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.redLayout.setStyleSheet('QWidget#redLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')
    if corJogador(JogadorDaVez) == "Azul":
        interface.tabuleiro.diceBlue.show()
        interface.tabuleiro.diceBlue.setDisabled(False)
        interface.tabuleiro.diceBlue.setStyleSheet("image: url(:/Imagens/dice.png);background-color: rgba(255, 255, 255, 0);")
        interface.tabuleiro.blueLayout.setStyleSheet('QWidget#blueLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')



def checaTorre(Jogador,peca):
    for cont in range(0,len(posicaoPecas(Jogador))):
        if posicaoPecas(Jogador,peca) == posicaoPecas(Jogador,cont) and peca != cont: 
            return True
    return False
        


def checaColisao(JogadorDaVez):
    for Jogador in Jogadores:
        if Jogador != JogadorDaVez:
            if bool(set(posicaoPecas(JogadorDaVez)).intersection(posicaoPecas(Jogador))):
                return [True,Jogador]
    return [False]



def validaJogada(JogadorDaVez, valoresDado):
    if dadoRolado == True:
        peca = 0
        livre = False
        global numJogada
        for posicaoPeca in posicaoPecas(JogadorDaVez):
            if interface.tabuleiro.sender().objectName() == "space_"+str(posicaoPeca):
                if checaTorre(JogadorDaVez,peca) == False:
                    movimentaPeca(JogadorDaVez, peca, valoresDado[numJogada-1])
                    return
                elif checaTorre(JogadorDaVez,peca) == True:
                    movimentaPeca(JogadorDaVez, peca, valoresDado[numJogada-1])
                    if corJogador(JogadorDaVez) == "Verde":
                        exec("interface.tabuleiro.space_"+str(posicaoPeca)+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);')")
                    elif corJogador(JogadorDaVez) == "Amarelo":
                        exec("interface.tabuleiro.space_"+str(posicaoPeca)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);')")
                    elif corJogador(JogadorDaVez) == "Vermelho":
                        exec("interface.tabuleiro.space_"+str(posicaoPeca)+".setStyleSheet('image: url(:/Imagens/tokenRed.png);')")
                    elif corJogador(JogadorDaVez) == "Azul":
                        exec("interface.tabuleiro.space_"+str(posicaoPeca)+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);')")
                    return
            peca += 1



def retornaBase(Jogador,peca):
    for cont in range(0,4):
        if posicaoPecas(Jogador,peca) == posicaoPecas(Jogador,cont):
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            if corJogador(Jogador) == "Verde":
                Jogador[2][cont] = 77+cont
                exec("interface.tabuleiro.space_"+str(77+cont)+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);');")
            elif corJogador(Jogador) == "Amarelo":
                Jogador[2][cont] = 89+cont
                exec("interface.tabuleiro.space_"+str(89+cont)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);');")
            elif corJogador(Jogador) == "Vermelho":
                Jogador[2][cont] = 81+cont
                exec("interface.tabuleiro.space_"+str(81+cont)+".setStyleSheet('image: url(:/Imagens/tokenRed.png);');")
            elif corJogador(Jogador) == "Azul":
                Jogador[2][cont] = 85+cont
                exec("interface.tabuleiro.space_"+str(85+cont)+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);');")



def movimentaPeca(JogadorDaVez, peca, dado, visualização = False):

    ação = []
    JogadorInicial = JogadorDaVez

    if corJogador(JogadorDaVez) == "Verde":
        #Quando está na base
        if posicaoPecas(JogadorDaVez,peca) in range(77,81):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 2
                interface.tabuleiro.space_2.setStyleSheet('image: url(:/Imagens/tokenGreen.png);')
        #Quando está na área comum
        elif posicaoPecas(JogadorDaVez,peca) in range(1,53):
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    if posicaoPecas(JogadorDaVez,peca)+dado > 53:
                        Jogadores[cont][2][peca] = posicaoPecas(JogadorDaVez,peca)+dado-1
                    elif posicaoPecas(JogadorDaVez,peca) == 1:
                        Jogadores[cont][2][peca] = 52+dado
                    else:
                        Jogadores[cont][2][peca] = (posicaoPecas(JogadorDaVez,peca)+dado)%52
                        if Jogadores[cont][2][peca] == 0:
                            Jogadores[cont][2][peca] += 1
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);');")
        #Quando está na área de chegada
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = 58-abs(58-(posicaoPecas(JogadorDaVez,peca)+dado))
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);');")

    elif corJogador(JogadorDaVez) == "Amarelo":
        #Quando está na base
        if posicaoPecas(JogadorDaVez,peca) in range(89,93):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 41
                interface.tabuleiro.space_41.setStyleSheet('image: url(:/Imagens/tokenYellow.png);')
        #Quando está na área comum
        elif posicaoPecas(JogadorDaVez,peca) in range(1,53):
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    if posicaoPecas(JogadorDaVez,peca)<=40 and posicaoPecas(JogadorDaVez,peca)+dado > 40:
                        Jogadores[cont][2][peca] = 70 + abs(40-(posicaoPecas(JogadorDaVez,peca)+dado))
                    else:
                        Jogadores[cont][2][peca] = (posicaoPecas(JogadorDaVez,peca)+dado)%52
                        if Jogadores[cont][2][peca] == 0:
                            Jogadores[cont][2][peca] += 1
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);');")
        #Quando está na área de chegada
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = 76-abs(76-(posicaoPecas(JogadorDaVez,peca)+dado))
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);');")

    elif corJogador(JogadorDaVez) == "Vermelho":
        #Quando está na base
        if posicaoPecas(JogadorDaVez,peca) in range(81,85):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 15
                interface.tabuleiro.space_15.setStyleSheet('image: url(:/Imagens/tokenRed.png);')
        #Quando está na área comum
        elif posicaoPecas(JogadorDaVez,peca) in range(1,53):
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    if posicaoPecas(JogadorDaVez,peca)<=14 and posicaoPecas(JogadorDaVez,peca)+dado > 14:
                        Jogadores[cont][2][peca] = 58 + abs(14-(posicaoPecas(JogadorDaVez,peca)+dado))
                    else:
                        Jogadores[cont][2][peca] = (posicaoPecas(JogadorDaVez,peca)+dado)%52
                        if Jogadores[cont][2][peca] == 0:
                            Jogadores[cont][2][peca] += 1
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenRed.png);');")
        #Quando está na área de chegada
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = 64-abs(64-(posicaoPecas(JogadorDaVez,peca)+dado))
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenRed.png);');")
        
    elif corJogador(JogadorDaVez) == "Azul":
        #Quando está na base
        if posicaoPecas(JogadorDaVez,peca) in range(85,89):
            if dado == 1 or dado == 6:
                exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
                for cont in range(0,len(Jogadores)):
                    if Jogadores[cont] == JogadorDaVez:
                        Jogadores[cont][2][peca] = 28
                interface.tabuleiro.space_28.setStyleSheet('image: url(:/Imagens/tokenBlue.png);')
        #Quando está na área comum
        elif posicaoPecas(JogadorDaVez,peca) in range(1,53):
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    if posicaoPecas(JogadorDaVez,peca)<=27 and posicaoPecas(JogadorDaVez,peca)+dado > 27:
                        Jogadores[cont][2][peca] = 64 + abs(27-(posicaoPecas(JogadorDaVez,peca)+dado))
                    else:
                        Jogadores[cont][2][peca] = (posicaoPecas(JogadorDaVez,peca)+dado)%52
                        if (Jogadores[cont][2][peca]+dado)%52 == 0:
                            Jogadores[cont][2][peca] += 1
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);');")
        #Quando está na área de chegada
        else:
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('');")
            for cont in range(0,len(Jogadores)):
                if Jogadores[cont] == JogadorDaVez:
                    Jogadores[cont][2][peca] = 70-abs(70-(posicaoPecas(JogadorDaVez,peca)+dado))
            exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);');")

    if checaTorre(JogadorDaVez,peca):
        exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorDaVez,peca))+".setText('+')")
    else:
        exec("interface.tabuleiro.space_"+str(posicaoPecas(JogadorInicial,peca))+".setText('')")


    if checaColisao(JogadorDaVez)[0]:
        retornaBase(checaColisao(JogadorDaVez)[1],peca)



    print(Jogadores)

    novaJogada(False)


interface.tabuleiro.diceBlue.clicked.connect(rolaDado)
interface.tabuleiro.diceRed.clicked.connect(rolaDado)
interface.tabuleiro.diceGreen.clicked.connect(rolaDado)
interface.tabuleiro.diceYellow.clicked.connect(rolaDado)



for cont in range(1,93):
    exec("interface.tabuleiro.space_"+str(cont)+".clicked.connect(lambda: validaJogada(JogadorDaVez,valoresDado))")