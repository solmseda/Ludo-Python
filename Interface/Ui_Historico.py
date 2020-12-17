# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\victo\Desktop\PUC\Modular\Projeto\Ludo-Python\Interface\Historico.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Historico(object):
    def setupUi(self, Historico):
        Historico.setObjectName("Historico")
        Historico.resize(746, 790)
        Historico.setMinimumSize(QtCore.QSize(746, 790))
        Historico.setMaximumSize(QtCore.QSize(746, 790))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Imagens/ludo_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Historico.setWindowIcon(icon)
        Historico.setStyleSheet("QWidget#Historico {\n"
"background-color: rgb(85, 255, 127);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Historico)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(Historico)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.layoutTitle = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.layoutTitle.setObjectName("layoutTitle")
        self.labelTitle = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.layoutTitle.addWidget(self.labelTitle, 0, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(106, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutTitle.addItem(spacerItem)
        self.buttonTrash = QtWidgets.QPushButton(self.horizontalWidget)
        self.buttonTrash.setMaximumSize(QtCore.QSize(50, 16777215))
        self.buttonTrash.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonTrash.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.buttonTrash.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Imagens/trashIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonTrash.setIcon(icon1)
        self.buttonTrash.setIconSize(QtCore.QSize(48, 48))
        self.buttonTrash.setObjectName("buttonTrash")
        self.layoutTitle.addWidget(self.buttonTrash)
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layoutTitle.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.horizontalWidget)
        self.labelColuns = QtWidgets.QLabel(Historico)
        self.labelColuns.setMinimumSize(QtCore.QSize(0, 50))
        self.labelColuns.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelColuns.setFont(font)
        self.labelColuns.setObjectName("labelColuns")
        self.verticalLayout.addWidget(self.labelColuns)
        self.scrollArea = QtWidgets.QScrollArea(Historico)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 630))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 630))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 728, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutScrollArea = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayoutScrollArea.setContentsMargins(0, 0, 9, 0)
        self.verticalLayoutScrollArea.setSpacing(3)
        self.verticalLayoutScrollArea.setObjectName("verticalLayoutScrollArea")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        spacerItem2 = QtWidgets.QSpacerItem(20, 4, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(Historico)
        QtCore.QMetaObject.connectSlotsByName(Historico)

    def retranslateUi(self, Historico):
        _translate = QtCore.QCoreApplication.translate
        Historico.setWindowTitle(_translate("Historico", "Histórico"))
        self.labelTitle.setText(_translate("Historico", "Histórico de Partidas"))
        self.buttonTrash.setToolTip(_translate("Historico", "Deleta todos os registros das partidas jogdas"))
        self.labelColuns.setText(_translate("Historico", "   Nº Partida     |            Vencedor             |    Nº Jogadores    |     Info"))
import Interface.Resources.resources_rc
