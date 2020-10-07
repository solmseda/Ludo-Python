from Ui_Regras import Ui_Regras
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class Regras(QWidget,Ui_Regras):
    
    def __init__(self):
        super(Regras, self).__init__()
        self.setupUi(self)
        self.pushButtonConfirm.clicked.connect(self.close)
        
import sys
app = QApplication(sys.argv)
a = Regras()
a.show()
sys.exit(app.exec_())