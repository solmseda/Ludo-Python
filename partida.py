from jogadorPeca import *
from PyQt5.QtWidgets import QApplication
from Interface.Tabuleiro import Tabuleiro
from PyQt5.QtCore import pyqtSlot
import random
import sys
from main import *



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
            interface.tabuleiro.diceLeft.setEnabled(True)
            interface.tabuleiro.diceLeft.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);')")
            if prioridade == 0:
                exec("interface.tabuleiro.greenLayout.setStyleSheet('QWidget#greenLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')")

        elif corJogador(Jogador) == "Amarelo":
            telaEsq = True
            interface.tabuleiro.sideBarPlayersLeft.show()
            interface.tabuleiro.yellowImage.setStyleSheet("image: url(:/Imagens/playerYellow.png);")
            interface.tabuleiro.yellowName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceLeft.setEnabled(True)
            interface.tabuleiro.diceLeft.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);')")
            if prioridade == 0:
                exec("interface.tabuleiro.yellowLayout.setStyleSheet('QWidget#yellowLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')")


        elif corJogador(Jogador) == "Vermelho":
            telaDir = True
            interface.tabuleiro.sideBarPlayersRight.show()
            interface.tabuleiro.redImage.setStyleSheet("image: url(:/Imagens/playerRed.png);")
            interface.tabuleiro.redName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceRight.setEnabled(True)
            interface.tabuleiro.diceRight.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenRed.png);')")
            if prioridade == 0:
                exec("interface.tabuleiro.redLayout.setStyleSheet('QWidget#redLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')")


        elif corJogador(Jogador) == "Azul":
            telaDir = True
            interface.tabuleiro.sideBarPlayersRight.show()
            interface.tabuleiro.blueImage.setStyleSheet("image: url(:/Imagens/playerBlue.png);")
            interface.tabuleiro.blueName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceRight.setEnabled(True)
            interface.tabuleiro.diceRight.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);')")
            if prioridade == 0:
                exec("interface.tabuleiro.blueLayout.setStyleSheet('QWidget#blueLayout {background-color: rgb(255, 170, 0);border-width: 2px;border-style: solid;border-color: rgb(0, 0, 0);border-radius: 4;}')")

        prioridade -= 1


    if telaEsq and telaDir:
        interface.tabuleiro.setGeometry(100,100,1500,212)
    else:
        interface.tabuleiro.setGeometry(100,50,1050,212)
    interface.tabuleiro.show()
    interface.menu.close()