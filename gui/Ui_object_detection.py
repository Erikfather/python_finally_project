# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wlw/learn_project/python_homework/pyqt_project/gui/object_detection.ui'
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

class Ui_object_detection_Dialog(object):
    def setupUi(self, object_detection_Dialog):
        object_detection_Dialog.setObjectName(_fromUtf8("object_detection_Dialog"))
        object_detection_Dialog.resize(757, 560)
        object_detection_Dialog.setSizeGripEnabled(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(object_detection_Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(object_detection_Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label = QtGui.QLabel(object_detection_Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.graphicsView = QtGui.QGraphicsView(object_detection_Dialog)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout.addWidget(self.graphicsView)
        self.graphicsView_2 = QtGui.QGraphicsView(object_detection_Dialog)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.horizontalLayout.addWidget(self.graphicsView_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton = QtGui.QPushButton(object_detection_Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(object_detection_Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(object_detection_Dialog)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(object_detection_Dialog)
        QtCore.QMetaObject.connectSlotsByName(object_detection_Dialog)

    def retranslateUi(self, object_detection_Dialog):
        object_detection_Dialog.setWindowTitle(_translate("object_detection_Dialog", "目标检测", None))
        self.label_2.setText(_translate("object_detection_Dialog", "原图", None))
        self.label.setText(_translate("object_detection_Dialog", "结果", None))
        self.pushButton.setText(_translate("object_detection_Dialog", "打开图片", None))
        self.pushButton_2.setText(_translate("object_detection_Dialog", "开始检测", None))
        self.pushButton_3.setText(_translate("object_detection_Dialog", "返回", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    object_detection_Dialog = QtGui.QDialog()
    ui = Ui_object_detection_Dialog()
    ui.setupUi(object_detection_Dialog)
    object_detection_Dialog.show()
    sys.exit(app.exec_())

