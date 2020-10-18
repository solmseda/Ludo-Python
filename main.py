from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QColorDialog, QMainWindow
from Interface.Menu import Menu
import sys

app = QApplication(sys.argv)
window = Menu()
window.show()

sys.exit(app.exec_())


