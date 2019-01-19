# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 550)
        MainWindow.setStyleSheet("#MainWindow {background-image:url(./bg2.jpg);}")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(120, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 243, 101);")
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(MainWindow)
        self.graphicsView.setGeometry(QtCore.QRect(0, 120, 241, 231))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 81, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(315, 120, 231, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(360, 80, 111, 31))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 199, 85);")
        self.label_2.setObjectName("label_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(MainWindow)
        self.commandLinkButton.setGeometry(QtCore.QRect(220, 360, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.choose)
        self.commandLinkButton.clicked.connect(MainWindow.recognition)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "发票识别系统"))
        self.label.setText(_translate("MainWindow", "欢迎使用发票识别系统"))
        self.pushButton.setText(_translate("MainWindow", "选择发票"))
        self.label_2.setText(_translate("MainWindow", "识别结果"))
        self.commandLinkButton.setText(_translate("MainWindow", "开始识别"))

