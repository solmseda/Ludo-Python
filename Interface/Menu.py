# Autor: Victor Nielsen Ribeirete (1811545)
# Horas Trabalhadas: 10 Horas


from Interface.Ui_Menu import Ui_Menu

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot


class Menu(QMainWindow,Ui_Menu):

    StartMatchSignal = pyqtSignal(list,list)

    def __init__(self):
        super(Menu, self).__init__()
        
        self.setupUi(self)

        self.pushButtonExit.clicked.connect(self.close)
        self.PlayOptions = False
        self.pushButtonPlay.clicked.connect(self.switchOptions)
        self.spinBoxNumPlayers.lineEdit().setReadOnly(True)
        self.pushButtonBack.clicked.connect(self.switchOptions)
        self.playerOptions.hide()
        self.warningLayout.hide()
        self.spinBoxNumPlayers.valueChanged.connect(self.setNumPlayers)
        self.setNumPlayers()

        self.p1Color = "Vermelho"
        self.p2Color = "Amarelo"
        self.p3Color = "Verde"
        self.p4Color = "Azul"
        self.colorP1.clicked.connect(self.changeColorP1)
        self.colorP2.clicked.connect(self.changeColorP2)
        self.colorP3.clicked.connect(self.changeColorP3)
        self.colorP4.clicked.connect(self.changeColorP4)

        self.playerNames = []
        self.playerColors = []

        self.pushButtonStart.clicked.connect(self.startMatch)


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
        if self.p1Color == "Vermelho":
            self.colorP1.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p1Color = "Amarelo"
        elif self.p1Color == "Amarelo":
            self.colorP1.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p1Color = "Verde"
        elif self.p1Color == "Verde":
            self.colorP1.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p1Color = "Azul"
        else:
            self.colorP1.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p1Color = "Vermelho"


    def changeColorP2(self):
        if self.p2Color == "Vermelho":
            self.colorP2.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p2Color = "Amarelo"
        elif self.p2Color == "Amarelo":
            self.colorP2.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p2Color = "Verde"
        elif self.p2Color == "Verde":
            self.colorP2.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p2Color = "Azul"
        else:
            self.colorP2.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p2Color = "Vermelho"


    def changeColorP3(self):
        if self.p3Color == "Vermelho":
            self.colorP3.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p3Color = "Amarelo"
        elif self.p3Color == "Amarelo":
            self.colorP3.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p3Color = "Verde"
        elif self.p3Color == "Verde":
            self.colorP3.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p3Color = "Azul"
        else:
            self.colorP3.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p3Color = "Vermelho"


    def changeColorP4(self):
        if self.p4Color == "Vermelho":
            self.colorP4.setStyleSheet("background-color: rgb(255, 255, 0);")
            self.p4Color = "Amarelo"
        elif self.p4Color == "Amarelo":
            self.colorP4.setStyleSheet("background-color: rgb(0, 170, 0);")
            self.p4Color = "Verde"
        elif self.p4Color == "Verde":
            self.colorP4.setStyleSheet("background-color: rgb(0, 85, 255);")
            self.p4Color = "Azul"
        else:
            self.colorP4.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.p4Color = "Vermelho"

    
    @pyqtSlot()
    def invalidMatch(self):
        self.warningLayout.show()


    def startMatch(self):
        self.playerColors.append(self.p1Color)
        self.playerColors.append(self.p2Color)
        self.playerNames.append(self.lineEditP1.text())
        self.playerNames.append(self.lineEditP2.text())
        if self.numPlayers == 3:
            self.playerColors.append(self.p3Color)
            self.playerNames.append(self.lineEditP3.text())
        elif self.numPlayers == 4:
            self.playerColors.append(self.p3Color)
            self.playerColors.append(self.p4Color)
            self.playerNames.append(self.lineEditP3.text())
            self.playerNames.append(self.lineEditP4.text())

        self.StartMatchSignal.emit(self.playerNames,self.playerColors)
        self.playerNames.clear()
        self.playerColors.clear()



