#Autor: Victor Nielsen
#Tempo: 4 horas

from jogadorPeca import *
from PyQt5.QtWidgets import QApplication
from Interface.Tabuleiro import Tabuleiro
from PyQt5.QtCore import pyqtSlot
import random
import sys
from main import *
import jogada
interface.menu.close()




@pyqtSlot()
def iniciaPartida():

    telaEsq = False
    telaDir = False
    prioridade = random.randint(0,len(Jogadores)-1)
    for Jogador in Jogadores:

        if corJogador(Jogador) == "Verde":
            telaEsq = True
            interface.tabuleiro.sideBarPlayersLeft.show()
            interface.tabuleiro.greenImage.setStyleSheet("image: url(:/Imagens/playerGreen.png);")
            interface.tabuleiro.greenName.setText(nomeJogador(Jogador))
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);')")
            if prioridade == 0:
                ordemCores = ["Verde","Vermelho","Azul","Amarelo"]
                interface.NovaJogada.emit(False)

        elif corJogador(Jogador) == "Amarelo":
            telaEsq = True
            interface.tabuleiro.sideBarPlayersLeft.show()
            interface.tabuleiro.yellowImage.setStyleSheet("image: url(:/Imagens/playerYellow.png);")
            interface.tabuleiro.yellowName.setText(nomeJogador(Jogador))
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);')")
            if prioridade == 0:
                ordemCores = ["Amarelo","Verde","Vermelho","Azul"]
                interface.NovaJogada.emit(False)

        elif corJogador(Jogador) == "Vermelho":
            telaDir = True
            interface.tabuleiro.sideBarPlayersRight.show()
            interface.tabuleiro.redImage.setStyleSheet("image: url(:/Imagens/playerRed.png);")
            interface.tabuleiro.redName.setText(nomeJogador(Jogador))
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenRed.png);')")
            if prioridade == 0:
                ordemCores = ["Vermelho","Azul","Amarelo","Verde"]
                interface.NovaJogada.emit(False)

        elif corJogador(Jogador) == "Azul":
            telaDir = True
            interface.tabuleiro.sideBarPlayersRight.show()
            interface.tabuleiro.blueImage.setStyleSheet("image: url(:/Imagens/playerBlue.png);")
            interface.tabuleiro.blueName.setText(nomeJogador(Jogador))
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);')")
            if prioridade == 0:
                ordemCores = ["Azul","Amarelo","Verde","Vermelho"]
                interface.NovaJogada.emit(False)

        prioridade -= 1
    """
    cont = 0
    while cont < len(Jogadores):
        for Jogador in Jogadores:
            if corJogador(Jogador) == ordemCores[cont]:
                ordemJogadores[cont] = Jogador
                cont += 1
    print(ordemJogadores)
    """

    if telaEsq and telaDir:
        interface.tabuleiro.setGeometry(100,50,1500,212)
    else:
        interface.tabuleiro.setGeometry(100,50,1250,212)
    interface.tabuleiro.show()
    interface.menu.close()

    

    

    



interface.NovaJogada.connect(jogada.novaJogada)