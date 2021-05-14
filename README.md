# Ludo-Python

[![Python Version](https://img.shields.io/badge/python-3.8-blue?logo=python)](https://www.python.org/downloads/)

---

Jogo de Ludo, com interface gráfica, implementado em Python.

[Metodo de Implementação]()

---

### Testes

Para rodar os testes deve-se abrir e arquivo Testes.py e rodar de acordo com a ide utilizada;
**Exemplo**: Para a produção dos testes foi utilizado o **VSCode**, nesta ide deve-se pressionar ```Ctrl + F5``` para rodar o programa.

### Interface

Para testar a interface gráfica, é necessário possuir instalado com **pip** o **pyqt5**, junto da extensão **PYQT Integration**.
Rode o módulo main.py, uma janela irá se abrir.

### Como Jogar

1. Ao clicar em Jogar
	1. Na tela que surgir digite a quantidade de jogadores desejada (minimo 2 e máximo 4)
	2. Digite o nome do primeiro jogador e clique no botao ao lado para escolher a cor (cada clique mostra uma das 4 cores disponiveis)
	3. Repita o passo (1.2) para os jogadores seguintes
	4. Caso clique em Iniciar Partida:
		1. Se não houver nomes e cores repitidos, serão enviados ao modulo jogadorPeca vetores contendo os nomes e cores de todos os jogadores confirmados. Em seguida os jogadores serão gerados, assim como um sinal para iniciar a partida. O programa fechará por ainda não haver o módulo partida
		2. Se houver nomes ou cores repitidos, aparecerá um aviso na tela indicando ser necessário alterá-los e os jogadores e partida não serão iniciados neste momento
	5. Caso clique em Voltar ao Menu, o menu irá retornar a tela anterior
2. Ao clicar em Regras
	1. Aparecerá uma tela mostrando as regras do jogo irá
	2. Para fechar essa tela clique no botão Ok situado no meio inferior
3. Ao clicar em Histórico nada acontece pelo o mesmo ainda não ter sido implementado
4. Ao clicar em Sair o programa encerrara



