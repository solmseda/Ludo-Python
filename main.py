from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QColorDialog, QMainWindow
from Interface.Menu import Menu
from Interface.Regras import Regras
import sys

app = QApplication(sys.argv)


class Interface(QObject):
    IniciaPartida = pyqtSignal(list,list)
    PartidaInvalida = pyqtSignal()
    def __init__(self):
        super(Interface, self).__init__()
        self.menu = Menu()
        self.regras = Regras()
        self.menu.show()
        self.menu.StartMatchSignal.connect(valida_partida)
        self.menu.pushButtonRules.clicked.connect(abre_regras)
        #self.menu.pushButtonHistory.clicked.connect(abre_historico)
        self.PartidaInvalida.connect(self.menu.invalidMatch)

    
@pyqtSlot(list,list)
def valida_partida(nomesJogadores,coresJogadores):
    numJogadores= len(nomesJogadores)
    if numJogadores == 2:
        if (coresJogadores[0] != coresJogadores[1]) and (nomesJogadores[0] != nomesJogadores[1]) and (nomesJogadores[0] != "" and nomesJogadores[1] != ""):
            interface.IniciaPartida.emit(nomesJogadores,coresJogadores)
            print("2")
            return 0
    elif numJogadores == 3:
        if (coresJogadores[0] != coresJogadores[1] and coresJogadores[0] != coresJogadores[2] and coresJogadores[1] != coresJogadores[2]) and (nomesJogadores[0] != nomesJogadores[1] and nomesJogadores[0] != nomesJogadores[2] and nomesJogadores[1] != nomesJogadores[2]) and (nomesJogadores[0] != "" and nomesJogadores[1] != "" and nomesJogadores[2] != ""):
            interface.IniciaPartida.emit(nomesJogadores,coresJogadores)
            print("3")
            return 0
    elif numJogadores == 4:
        if (coresJogadores[0] != coresJogadores[1] and coresJogadores[0] != coresJogadores[2] and coresJogadores[0] != coresJogadores[3] and coresJogadores[1] != coresJogadores[2] and coresJogadores[1] != coresJogadores[3] and coresJogadores[2] != coresJogadores[3]) and (nomesJogadores[0] != nomesJogadores[1] and nomesJogadores[0] != nomesJogadores[2] and nomesJogadores[0] != nomesJogadores[3] and nomesJogadores[1] != nomesJogadores[2] and nomesJogadores[1] != nomesJogadores[3] and nomesJogadores[2] != nomesJogadores[3]) and (nomesJogadores[0] != "" and nomesJogadores[1] != "" and nomesJogadores[2] != "" and nomesJogadores[3] != ""):
            interface.IniciaPartida.emit(nomesJogadores,coresJogadores)
            print("4")
            return 0
    interface.PartidaInvalida.emit()
    return 1


@pyqtSlot()
def abre_regras():
    try:
        interface.regras.show()
        return 0
    except:
        return 1


"""
@pyqtSlot()
def abre_historico():
    try:
        interface.historico.show()
        return 0
    except:
        return 1
"""

interface = Interface()
sys.exit(app.exec_())