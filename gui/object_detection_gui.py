# -*- coding: utf-8 -*-

"""
Module implementing object_detection_Dialog.
"""
import os
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from PyQt4 import QtCore, QtGui
from Ui_object_detection import Ui_object_detection_Dialog
import sys
sys.path.append("..")
from app.object_detect import object_detection
class object_detection_Dialog(QDialog, Ui_object_detection_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        打开图片
        """
        # TODO: not implemented yet
        print "打开图片"
        self.imgPath = QtGui.QFileDialog.getOpenFileName(self, u'选择图片', '/', u'Images (*.png *.xpm *.jpg)')
        self.imgPath = unicode(self.imgPath)
        print(self.imgPath)
        #print(os.path.dirname(self.imgPath))
        father_path = os.path.abspath(os.path.dirname(self.imgPath)+os.path.sep+".")
        self.resultPath = os.path.join(father_path, 'object_detection.jpg')
        if(self.imgPath != ''):
            scene = QtGui.QGraphicsScene(self)                # 创建场景
            pixmap = QtGui.QPixmap(self.imgPath)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
            scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
            self.graphicsView.setScene(scene)           # 将场景添加到graphicsView中
            self.graphicsView.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        开始检测
        """
        # TODO: not implemented yet
        print "开始检测"
        fc = object_detection(img_path=self.imgPath)        
        res_img = fc.run() 
        #res_img.show()
        self.res_img_path="object_detection.jpg" 
        #res_img = cv2.cvtColor(res_img, cv2.COLOR_RGB2BGR)
        #cv2.imwrite(self.resultPath, res_img)
        
        scene = QtGui.QGraphicsScene(self)                # 创建场景
        pixmap = QtGui.QPixmap(self.res_img_path)              # 调用QtGui.QPixmap方法，打开一个图片，存放在变量中
        scene.addItem(QtGui.QGraphicsPixmapItem(pixmap))  # 添加图片到场景中
        self.graphicsView_2.setScene(scene)           # 将场景添加到graphicsView中
        self.graphicsView_2.show()                    # 显示
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print "返回"
        self.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = object_detection_Dialog()
    ui.show()
    sys.exit(app.exec_())
