from Interface.Ui_Historico_Modulo import Ui_Historico_Modulo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from jogadorPeca import *



class Historico_Modulo(QWidget,Ui_Historico_Modulo):
    
    def __init__(self, partida):
        super(Historico_Modulo, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.matchNumber.setText(str(partida[0]))
        self.winnerName.setText(partida[1])

        corVencedor = partida[2]
        if corVencedor == "Verde":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerGreen.png);")
        elif corVencedor == "Vermelho":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerRed.png);")
        elif corVencedor == "Azul":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerBlue.png);")
        elif corVencedor == "Amarelo":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerYellow.png);")


        



        