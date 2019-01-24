# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(446, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 431, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actiondakai = QtWidgets.QAction(MainWindow)
        self.actiondakai.setObjectName("actiondakai")
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        self.actionxinjian.setObjectName("actionxinjian")
        self.actiongaunbi = QtWidgets.QAction(MainWindow)
        self.actiongaunbi.setObjectName("actiongaunbi")
        self.addwindowaction = QtWidgets.QAction(MainWindow)
        self.addwindowaction.setObjectName("addwindowaction")
        self.actionSecond = QtWidgets.QAction(MainWindow)
        self.actionSecond.setObjectName("actionSecond")
        self.menu.addAction(self.actiondakai)
        self.menu.addAction(self.actionxinjian)
        self.menu.addAction(self.actiongaunbi)
        self.menu_2.addSeparator()
        self.menu_2.addSeparator()
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.addwindowaction)
        self.toolBar.addAction(self.actionSecond)

        self.retranslateUi(MainWindow)
        self.toolBar.actionTriggered['QAction*'].connect(MainWindow.showchildren)
        self.toolBar.actionTriggered['QAction*'].connect(MainWindow.slot1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件(&F)"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actiondakai.setText(_translate("MainWindow", "打开"))
        self.actiondakai.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionxinjian.setText(_translate("MainWindow", "新建"))
        self.actionxinjian.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actiongaunbi.setText(_translate("MainWindow", "关闭"))
        self.actiongaunbi.setShortcut(_translate("MainWindow", "Alt+C"))
        self.addwindowaction.setText(_translate("MainWindow", "添加窗体"))
        self.actionSecond.setText(_translate("MainWindow", "添加第二个窗体"))

