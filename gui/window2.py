# -*- coding: utf-8 -*-

"""
Module implementing MainWindow2.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QMainWindow
from PyQt4 import QtCore, QtGui
from Ui_window2 import Ui_MainWindow2
from face_rec_gui import face_rec_Dialog
from meiyan_gui import meiyan_Dialog
from object_detection_gui import object_detection_Dialog
from texture_rec_gui import texture_rec_Dialog
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
        self.setFixedSize(self.width(), self.height())

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
        self.dialog=meiyan_Dialog()
        self.dialog.show()
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print "纹理图片识别"
        self.dialog=texture_rec_Dialog()
        self.dialog.show()
        

    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print "目标检测"
        self.dialog=object_detection_Dialog()
        self.dialog.show()

import background_image_rc
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MainWindow2()
    #ui.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    ui.show()
    sys.exit(app.exec_())
    

