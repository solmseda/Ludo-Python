from Interface.Ui_Menu import Ui_Menu

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from Interface.Regras import Regras
#from Interface.Historico import Historico


class Menu(QMainWindow,Ui_Menu):

    StartMatchSignal = pyqtSignal(list,list)

    def __init__(self):
        super(Menu, self).__init__()
        
        self.setupUi(self)
        #self.historico = Historico()

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
        self.close()



