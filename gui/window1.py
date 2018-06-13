# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow

from Ui_window1 import Ui_MainWindow
from window2 import MainWindow2


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
  
        
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        进入系统
        """
        # TODO: not implemented yet
        print("进入系统")
        self.window2=MainWindow2()
        self.window2.show()
        self.close()
        

import background_image_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
