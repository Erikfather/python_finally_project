# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wlw/learn_project/python_homework/pyqt_project/gui/window1.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(650, 437)
        MainWindow.setStyleSheet(_fromUtf8("border-image: url(:/bg_pic/bg.jpeg);"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(160, 50, 321, 81))
        self.label.setStyleSheet(_fromUtf8("border-image:url()"))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 200, 121, 31))
        self.pushButton.setStyleSheet(_fromUtf8("border-image:url()"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 250, 121, 31))
        self.pushButton_2.setStyleSheet(_fromUtf8("border-image:url()"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "图片识别系统", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">图 片 识 别 系 统</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "进入系统", None))
        self.pushButton_2.setText(_translate("MainWindow", "退出系统", None))

#import background_image_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

