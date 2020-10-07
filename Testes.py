import unittest
from unittest import mockexit


class Testmock (unittest.TestCase):


# Inserindo a quantidade de jogadores
def test_01_inserir_quantidade_dois_ok(self):
    print("Caso de teste 1 - inserindo dois jogadores")
    retorno_esperado = m.jogador_qnt(2)
    self.assetEqual(retorno_esperado, 0)


def test_02_inserir_quantidade_dois_erro(self):
    print("Caso de teste 2 - erro ao inserir dois jogadores")
    retorno_esperado = m.jogador_qnt(2)
    self.assetEqual(retorno_esperado, 1)


def test_03_inserir_quantidade_tres_ok(self):
    print("Caso de teste 3 - inserindo tres jogadores")
    retorno_esperado = m.jogador_qnt(3)
    self.assetEqual(retorno_esperado, 0)


def test_04_inserir_quantidade_dois_erro(self):
    print("Caso de teste 4 - erro ao inserir tres jogadores")
    retorno_esperado = m.jogador_qnt(3)
    self.assetEqual(retorno_esperado, 1)


def test_05_inserir_quantidade_quatro_ok(self):
    print("Caso de teste 5 - inserindo quatro jogadores")
    retorno_esperado = m.jogador_qnt(4)
    self.assetEqual(retorno_esperado, 0)


def test_06_inserir_quantidade_quatro_erro(self):
    print("Caso de teste 6 - erro ao inserir quatro jogadores")
    retorno_esperado = m.jogador_qnt(4)
    self.assetEqual(retorno_esperado, 1)


# inserindo um jogador
def test_07_inserir_jogador_ok_condicao_retorno(self):
    m = mock.Mock()
    print("Caso de teste 7 - Inserir com sucesso")
    retorno_esperado = m.jogador_insere("Mario", "azul")
    self.assertEqual(retorno_esperado, 0)


def test_08_verifica_jogador_inserido_com_sucesso(self):
    m = mock.Mock()
    print("Caso de teste 8 - verifica insercão")
    self.assertIn({'nome': 'Mario', 'cor': 'azul'}, m.lista_jogadores())


def test_09_inserir_jogador_ja_existente(self):
    m = mock.Mock()
    print("Caso de teste 9 - inserir jogador ja existente")
    retorno_esperado = m.jogador_insere("Mario", "Azul")
    self.assertEqual(retorno_esperado, 1)

# abrir a tela de regras
def test_10_abrir_regras_ok(self):
    m = mock.Mock()
    print("Caso de teste 10 - Abrir a tela de regras")
    retorno_esperado = m.abre_regras()
    self.assertEqual(retorno_esperado, 0)


def test_11_abrir_regras_falha(self):
    m = mock.Mock()
    Print("Caso de teste 11 - Abrir tela de Regras FALHA")
    retorno_esperado = m.abre_regras()
    self.assertEqual(retorno_esperado, 1)

test_01_inserir_quantidade_dois_ok()
test_02_inserir_quantidade_dois_erro()
test_03_inserir_quantidade_tres_ok()
test_04_inserir_quantidade_dois_erro()
test_05_inserir_quantidade_quatro_ok()
test_06_inserir_quantidade_quatro_erro()
test_07_inserir_jogador_ok_condicao_retorno()
test_08_verifica_jogador_inserido_com_sucesso()
test_09_inserir_jogador_ja_existente()
test_10_abrir_regras_ok()
test_11_abrir_regras_falha()