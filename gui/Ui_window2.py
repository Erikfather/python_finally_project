# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wlw/learn_project/python_homework/pyqt_project/gui/window2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName(_fromUtf8("MainWindow2"))
        MainWindow2.resize(600, 474)
        MainWindow2.setMaximumSize(QtCore.QSize(600, 474))
        MainWindow2.setStyleSheet(_fromUtf8("border-image: url(:/bg_pic/bg2.jpg);"))
        self.centralWidget = QtGui.QWidget(MainWindow2)
        self.centralWidget.setMaximumSize(QtCore.QSize(618, 16777215))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(441, 106, 91, 33))
        self.pushButton.setStyleSheet(_fromUtf8("border-image:url()"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(441, 238, 91, 33))
        self.pushButton_3.setStyleSheet(_fromUtf8("border-image:url()"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(441, 150, 91, 33))
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image:url()"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(441, 194, 91, 33))
        self.pushButton_4.setStyleSheet(_fromUtf8("border-image:url()"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        MainWindow2.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        MainWindow2.setWindowTitle(_translate("MainWindow2", "图片识别系统", None))
        self.pushButton.setText(_translate("MainWindow2", "人脸识别", None))
        self.pushButton_3.setText(_translate("MainWindow2", "纹理图片识别", None))
        self.pushButton_2.setText(_translate("MainWindow2", "照片美颜", None))
        self.pushButton_4.setText(_translate("MainWindow2", "目标检测", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow2 = QtGui.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())

