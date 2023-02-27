# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot as Slot
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_components()        
 
    def init_components(self):
        self.setWindowTitle('PDI')
        self.showMaximized()
                



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
