from Interface.Ui_Historico_Modulo import Ui_Historico_Modulo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from jogadorPeca import *



class Historico_Modulo(QWidget,Ui_Historico_Modulo):
    
    def __init__(self, partida):
        super(Historico_Modulo, self).__init__()
        self.setupUi(self)

        self.matchNumber.setText(str(partida[0]))
        self.winnerName.setText(partida[1])
        
        if corJogador(partida[0]) == "Verde":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerGreen.png);")
        elif corJogador(partida[0]) == "Verde":


        if Jogador[1] == "Verde":
            Jogador.append([77,78,79,80])
        elif Jogador[1] == "Vermelho":
            Jogador.append([81,82,83,84])
        elif Jogador[1] == "Azul":
            Jogador.append([85,86,87,88])
        elif Jogador[1] == "Amarelo":
            Jogador.append([72,73,74,75])

        