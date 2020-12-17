from Interface.Ui_FimdeJogo import Ui_FimdeJogo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from jogadorPeca import *



class FimdeJogo(QWidget,Ui_FimdeJogo):
    
    def __init__(self):
        super(FimdeJogo, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


    def geraVencedor(self, Vencedor):
        if corJogador(Vencedor) == "Vermelho":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerRed.png);")
        elif corJogador(Vencedor) == "Amarelo":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerYellow.png);")
        elif corJogador(Vencedor) == "Verde":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerGreen.png);")
        elif corJogador(Vencedor) == "Azul":
            self.winnerImage.setStyleSheet("image: url(:/Imagens/playerBlue.png);")

        self.winnerName.setText(nomeJogador(Vencedor)+" venceu!")




