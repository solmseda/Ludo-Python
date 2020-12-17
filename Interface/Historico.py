from Interface.Ui_Historico import Ui_Historico

from Interface.Historico_Modulo import Historico_Modulo

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from jogadorPeca import *
import bd



class Historico(QWidget,Ui_Historico):
    
    def __init__(self):
        super(Historico, self).__init__()
        self.setupUi(self)
        self.buttonTrash.clicked.connect(self.clearHistory)


    def fillHistory(self):
        partidas = bd.recuperaPartida()
        for tupla in partidas:
            partida = list(tupla)
            exec("partida_"+str(partida[0])+" = Historico_Modulo(partida)")
            exec("self.scrollAreaWidgetContents.setWidget(partida_"+str(partida[0]))
        return


    def clearHistory(self):
        if self.scrollArea is not None:
            while self.scrollArea.count():
                item = self.scrollArea.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
        bd.dropPartida()
        return