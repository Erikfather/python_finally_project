# -*- coding: utf-8 -*-

"""
Module implementing MainWindow2.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore, QtGui
from Ui_window2 import Ui_MainWindow2
from face_rec_gui import face_rec_Dialog

class MainWindow2(QMainWindow, Ui_MainWindow2):
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
        
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        人脸识别
        """
        # TODO: not implemented yet
        self.dialog=face_rec_Dialog()
        self.dialog.show()
        #self.close()
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow2()
    ui.show()
    sys.exit(app.exec_())
    
   
