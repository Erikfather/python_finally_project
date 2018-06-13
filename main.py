# -*- coding: utf-8 -*-

from gui.window1 import MainWindow
from gui.window2 import MainWindow2
from PyQt4 import QtCore, QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
