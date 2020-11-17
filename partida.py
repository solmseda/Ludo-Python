from jogadorPeca import *
from Interface.Tabuleiro import Tabuleiro
from PyQt5.QtCore import pyqtSlot
import sys



@pyqtSlot()
def iniciaPartida():
    from main import interface

    for Jogador in Jogadores:

        if corJogador(Jogador) == "Verde":
            interface.tabuleiro.sideBarPlayersLeft.show()
            interface.tabuleiro.greenImage.setStyleSheet("image: url(:/Imagens/playerGreen.png);")
            interface.tabuleiro.greenName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceLeft.setEnabled(True)
            interface.tabuleiro.diceLeft.setStyleSheet("image: url(:/Imagens/dice.png);\nbackground-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenGreen.png);')")

        elif corJogador(Jogador) == "Amarelo":
            interface.tabuleiro.sideBarPlayersLeft.show()
            interface.tabuleiro.yellowImage.setStyleSheet("image: url(:/Imagens/playerYellow.png);")
            interface.tabuleiro.yellowName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceLeft.setEnabled(True)
            interface.tabuleiro.diceLeft.setStyleSheet("image: url(:/Imagens/dice.png);\nbackground-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenYellow.png);')")

        elif corJogador(Jogador) == "Vermelho":
            interface.tabuleiro.sideBarPlayersRight.show()
            interface.tabuleiro.redImage.setStyleSheet("image: url(:/Imagens/playerRed.png);")
            interface.tabuleiro.redName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceRight.setEnabled(True)
            interface.tabuleiro.diceRight.setStyleSheet("image: url(:/Imagens/dice.png);\nbackground-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenRed.png);')")

        elif corJogador(Jogador) == "Azul":
            interface.tabuleiro.sideBarPlayersRight.show()
            interface.tabuleiro.blueImage.setStyleSheet("image: url(:/Imagens/playerBlue.png);")
            interface.tabuleiro.blueName.setText(nomeJogador(Jogador))
            interface.tabuleiro.diceRight.setEnabled(True)
            interface.tabuleiro.diceRight.setStyleSheet("image: url(:/Imagens/dice.png);\nbackground-color: rgba(255, 255, 255, 0);")
            for peca in posicaoPecas(Jogador):
                exec("interface.tabuleiro.space_"+str(peca)+".setStyleSheet('image: url(:/Imagens/tokenBlue.png);')")

    interface.tabuleiro.show()
    interface.menu.close()