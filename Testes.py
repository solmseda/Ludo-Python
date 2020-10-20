# Autor: Sol Castilho Araújo de Moraes Sêda (1711600)
# Horas Trabalhadas:
"""	
Horas Trabalhadas - Sol Castilho Araújo de Moraes Sêda (1711600)	
01/10/2020 -> INICIO: 13:00 - TERMINO: 15:00	
07/10/2020 -> INICIO: 22:30 - TERMINO: 22:00
10/10/2020 -> INICIO: 17:00 - TERMINO: 18:00
19/10/2020 -> INICIO: 20:00 - TERMINO: 
         

"""
import unittest
from unittest import mock
#import main

class Testmock (unittest.TestCase):

    #------------Menu.py------------#
    # Inserindo a quantidade de jogadores
    def test_01_inserir_quantidade_dois_ok(self):
        m = mock.Mock()
        jogadores = ["Mario", "Jorge"]
        cores = ["Vermelho", "Amarelo"]
        print("Caso de teste 1 - inserindo dois jogadores ")
        m.valida_partida.return_value = 0
        self.assertEqual(m.valida_partida(jogadores, cores), 0)
        #self.assertEqual(main.valida_partida(jogadores, cores), 0)

    def test_02_inserir_quantidade_dois_erro(self):
        m = mock.Mock()
        jogadores = ["Mario", "Jorge"]
        cores = ["Vermelho", "Vermelho"]
        print("Caso de teste 2 - erro dois jogadores inseridos na mesma cor")
        m.valida_partida.return_value = 1
        self.assertEqual(m.valida_partida(jogadores, cores), 1)
        #self.assertEqual(main.valida_partida(jogadores, cores), 1)

    def test_03_inserir_quantidade_tres_ok(self):
        m = mock.Mock()
        jogadores = ["Mario", "Jorge", "Isabela"]
        cores = ["Vermelho", "Amarelo", "Verde"]
        print("Caso de teste 3 - inserindo três jogadores")
        m.valida_partida.return_value = 0
        self.assertEqual(m.valida_partida(jogadores, cores), 0)
        #self.assertEqual(main.valida_partida(jogadores, cores), 0)

    def test_04_inserir_quantidade_tres_erro(self):
        m = mock.Mock()
        jogadores = ["Mario", "Jorge", "Isabela"]
        cores = ["Vermelho", "Vermelho", "Verde"]
        print("Caso de teste 4 - erro ao inserir três jogaores, dois jogadores com a mesma cor")
        m.valida_partida.return_value = 1
        self.assertEqual(m.valida_partida(jogadores, cores), 1)
        #self.assertEqual(main.valida_partida(jogadores, cores), 1)

    def test_05_inserir_quantidade_quatro_ok(self):
        m = mock.Mock()
        jogadores = ["Mario", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Vermelho", "Verde", "Azul"]
        print("Caso de teste 5 - inserindo quatro jogadores")
        m.valida_partida.return_value = 0
        self.assertEqual(m.valida_partida(jogadores, cores), 0)
        #self.assertEqual(main.valida_partida(jogadores, cores), 0)

    def test_06_inserir_quantidade_quatro_erro(self):
        m = mock.Mock()
        jogadores = ["Mario", "Jorge", "Isabela", "Maria"]
        cores = ["Vermelho", "Vermelho", "Verde", "Azul"]
        print("Caso de teste 6 - erro ao inserir quatro jogadores, dois jogadores com a mesma cor")
        m.valida_partida.return_value = 1
        self.assertEqual(m.valida_partida(jogadores, cores), 1)
        #self.assertEqual(main.valida_partida(jogadores, cores), 1)


    # inserindo um jogador
    def test_07_inserir_jogador_ok_condicao_retorno(self):
        m = mock.Mock()
        print("Caso de teste 7 - Inserir com sucesso")
        m.jogador_insere().return_value = 0
        m.jogador_insere.return_value = 0
        self.assertEqual(m.jogador_insere("Mario", "azul"), 0)

    def test_08_verifica_jogador_inserido_com_sucesso(self):            #DANDO ERRO
        m = mock.Mock()
        m.lista_jogadores.nome = 'Mario'
        m.lista_jogadores.cor = 'azul'
        print("Caso de teste 8 - verifica insercão")
        self.assertIn({'nome': 'Mario', 'cor': 'azul'}, m.lista_jogadores())

    def test_09_inserir_jogador_ja_existente(self):            #DANDO ERRO
        m = mock.Mock()
        print("Caso de teste 9 - inserir jogador ja existente")
        retorno_esperado = m.jogador_insere("Mario", "Azul")
        self.assertEqual(retorno_esperado, 1)


    # Abrir a tela de regras
    def test_10_abrir_regras_ok(self):
        m = mock.Mock()
        print("Caso de teste 10 - Abrir a tela de regras")
        m.abre_regras.return_value = 0
        self.assertEqual(m.abre_regras(), 0)

    def test_11_abrir_regras_falha(self):
        m = mock.Mock()
        print("Caso de teste 11 - Abrir tela de Regras falhou")
        m.abre_regras.return_value = 1
        self.assertEqual(m.abre_regras(), 1)


    # Abrir o histórico
    def test_12_abrir_historico_ok(self):
        m = mock.Mock()
        print("Caso de teste 12 - Abrir a tela de histórico")
        m.abre_historico.return_value = 0
        self.assertEqual(m.abre_historico(), 0)

    def test_13_abrir_historico_falha(self):
        m = mock.Mock()
        print("Caso de teste 13 - Abrir a tela de histórico falhou")
        m.abre_historico.return_value = 1
        self.assertEqual(m.abre_historico(), 1)


    # iniciar a partida
    def test_14_iniciar_partida_ok(self):
        m = mock.Mock()
        print("Caso de teste 14 - Iniciar a partida")
        m.iniciar_partida.return_value = 0
        self.assertEqual(m.iniciar_partida(), 0)

    def test_15_iniciar_partida_falha(self):
        m = mock.Mock()
        print("Caso de teste 15 - Iniciar a partida falhou")
        m.iniciar_partida.return_value = 1
        self.assertEqual(m.iniciar_partida(), 1)


    # teste de uma jogada
    def test_16_realizar_jogada_ok(self):
        m = mock.Mock()
        print("Caso de teste 16 - realizar uma jogada")
        retorno_esperado = m.movimenta(m.posicao(), m.novas_posicoes())
        self.assertEqual(retorno_esperado, 0)

    def test_17_realizar_jogada_falha(self):
        m = mock.Mock()
        print("Caso de teste 17- realizar uma jogada falhou")
        retorno_esperado = m.movimenta(m.posicao(), m.novas_posicoes())
        self.assertEqual(retorno_esperado, 1)

    #------------partida.py------------#
    #exibir vencedor
    def test_18_exibir_vencedor_ok(self):
        m = mock.Mock()
        print("Caso de teste 18 - exibir o vencedor de uma partida")
        m.exibe_vencedor.return_value = 0
        self.assertEqual(m.exibe_vencedor(), 0)

    def test_19_exibir_vencedor_falha(self):
        m = mock.Mock()
        print("Caso de teste 19 - exibir o vencedor de uma partida")
        m.exibe_vencedor.return_value = 1
        self.assertEqual(m.exibe_vencedor(), 1)

    def test_20_abre_menu_ok(self):
        m = mock.Mock()
        print("Caso de teste 20 - abrir o menu após o final de uma partida")
        m.abre_menu.return_value = 0
        self.assertEqual(m.abre_menu(), 0)

    
    
unittest.main()