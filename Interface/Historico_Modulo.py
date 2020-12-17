from Interface.Ui_Historico_Modulo import Ui_Historico_Modulo
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt
from jogadorPeca import *



class Historico_Modulo(QWidget,Ui_Historico_Modulo):
    
    def __init__(self, parent = None):
        super(Historico_Modulo, self).__init__()
        self.setupUi(self)

        