#Victor - 5 horas


from Interface.Ui_Historico import Ui_Historico

from Interface.Historico_Modulo import Historico_Modulo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from jogadorPeca import *
import bd



class Historico(QWidget,Ui_Historico):
    
    def __init__(self):
        super(Historico, self).__init__()
        self.setupUi(self)
        self.scrollArea.setWidgetResizable(True)
        #self.buttonTrash.clicked.connect(self.clearHistory)


    def fillHistory(self):
        partidas = bd.recuperaPartida()
        for tupla in partidas:
            partida = list(tupla)
            exec("partida_"+str(partida[0])+" = Historico_Modulo(partida)")
            exec("self.scrollAreaWidgetContents.setWidget(partida_"+str(partida[0]))
        return


    def clearHistory(self):
        for i in reversed(range(self.verticalLayoutScrollArea.count())): 
            widgetToRemove = self.verticalLayoutScrollArea.itemAt(i).widget()

            if type(widgetToRemove) == Historico_Modulo:
                self.verticalLayoutScrollArea.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)
        return