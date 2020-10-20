from PyQt5.QtCore import pyqtSignal, pyqtSlot
from main import Main

__all__ = ["criaJogador","posicaoJogador"]

class SinaisJogador(Main):
    SinalPosicao = pyqtSignal()
    def __init__(self):
        super(SinaisJogador, self).__init__()


Jogador_1 = []
Jogador_2 = []
Jogador_3 = []
Jogador_4 = []

#Recebe as nomes e cores dos jogadores escolhidos na interface e cria os jogadores necessários para a partida
@pyqtSlot(list,list)
def criaJogador(nomesJogadores,coresJogadores):
    numJogadores = len(nomesJogadores)
    
    if numJogadores == 2:
        Jogador_1.append(nomesJogadores[0])
        Jogador_1.append(coresJogadores[0])
        escolheBase(Jogador_1)
        __all__.append(Jogador_1)

        Jogador_2.append(nomesJogadores[1])
        Jogador_2.append(coresJogadores[1])
        escolheBase(Jogador_2)
        __all__.append(Jogador_2)

    elif numJogadores == 3:
        Jogador_1.append(nomesJogadores[0])
        Jogador_1.append(coresJogadores[0])
        escolheBase(Jogador_1)
        __all__.append(Jogador_1)

        Jogador_2.append(nomesJogadores[1])
        Jogador_2.append(coresJogadores[1])
        escolheBase(Jogador_2)
        __all__.append(Jogador_2)

        Jogador_3.append(nomesJogadores[2])
        Jogador_3.append(coresJogadores[2])
        escolheBase(Jogador_3)
        __all__.append(Jogador_3)

    elif numJogadores == 4:
        Jogador_1.append(nomesJogadores[0])
        Jogador_1.append(coresJogadores[0])
        escolheBase(Jogador_1)
        __all__.append(Jogador_1)

        Jogador_2.append(nomesJogadores[1])
        Jogador_2.append(coresJogadores[1])
        escolheBase(Jogador_2)
        __all__.append(Jogador_2)

        Jogador_3.append(nomesJogadores[2])
        Jogador_3.append(coresJogadores[2])
        escolheBase(Jogador_3)
        __all__.append(Jogador_3)

        Jogador_4.append(nomesJogadores[3])
        Jogador_4.append(coresJogadores[3])
        escolheBase(Jogador_4)
        __all__.append(Jogador_4)

    #Começa partida
    print(Jogador_1)
    print(Jogador_2)
    print(Jogador_3)
    print(Jogador_4)
    #abreTabuleiro()


def escolheBase(Jogador):
    if Jogador[1] == "Verde":
        Jogador.append([77,78,79,80])
    elif Jogador[1] == "Vermelho":
        Jogador.append([81,82,83,84])
    elif Jogador[1] == "Azul":
        Jogador.append([85,86,87,88])
    elif Jogador[1] == "Amarelo":
        Jogador.append([89,90,91,92])


def nomeJogador(Jogador):
    return Jogador[0]


def corJogador(Jogador):
    return Jogador[1]


def posicaoJogador(Jogador, peca = None):
    if peca == None:
        return Jogador[2]
    elif peca == 0:
        return Jogador[2][0]
    elif peca == 1:
        return Jogador[2][1]
    elif peca == 2:
        return Jogador[2][2]
    elif peca == 3:
        return Jogador[2][3]


#def abreTabuleiro()
