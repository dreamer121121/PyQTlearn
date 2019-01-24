# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Children.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(297, 382)
        self.label = QtWidgets.QLabel(ChildrenForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(ChildrenForm)
        self.lineEdit.setGeometry(QtCore.QRect(80, 150, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "ChildrenForm"))
        self.label.setText(_translate("ChildrenForm", "我是一个子窗口"))

