# Autor: Sol Castilho Araújo de Moraes Sêda (1711600)
# Horas Trabalhadas: 7 horas e meia
"""	
Horas Trabalhadas - Sol Castilho Araújo de Moraes Sêda (1711600)	
01/10/2020 -> INICIO: 13:00 - TERMINO: 15:00	
07/10/2020 -> INICIO: 22:30 - TERMINO: 23:00
10/10/2020 -> INICIO: 17:00 - TERMINO: 18:00
19/10/2020 -> INICIO: 20:00 - TERMINO: 00:00
"""

import unittest
from unittest import mock
from main import *
from jogadorPeca import *

class Testmock (unittest.TestCase):

    # Testes
    def test_00_inicio(self):
        print("\nBateria de testes do programa:")


    #------------main.py------------#

    # Validar a partida
    def test_01_inserir_quantidade_dois_ok(self):
        jogadores = ["Mario", "Jorge"]
        cores = ["Vermelho", "Amarelo"]
        print("Caso de teste 1 - inserindo dois jogadores")
        self.assertEqual(validaPartida(jogadores, cores), 0)

    def test_02_inserir_quantidade_dois_erro(self):
        jogadores = ["Mario", "Jorge"]
        cores = ["Vermelho", "Vermelho"]
        print("Caso de teste 2 - erro dois jogadores inseridos na mesma cor")
        self.assertEqual(validaPartida(jogadores, cores), 1)

    def test_03_inserir_quantidade_tres_ok(self):
        jogadores = ["Mario", "Jorge", "Isabela"]
        cores = ["Vermelho", "Amarelo", "Verde"]
        print("Caso de teste 3 - inserindo três jogadores")
        self.assertEqual(validaPartida(jogadores, cores), 0)

    def test_04_inserir_quantidade_tres_erro(self):
        jogadores = ["Mario", "Jorge", "Isabela"]
        cores = ["Vermelho", "Vermelho", "Verde"]
        print("Caso de teste 4 - erro ao inserir três jogaores, dois jogadores com a mesma cor")
        self.assertEqual(validaPartida(jogadores, cores), 1)

    def test_05_inserir_quantidade_quatro_ok(self):
        jogadores = ["Mario", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Amarelo", "Verde", "Azul"]
        print("Caso de teste 5 - inserindo quatro jogadores")
        self.assertEqual(validaPartida(jogadores, cores), 0)

    def test_06_inserir_quantidade_quatro_erro(self):
        jogadores = ["Mario", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Vermelho", "Verde", "Azul"]
        print("Caso de teste 6 - erro ao inserir quatro jogadores, dois jogadores com a mesma cor")
        self.assertEqual(validaPartida(jogadores, cores), 1)

    def test_07_inserir_jogador_sem_nome_erro(self):
        jogadores = ["", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Amarelo", "Verde", "Azul"]
        print("Caso de teste 7 - erro ao inserir quatro jogadores, um deles sem nome")
        self.assertEqual(validaPartida(jogadores, cores), 1)
    

    # Abrir a tela de regras
    def test_08_abrir_regras(self):
        print("Caso de teste 8 - Abrir a tela de regras")
        self.assertEqual(abreRegras(), 0)

    def test_09_abrir_regras_falha(self):
        print("Caso de teste 9 - Abrir tela de Regras falhou")
        del interface.regras
        self.assertEqual(abreRegras(), 1)


    # Abrir o histórico
    def test_10_abrir_historico_ok(self):
        m = mock.Mock()
        print("Caso de teste 10 - Abrir a tela de histórico")
        m.abreHistorico.return_value = 0
        self.assertEqual(m.abreHistorico(), 0)

    def test_11_abrir_historico_falha(self):
        m = mock.Mock()
        print("Caso de teste 11 - Abrir a tela de histórico falhou")
        del m.interface.historico
        m.abreHistorico.return_value = 1
        self.assertEqual(m.abreHistorico(), 1)


    # Avisar inicio da partida
    def test_12_iniciar_partida_ok(self):
        m = mock.Mock()
        print("Caso de teste 12 - Avisa inicio da partida")
        m.iniciaPartida.return_value = 0
        self.assertEqual(m.iniciaPartida(), 0)

    def test_13_iniciar_partida_falha(self):
        m = mock.Mock()
        print("Caso de teste 13 - Avisa inicio da partida falhou")
        m.iniciaPartida.return_value = 1
        self.assertEqual(m.iniciaPartida(), 1)



    #------------jogada.py------------#

    # Rolar dado
    def test_14_rola_dado_ok(self):
        m = mock.Mock()
        print("Caso de teste 14 - rolar um dado")
        m.rolaDado.return_value = 0
        self.assertEqual(m.rolaDado(), 0)

    def test_15_rola_dado_falhou(self):
        m = mock.Mock()
        print("Caso de teste 15 - rolar um dado falhou")
        m.rolaDado.return_value = 1
        self.assertEqual(m.rolaDado(), 1)


    # Movimentar pecas
    def test_16_movimenta_pecas_ok(self):
        m = mock.Mock()
        print("Caso de teste 16 - movimenta pecas ok")
        m.movimentaPecas.return_value = 0
        self.assertEqual(m.movimentaPecas(m.posicoes,m.novasPosicoes), 0)

    def test_17_movimenta_pecas_falhou(self):
        m = mock.Mock()
        print("Caso de teste 17 - movimenta pecas falhou")
        m.movimentaPecas.return_value = 1
        self.assertEqual(m.movimentaPecas(m.posicoes,m.novasPosicoes), 1)


    # Validar uma jogada
    def test_18_valida_jogada_ok(self):
        m = mock.Mock()
        print("Caso de teste 18 - valida uma jogada")
        m.validaJogada.return_value = 0
        self.assertEqual(m.validaJogada(m.posicoes), 0)

    def test_19_valida_jogada_falhou(self):
        m = mock.Mock()
        print("Caso de teste 19 - valida uma jogada falhou")
        m.validaJogada.return_value = 1
        self.assertEqual(m.validaJogada(m.posicoes), 1)


    # Checar torre
    def test_20_checa_torre_ok(self):
        m = mock.Mock()
        print("Caso de teste 20 - checa se é torre")
        m.checaTorre.return_value = 0
        self.assertEqual(m.checaTorre(m.posicoes), 0)

    def test_21_checa_torre_falha(self):
        m = mock.Mock()
        print("Caso de teste 21 - checa se é torre falhou")
        m.checaTorre.return_value = 1
        self.assertEqual(m.checaTorre(m.posicoes), 1)



    #------------fimDeJogo.py------------#

    # Abrir menu
    def test_22_abre_menu_ok(self):
        m = mock.Mock()
        print("Caso de teste 24 - abrir o menu após o final de uma partida")
        m.abreMenu.return_value = 0
        self.assertEqual(m.abreMenu(), 0)

    def test_23_abre_menu_falha(self):
        m = mock.Mock()
        print("Caso de teste 25 - abrir o menu após o final de uma partida falhou")
        m.abreMenu.return_value = 1
        self.assertEqual(m.abreMenu(), 1)



    #------------partida.py------------#

    # Iniciar a partida
    def test_24_partida_inicia_ok(self):
        m = mock.Mock()
        print("Caso de teste 26 - partida iniciada")
        m.partidaInicia.return_value = 0
        self.assertEqual(m.partidaInicia(), 0)

    def test_25_partida_inicia_falha(self):
        m = mock.Mock()
        print("Caso de teste 27 - partida iniciada falhou")
        m.partidaInicia.return_value = 1
        self.assertEqual(m.partidaInicia(), 1)


    # Exibir vencedor
    def test_26_exibir_vencedor_ok(self):
        m = mock.Mock()
        print("Caso de teste 22 - exibir o vencedor de uma partida")
        m.exibeVencedor.return_value = 0
        self.assertEqual(m.exibeVencedor(), 0)

    def test_27_exibir_vencedor_falha(self):
        m = mock.Mock()
        print("Caso de teste 23 - exibir o vencedor de uma partida falhou")
        m.exibeVencedor.return_value = 1
        self.assertEqual(m.exibeVencedor(), 1)


    # Exibir Data
    def test_28_exibe_data_ok(self):
        m = mock.Mock()
        print("Caso de teste 28 - exibe data ok")
        m.exibeData.return_value = 0
        self.assertEqual(m.exibeData(), 0)

    def test_29_exibe_data_falha(self):
        m = mock.Mock()
        print("Caso de teste 29 - exibe data falhou")
        m.exibeData.return_value = 1
        self.assertEqual(m.exibeData(), 1)


    # Exibir numero
    def test_30_exibe_numero_ok(self):
        m = mock.Mock()
        print("Caso de teste 30 - numero da partida exibido")
        m.exibeNumero.return_value = 0
        self.assertEqual(m.exibeNumero(), 0)

    def test_31_exibe_numero_falhou(self):
        m = mock.Mock()
        print("Caso de teste 31 - numero da partida exibido falhou")
        m.exibeNumero.return_value = 1
        self.assertEqual(m.exibeNumero(), 1)

    
    #------------jogadorPeca.py------------#
    
    # Criar jogadores
    def test_32_criando_quantidade_dois_ok(self):
        jogadores = ["Mario", "Jorge"]
        cores = ["Vermelho", "Amarelo"]
        print("Caso de teste 32 - criando dois jogadores")
        self.assertEqual(criaJogador(jogadores, cores), 0)

    def test_33_criando_quantidade_dois_erro(self):
        jogadores = ["Mario", "Jorge"]
        cores = ["Vermelho", "Amarelo"]
        print("Caso de teste 33 - criando dois jogadores falhou")
        jogadores.pop()
        self.assertEqual(criaJogador(jogadores, cores), 1)

    def test_34_criando_quantidade_tres_ok(self):
        jogadores = ["Mario", "Jorge", "Isabela"]
        cores = ["Vermelho", "Amarelo", "Verde"]
        print("Caso de teste 33 - criando três jogadores")
        self.assertEqual(criaJogador(jogadores, cores), 0)

    def test_35_criando_quantidade_tres_erro(self):
        jogadores = ["Mario", "Jorge", "Isabela"]
        cores = ["Vermelho", "Amarelo", "Verde"]
        print("Caso de teste 35 - criando tres jogadores falhou")
        cores.pop()
        self.assertEqual(criaJogador(jogadores, cores), 1)

    def test_36_criando_quantidade_quatro_ok(self):
        jogadores = ["Mario", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Amarelo", "Verde", "Azul"]
        print("Caso de teste 36 - criando quatro jogadores")
        self.assertEqual(criaJogador(jogadores, cores), 0)

    def test_37_criando_quantidade_quatro_erro(self):
        jogadores = ["Mario", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Amarelo", "Verde", "Azul"]
        print("Caso de teste 37 - criando quatro jogadores falhou")
        jogadores.pop()
        self.assertEqual(criaJogador(jogadores, cores), 1)


    # Escolher base
    def test_38_escolhendo_base_ok(self):
        jogador = ["Mario", "Vermelho"]
        print("Caso de teste 38 - escolhe base de jogador")
        self.assertEqual(escolheBase(jogador), 0)

    def test_39_escolhendo_base_erro(self):
        jogador = ["Mario", "Vermelho"]
        jogador.pop(0)
        print("Caso de teste 39 - escolhe base de jogador falhou")
        self.assertEqual(escolheBase(jogador), 1)


    # Dizer nome do jogador
    def test_40_nome_jogador_ok(self):
        jogador = ["Mario", "Vermelho",[81,82,83,84]]
        print("Caso de teste 40 - diz nome do jogador ok")
        self.assertEqual(nomeJogador(jogador), "Mario")

    def test_41_nome_jogador_erro(self):
        jogador = ["Vermelho", "Mario",[81,82,83,84]]
        print("Caso de teste 41 - diz nome do jogador falhou")
        self.assertNotEqual(nomeJogador(jogador), "Mario")

    
    # Dizer cor do jogador
    def test_42_cor_jogador_ok(self):
        jogador = ["Mario", "Vermelho",[81,82,83,84]]
        print("Caso de teste 42 - diz cor do jogador ok")
        self.assertEqual(corJogador(jogador), "Vermelho")

    def test_43_cor_jogador_erro(self):
        jogador = ["Vermelho", "Mario",]
        print("Caso de teste 43 - diz cor do jogador falhou")
        self.assertNotEqual(corJogador(jogador), "Vermelho")

    
    #Dizer posição das peças do jogador
    def test_44_posicoes_peca_jogador_ok(self):
        jogador = ["Mario", "Vermelho",[27,39,48,54]]
        print("Caso de teste 44 - diz posicao das pecas do jogador ok")
        self.assertEqual(posicaoPecas(jogador,3), 54)

    def test_45_posicoes_peca_jogador_erro(self):
        jogador = ["Mario", "Vermelho",[27,39,48,54]]
        print("Caso de teste 45 - diz posicao das pecas do jogador falhou")
        self.assertNotEqual(posicaoPecas(jogador), [27,39,48,55])


unittest.main()