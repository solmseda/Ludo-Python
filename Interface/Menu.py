from Interface.Ui_Menu import Ui_Menu

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from Interface.Regras import Regras
#from Interface.Historico import Historico


class Menu(QMainWindow,Ui_Menu):

    IniciaPartida = pyqtSignal(bool)

    def __init__(self):
        super(Menu, self).__init__()
        
        self.setupUi(self)
        self.regras = Regras()
        #self.historico = Historico()

        self.pushButtonRules.clicked.connect(self.regras.show)
        self.pushButtonExit.clicked.connect(self.close)
        self.PlayOptions = False
        self.pushButtonPlay.clicked.connect(self.switchOptions)
        self.spinBoxNumPlayers.lineEdit().setReadOnly(True)
        self.pushButtonBack.clicked.connect(self.switchOptions)
        self.playerOptions.hide()
        self.warningLayout.hide()
        self.spinBoxNumPlayers.valueChanged.connect(self.setNumPlayers)
        self.setNumPlayers()

        self.p1Color = "Red"
        self.p2Color = "Yellow"
        self.p3Color = "Green"
        self.p4Color = "Blue"
        self.colorP1.clicked.connect(self.changeColorP1)
        self.colorP2.clicked.connect(self.changeColorP2)
        self.colorP3.clicked.connect(self.changeColorP3)
        self.colorP4.clicked.connect(self.changeColorP4)

        self.pushButtonStart.clicked.connect(self.close)

        #self.pushButtonPlay.clicked.connect(self.)
        #self.nomesJogadores = []
        #self.coresJogadores = []

        #self.pushButtonStart.clicked.connect(self.inicia_partida)



    def switchOptions(self):
        if self.PlayOptions == False:
            self.menuOptions.hide()
            self.playerOptions.show()
            self.PlayOptions = True
        else:
            self.menuOptions.show()
            self.playerOptions.hide()
            self.PlayOptions = False


    def setNumPlayers(self):
        self.numPlayers = self.spinBoxNumPlayers.value()
        if self.numPlayers == 2:
            self.optionsP3.hide()
            self.optionsP4.hide()
        elif self.numPlayers == 3:
            self.optionsP3.show()
            self.optionsP4.hide()
        else:
            self.optionsP3.show()
            self.optionsP4.show()


    def changeColorP1(self):
        if self.p1Color == "Red":
            self.colorP1.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p1Color = "Yellow"
        elif self.p1Color == "Yellow":
            self.colorP1.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p1Color = "Green"
        elif self.p1Color == "Green":
            self.colorP1.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p1Color = "Blue"
        else:
            self.colorP1.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p1Color = "Red"


    def changeColorP2(self):
        if self.p2Color == "Red":
            self.colorP2.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p2Color = "Yellow"
        elif self.p2Color == "Yellow":
            self.colorP2.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p2Color = "Green"
        elif self.p2Color == "Green":
            self.colorP2.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p2Color = "Blue"
        else:
            self.colorP2.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p2Color = "Red"


    def changeColorP3(self):
        if self.p3Color == "Red":
            self.colorP3.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p3Color = "Yellow"
        elif self.p3Color == "Yellow":
            self.colorP3.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p3Color = "Green"
        elif self.p3Color == "Green":
            self.colorP3.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p3Color = "Blue"
        else:
            self.colorP3.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p3Color = "Red"


    def changeColorP4(self):
        if self.p4Color == "Red":
            self.colorP4.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p4Color = "Yellow"
        elif self.p4Color == "Yellow":
            self.colorP4.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p4Color = "Green"
        elif self.p4Color == "Green":
            self.colorP4.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p4Color = "Blue"
        else:
            self.colorP4.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p4Color = "Red"


    #def inicia_partida(self):

"""
    def valida_partida(self):

        if len(self.nomesJogadores) == 2 and (numJogadores[0] == "" or numJogadores[1] == ""):
            self.error_dialog.showMessage('É necessário preencher o nome dos 2 jogadores\n para começar a partida.')
            self.validada = False
            return

        elif len(self.nomesJogadores) == 3 and (numJogadores[0] == "" or numJogadores[1] == "" or numJogadores[2] == ""):
            self.error_dialog.showMessage('É necessário preencher o nome dos 3 jogadores\n para começar a partida.')
            self.validada = False
            return

        elif len(self.nomesJogadores) == 4 and (numJogadores[0] == "" or numJogadores[1] == "" or numJogadores[2] == "" or numJogadores[3] == ""):
            self.error_dialog.showMessage('É necessário preencher o nome dos 4 jogadores\n para começar a partida.')
            self.validada = False
            return

        if len(self.coresJogadores) == 2 and (numJogadores[0] == "" or numJogadores[1] == ""):

        




    def jogador_qnt(self, num):
        self.numJogadores = self.spinBoxPlayersNum.getValue()
        


    def jogador_insere(self, nome, cor):

        self.nomesJogadores.append(str(self.lineEditP1.text()))
        self.coresJogadores.append(self.selecionaCor())

        self.nomesJogadores.append(str(self.lineEditP1.text()))
        self.coresJogadores.append(self.selecionaCor())

        if self.numJogadores == 3:
            self.nomesJogadores.append(str(self.lineEditP1.text()))
            self.coresJogadores.append(self.selecionaCor())

        elif self.numJogadores == 4:
            self.nomesJogadores.append(str(self.lineEditP1.text()))
            self.coresJogadores.append(self.selecionaCor())



    def jogador_remove(self):




            
        
    
    def abre_regras(self):
        self.regras.show()


    def abre_historico(self):
        self.historico.show()

    
"""

