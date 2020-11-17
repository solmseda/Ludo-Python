# Autores: Eduardo Sardenberg e Victor Nielsen (1711600 e 1811545)
# Horas Trabalhadas ao todo: 8 horas e meia
"""	
Horas Trabalhadas - Sol Castilho de Moraes Sêda
11/11/2020 -> INICIO: 13:20
14/11/2020 -> INICIO: 14:00 - TERMINO: 19:00
15/11/2020 -> INICIO: 13:00 - TERMINO: 23:00

"""

import random
import jogadorPeca

def rolaDado():
    return random.randint(1, 6)

def checaTorre(jogador, posicao, outroPeao):
    if (jogador[2][0] == posicao):
        outroPeao == jogador [2][0]
        return True
    else if(jogador[2][1] == posicao):
        outroPeao == jogador [2][1]
        return True
    else if(jogador[2][2] == posicao):
        outroPeao == jogador [2][2]
        return True
    else if(jogador[2][3] == posicao):
        outroPeao == jogador [2][3]
        return True
    return False

def validaJogada(Jogador, posicaoAtual, dado, novaPosicao, valida):

    #SAIDA DA BASE
    p1 = 76
    p2 = 80
    p3 = 84
    p4 = 88
    for i in range(0, 3):
        if(posicaoAtual == jogadorPeca.posicaoPecas(Jogador, i)):
            if(Jogador == "Verde"):
                if(Jogador[2][i] == p1+=1):
                    if(dado == 6):
                        valida = True
            else if(Jogador == "Vermelho"):
                if(Jogador[2][i] == p2+=1):
                    if(dado == 6):
                        valida = True
            else if (Jogador == "Azul"):
                if(Jogador[2][i] == p3+=1):
                    if(dado == 6):
                        valida = True
            else if (Jogador == "Amarelo"):
                if(Jogador[2][i] == p4+=1):
                    if(dado == 6):
                        valida = True

    #VERIFICANDO A MOVIMENTACAO DA PECA
    if ((novaPosicao - posicaoAtual) <= 0) or ((novaPosicao - posicaoAtual) > 6):
        valida = False 
        return 1
    else if()
    
    #VERIFICAR PECA COME TORRE (IMPOSSIVEL DE ACONTECER)
    outra
    torre = checaTorre(Jogador_1, novaPosicao, outra)
    if (torre == True):
        valida = False
        return 1

    torre = checaTorre(Jogador_2, novaPosicao, outra)
    if (torre == True):
        valida = False
        return 1
        
    torre = checaTorre(Jogador_3, novaPosicao, outra)
    if (torre == True):
        valida = False
        return 1

    torre = checaTorre(Jogador_4, novaPosicao, outra)
    if (torre == True):
        valida = False
        return 1
    

    valida = True
    return 0


def movimentaPeca(jogadorAtual, posicaoAtual, numDado, novaPosicao):
    valida = false
    validaJogada(posicaoAtual, novaPosicao, valida, numDado)
    if(valida == true):
        #Caso já exista uma peça oponente na nova posição retorna ela para a base e toma o lugar

        #CASO DO JOGADOR ATUAL SER O 1
        if(jogadorAtual == Jogador_1):
            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_2, i)):
                    if(Jogador_2 == "Verde"):
                        Jogador_2[2][i] = p1+=1
                        posicaoAtual = novaPosicao
                    else if(Jogador_2 == "Vermelho"):
                        Jogador_2[2][i] = p2+=1
                        posicaoAtual = novaPosicao
                    else if (Jogador_2 == "Azul"):
                        Jogador_2[2][i] = p3+=1
                        posicaoAtual = novaPosicao
                    else if (Jogador_2 == "Amarelo"):
                        Jogador_2[2][i] = p4+=1
                        posicaoAtual = novaPosicao

            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_3, i)):
                if(Jogador_3 == "Verde"):
                    Jogador_3[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_3 == "Vermelho"):
                    Jogador_3[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_3 == "Azul"):
                    Jogador_3[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_3 == "Amarelo"):
                    Jogador_3[2][i] = p4+=1
                    posicaoAtual = novaPosicao

            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_4, i)):
                if(Jogador_4 == "Verde"):
                    Jogador_4[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_4 == "Vermelho"):
                    Jogador_4[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_4 == "Azul"):
                    Jogador_4[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_4 == "Amarelo"):
                    Jogador_4[2][i] = p4+=1
                    posicaoAtual = novaPosicao
        



        #CASO DO JOGADOR ATUAL SER O 2
        if(jogadorAtual == Jogador_2):
            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_1, i)):
                if(Jogador_1 == "Verde"):
                    Jogador_1[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_1 == "Vermelho"):
                    Jogador_1[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_2 == "Azul"):
                    Jogador_1[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_1 == "Amarelo"):
                    Jogador_1[2][i] = p4+=1
                    posicaoAtual = novaPosicao

            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_3, i)):
                if(Jogador_3 == "Verde"):
                    Jogador_3[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_3 == "Vermelho"):
                    Jogador_3[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_3 == "Azul"):
                    Jogador_3[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_3 == "Amarelo"):
                    Jogador_3[2][i] = p4+=1
                    posicaoAtual = novaPosicao

            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_4, i)):
                if(Jogador_4 == "Verde"):
                    Jogador_4[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_4 == "Vermelho"):
                    Jogador_4[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_4 == "Azul"):
                    Jogador_4[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_4 == "Amarelo"):
                    Jogador_4[2][i] = p4+=1
                    posicaoAtual = novaPosicao


        #CASO DO JOGADOR ATUAL SER O 3
        if(jogadorAtual == Jogador_3):
            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_1, i)):
                if(Jogador_1 == "Verde"):
                    Jogador_1[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_1 == "Vermelho"):
                    Jogador_1[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_1 == "Azul"):
                    Jogador_1[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_1 == "Amarelo"):
                    Jogador_1[2][i] = p4+=1
                    posicaoAtual = novaPosicao
            
            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_2, i)):
                if(Jogador_2 == "Verde"):
                    Jogador_2[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_2 == "Vermelho"):
                    Jogador_2[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_2 == "Azul"):
                    Jogador_2[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_2 == "Amarelo"):
                    Jogador_2[2][i] = p4+=1
                    posicaoAtual = novaPosicao

            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_4, i)):
                if(Jogador_4 == "Verde"):
                    Jogador_4[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_4 == "Vermelho"):
                    Jogador_4[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_4 == "Azul"):
                    Jogador_4[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_4 == "Amarelo"):
                    Jogador_4[2][i] = p4+=1
                    posicaoAtual = novaPosicao


        #CASO DO JOGADOR ATUAL SER O 4
        if(jogadorAtual == Jogador_4):
            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_1, i)):
                if(Jogador_1 == "Verde"):
                    Jogador_1[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_1 == "Vermelho"):
                    Jogador_1[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_1 == "Azul"):
                    Jogador_1[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_1 == "Amarelo"):
                    Jogador_1[2][i] = p4+=1
                    posicaoAtual = novaPosicao
            
            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_2, i)):
                if(Jogador_2 == "Verde"):
                    Jogador_2[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_2 == "Vermelho"):
                    Jogador_2[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_2 == "Azul"):
                    Jogador_2[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_2 == "Amarelo"):
                    Jogador_2[2][i] = p4+=1
                    posicaoAtual = novaPosicao

            p1 = 76
            p2 = 80
            p3 = 84
            p4 = 88
            for i in range(0, 3):
                if(novaPosicao == jogadorPeca.posicaoPecas(Jogador_3, i)):
                if(Jogador_3 == "Verde"):
                    Jogador_3[2][i] = p1+=1
                    posicaoAtual = novaPosicao
                else if(Jogador_3 == "Vermelho"):
                    Jogador_3[2][i] = p2+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_3 == "Azul"):
                    Jogador_3[2][i] = p3+=1
                    posicaoAtual = novaPosicao
                else if (Jogador_3 == "Amarelo"):
                    Jogador_3[2][i] = p4+=1
                    posicaoAtual = novaPosicao

            
        """#caso o jogador esteja tentando mover uma torre
        outroPeao
        torre = checaTorre(jogadorAtual, posicaoAtual, outroPeao)
        if (torre == true):
            if (numDado == 6):
                posicoes = novaPosicao
                outroPeao = novaPosicao"""

        
        #caso de só mover para uma nova posição
        posicoes = novasPosicoes
        return 0
    else:
        return 1
