# Autores: Eduardo Sardenberg e Victor Nielsen (1711600 e 1811545)
# Horas Trabalhadas ao todo: 8 horas e meia
"""	
Horas Trabalhadas - Eduardo Sardenberg e Victor Nielsen (1711600 e 1811545)
19/10/2020 -> INICIO: 20:00 - TERMINO: 20/10/2020 04:30
"""

from PyQt5.QtCore import pyqtSlot

__all__ = ["criaJogador","posicaoJogadorPecas", "nomeJogador", "corJogador"]

Jogador_1 = []
Jogador_2 = []
Jogador_3 = []
Jogador_4 = []

#Recebe as nomes e cores dos jogadores escolhidos na interface e cria os jogadores necessários para a partida
@pyqtSlot(list,list)
def criaJogador(nomesJogadores,coresJogadores):
    numJogadores = len(nomesJogadores)
    
    Jogador_1.append(nomesJogadores[0])
    Jogador_1.append(coresJogadores[0])
    escolheBase(Jogador_1)
    __all__.append(Jogador_1)

    Jogador_2.append(nomesJogadores[1])
    Jogador_2.append(coresJogadores[1])
    escolheBase(Jogador_2)
    __all__.append(Jogador_2)

    print(Jogador_1)
    print(Jogador_2)

    if numJogadores == 3:
        Jogador_3.append(nomesJogadores[2])
        Jogador_3.append(coresJogadores[2])
        escolheBase(Jogador_3)
        __all__.append(Jogador_3)

        print(Jogador_3)

    elif numJogadores == 4:
        Jogador_3.append(nomesJogadores[2])
        Jogador_3.append(coresJogadores[2])
        escolheBase(Jogador_3)
        __all__.append(Jogador_3)

        Jogador_4.append(nomesJogadores[3])
        Jogador_4.append(coresJogadores[3])
        escolheBase(Jogador_4)
        __all__.append(Jogador_4)

        print(Jogador_3)
        print(Jogador_4)


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


def posicaoJogadorPecas(Jogador, peca = None):
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
