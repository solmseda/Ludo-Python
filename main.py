# Autor: Victor Nielsen Ribeirete (1811545)
# Horas Trabalhadas: 20 Horas


from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QColorDialog, QMainWindow
from Interface.Menu import Menu
from Interface.Regras import Regras
from Interface.Tabuleiro import Tabuleiro
from Interface.Ui_FimdeJogo import Ui_Form
import sys
import jogadorPeca
import partida


__all__ = ["interface","validaPartida","abreRegras"]
"""
Gera classe somente para lidar com os sinais enviados entre as interfaces.
É necessário herdar as propriedades do QObject para trabalhar com os eventos
"""
class Interface(QObject):
    IniciaPartida = pyqtSignal()
    CriaJogador = pyqtSignal(list,list)
    PartidaInvalida = pyqtSignal()
    NovaJogada = pyqtSignal(bool)
    def __init__(self):
        super(Interface, self).__init__()
        self.menu = Menu()
        self.regras = Regras()
        self.tabuleiro = Tabuleiro()
        self.menu.StartMatchSignal.connect(validaPartida)
        self.menu.pushButtonRules.clicked.connect(abreRegras)
        #self.menu.pushButtonHistory.clicked.connect(abreHistorico)
        self.PartidaInvalida.connect(self.menu.invalidMatch)
        self.CriaJogador.connect(jogadorPeca.criaJogador)
        self.menu.show()


#Recebe os nomes e cores dos jogadores providos pela inteface do Menu e checa se são todos diferentes para validar ou não a partida
@pyqtSlot(list,list)
def validaPartida(nomesJogadores,coresJogadores):
    numJogadores= len(nomesJogadores)
    if numJogadores == 2:
        if (coresJogadores[0] != coresJogadores[1]) and (nomesJogadores[0] != nomesJogadores[1]) and (nomesJogadores[0] != "" and nomesJogadores[1] != ""):
            interface.CriaJogador.emit(nomesJogadores,coresJogadores)
            partida.iniciaPartida()
            interface.menu.close()
            return 0
    elif numJogadores == 3:
        if (coresJogadores[0] != coresJogadores[1] and coresJogadores[0] != coresJogadores[2] and coresJogadores[1] != coresJogadores[2]) and (nomesJogadores[0] != nomesJogadores[1] and nomesJogadores[0] != nomesJogadores[2] and nomesJogadores[1] != nomesJogadores[2]) and (nomesJogadores[0] != "" and nomesJogadores[1] != "" and nomesJogadores[2] != ""):
            interface.CriaJogador.emit(nomesJogadores,coresJogadores)
            interface.menu.close()
            partida.iniciaPartida()
            return 0
    elif numJogadores == 4:
        if (coresJogadores[0] != coresJogadores[1] and coresJogadores[0] != coresJogadores[2] and coresJogadores[0] != coresJogadores[3] and coresJogadores[1] != coresJogadores[2] and coresJogadores[1] != coresJogadores[3] and coresJogadores[2] != coresJogadores[3]) and (nomesJogadores[0] != nomesJogadores[1] and nomesJogadores[0] != nomesJogadores[2] and nomesJogadores[0] != nomesJogadores[3] and nomesJogadores[1] != nomesJogadores[2] and nomesJogadores[1] != nomesJogadores[3] and nomesJogadores[2] != nomesJogadores[3]) and (nomesJogadores[0] != "" and nomesJogadores[1] != "" and nomesJogadores[2] != "" and nomesJogadores[3] != ""):
            interface.CriaJogador.emit(nomesJogadores,coresJogadores)
            interface.menu.close()
            partida.iniciaPartida()
            return 0
    interface.PartidaInvalida.emit()
    return 1



#Abre a interface com as regras do jogo
@pyqtSlot()
def abreRegras():
    try:
        interface.regras.show()
        return 0
    except:
        return 1


#Irá abrir a interface com o histórico de partidas com os nomes dos jogadores de cada partida e o vencedor
"""
@pyqtSlot()
def abreHistorico():
    try:
        interface.historico.show()
        return 0
    except:
        return 1
"""

app = QApplication(sys.argv)
interface = Interface()
if __name__ == "__main__":
    sys.exit(app.exec_())