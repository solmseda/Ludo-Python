from Interface.Ui_Tabuleiro import Ui_Tabuleiro
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class Tabuleiro(QWidget,Ui_Tabuleiro):
    
    def __init__(self):
        super(Tabuleiro, self).__init__()
        self.setupUi(self)
        self.sideBarPlayersLeft.hide()
        self.sideBarPlayersRight.hide()
        self.diceLeft.hide()
        self.diceRight.hide()

        

import sys
if __name__ == "__main__":
    app = QApplication(sys.argv)
    board = Tabuleiro()
    sys.exit(app.exec_())






"""
QWidget#greenLayout {
background-color: rgb(255, 170, 0);
border-width: 2px;
border-style: solid;
border-color: rgb(0, 0, 0);
border-radius: 4;
}

image: url(:/Imagens/dice.png);
"""