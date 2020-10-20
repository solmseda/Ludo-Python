# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\victo\Desktop\PUC\Modular\Projeto\Ludo-Python\Regras.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Autor: Victor Nielsen Ribeirete (1811545)
# Horas Trabalhadas: 1 Hora e meia

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Regras(object):
    def setupUi(self, Regras):
        Regras.setObjectName("Regras")
        Regras.resize(1300, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Regras.sizePolicy().hasHeightForWidth())
        Regras.setSizePolicy(sizePolicy)
        Regras.setMinimumSize(QtCore.QSize(1300, 800))
        Regras.setMaximumSize(QtCore.QSize(1300, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagens/ludo_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Regras.setWindowIcon(icon)
        Regras.setStyleSheet("QWidget#Regras {\n"
"background-color: qlineargradient(spread:pad, x1:0.492588, y1:0, x2:0.492, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"border: 1px solid;\n"
"border-radius: 4;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Regras)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoLayout = QtWidgets.QWidget(Regras)
        self.infoLayout.setMinimumSize(QtCore.QSize(0, 0))
        self.infoLayout.setObjectName("infoLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.infoLayout)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelRules = QtWidgets.QLabel(self.infoLayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRules.sizePolicy().hasHeightForWidth())
        self.labelRules.setSizePolicy(sizePolicy)
        self.labelRules.setMinimumSize(QtCore.QSize(819, 394))
        self.labelRules.setMaximumSize(QtCore.QSize(950, 699))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.labelRules.setFont(font)
        self.labelRules.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"border: 1px solid;\n"
"border-radius: 4;\n"
"border-color: rgb(255, 255, 255);")
        self.labelRules.setTextFormat(QtCore.Qt.AutoText)
        self.labelRules.setScaledContents(False)
        self.labelRules.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelRules.setIndent(5)
        self.labelRules.setObjectName("labelRules")
        self.horizontalLayout_2.addWidget(self.labelRules)
        self.imagesLayout = QtWidgets.QWidget(self.infoLayout)
        self.imagesLayout.setMaximumSize(QtCore.QSize(300, 16777215))
        self.imagesLayout.setObjectName("imagesLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.imagesLayout)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TokenLabel = QtWidgets.QLabel(self.imagesLayout)
        self.TokenLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TokenLabel.setFont(font)
        self.TokenLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.TokenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TokenLabel.setObjectName("TokenLabel")
        self.verticalLayout_2.addWidget(self.TokenLabel)
        self.imageToken = QtWidgets.QLabel(self.imagesLayout)
        self.imageToken.setStyleSheet("image: url(:/Imagens/peca.png);")
        self.imageToken.setText("")
        self.imageToken.setObjectName("imageToken")
        self.verticalLayout_2.addWidget(self.imageToken)
        self.BoardLabel = QtWidgets.QLabel(self.imagesLayout)
        self.BoardLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BoardLabel.setFont(font)
        self.BoardLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.BoardLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BoardLabel.setObjectName("BoardLabel")
        self.verticalLayout_2.addWidget(self.BoardLabel)
        self.imageBoard = QtWidgets.QLabel(self.imagesLayout)
        self.imageBoard.setMaximumSize(QtCore.QSize(16777215, 282))
        self.imageBoard.setStyleSheet("image: url(:/Imagens/Ludo_board.png);")
        self.imageBoard.setText("")
        self.imageBoard.setObjectName("imageBoard")
        self.verticalLayout_2.addWidget(self.imageBoard)
        self.horizontalLayout_2.addWidget(self.imagesLayout)
        self.verticalLayout.addWidget(self.infoLayout)
        self.layoutButton = QtWidgets.QWidget(Regras)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutButton.sizePolicy().hasHeightForWidth())
        self.layoutButton.setSizePolicy(sizePolicy)
        self.layoutButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.layoutButton.setBaseSize(QtCore.QSize(0, 0))
        self.layoutButton.setStyleSheet("")
        self.layoutButton.setObjectName("layoutButton")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutButton)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonConfirm = QtWidgets.QPushButton(self.layoutButton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonConfirm.sizePolicy().hasHeightForWidth())
        self.pushButtonConfirm.setSizePolicy(sizePolicy)
        self.pushButtonConfirm.setMinimumSize(QtCore.QSize(80, 30))
        self.pushButtonConfirm.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonConfirm.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-bottom-color: rgb(0, 0, 0);\n"
"    border-right-color: rgb(0, 0, 0);\n"
"    border-radius: 4;\n"
"    \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(180,180,180);\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    \n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"    \n"
"    background-color: rgb(80, 80, 80);\n"
"}")
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.horizontalLayout.addWidget(self.pushButtonConfirm)
        self.verticalLayout.addWidget(self.layoutButton, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Regras)
        QtCore.QMetaObject.connectSlotsByName(Regras)

    def retranslateUi(self, Regras):
        _translate = QtCore.QCoreApplication.translate
        Regras.setWindowTitle(_translate("Regras", "Regras"))
        self.labelRules.setText(_translate("Regras", "<html><head/><body><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">Cada jogador por sua vez lança um dado</span><span style=\" font-family:\'sans-serif\'; color:#202122;\"> e faz avançar um dos seus peões em jogo o número de casas</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122;\">indicado. O seis permite colocar em jogo um peão que esteja na casa inicial ou fazer avançar um peão seis </span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122;\">casas, e ainda um novo lançamento de dados. O número um também permite que o jogador tire o peão, </span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122;\">mas é só o seis que permite o jogador a lançar o dado novamente. </span></p><p>.</p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">Quando o jogador entra com um peão na parte final, poderá completar o percurso somente se tirar o </span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">número de casas exato da casa final. Caso tire um número maior, o jogador entra e retrocede o número</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">das casas que sobraram.</span><br/>.</p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">Não é permitido mais do que um peão em cada casa. Caso um peão venha a ocupar uma casa ocupada</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">por um peão de outro jogador, o peão original regressará à casa inicial, é o chamado &quot;comer&quot;</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">(principalmente no Brasil</span><span style=\" font-family:\'sans-serif\'; color:#202122;\">). É proibido &quot;comer&quot; o adversário que está na casa de saída.</span></p><p>.</p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">Quando dois peões de uma mesma cor se encontram em uma mesma casa, forma-se uma torre,</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">impedindo outro peão de ocupar esta casa. Só poderá comer a torre com outra torre. Dois peões</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">somente poderão caminhar como torre (ou seja, ambos juntos) caso haja uma torre no meio do</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">caminho para ser &quot;comida&quot; uma vez que somente uma torre poderá comer outra, mandando os dois</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">peões para casa inicial. Não havendo outra torre, e lançando o dado, o jogador deverá desfazer a</span></p><p><span style=\" font-family:\'sans-serif\'; color:#202122; background-color:#ffffff;\">torre, caminhando somente com um dos peões.</span></p></body></html>"))
        self.TokenLabel.setText(_translate("Regras", "Peças e Dado:"))
        self.BoardLabel.setText(_translate("Regras", "Tabuleiro:"))
        self.pushButtonConfirm.setText(_translate("Regras", "OK"))
import Interface.Resources.resources_rc
