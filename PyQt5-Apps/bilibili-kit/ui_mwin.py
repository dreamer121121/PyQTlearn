# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MWin(object):
    def setupUi(self, MWin):
        MWin.setObjectName("MWin")
        MWin.resize(781, 508)
        MWin.setMinimumSize(QtCore.QSize(781, 508))
        MWin.setMaximumSize(QtCore.QSize(781, 514))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        MWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MWin.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MWin)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(30, 30))
        self.tabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab1)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout1Main = QtWidgets.QVBoxLayout()
        self.layout1Main.setSpacing(10)
        self.layout1Main.setObjectName("layout1Main")
        self.layout1T1 = QtWidgets.QHBoxLayout()
        self.layout1T1.setSpacing(6)
        self.layout1T1.setObjectName("layout1T1")
        self.lineEdit_input = QtWidgets.QLineEdit(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setInputMask("")
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.layout1T1.addWidget(self.lineEdit_input)
        self.search = QtWidgets.QPushButton(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.search.setFont(font)
        self.search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/b4"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search.setIcon(icon1)
        self.search.setObjectName("search")
        self.layout1T1.addWidget(self.search)
        self.download = QtWidgets.QPushButton(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download.setFont(font)
        self.download.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/b5"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download.setIcon(icon2)
        self.download.setObjectName("download")
        self.layout1T1.addWidget(self.download)
        self.layout1Main.addLayout(self.layout1T1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(35)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.layout1Main.addWidget(self.tableWidget)
        self.layout1Main.setStretch(0, 1)
        self.layout1Main.setStretch(1, 7)
        self.horizontalLayout.addLayout(self.layout1Main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/b1"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab1, icon3, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.layout2T1 = QtWidgets.QHBoxLayout()
        self.layout2T1.setSpacing(6)
        self.layout2T1.setObjectName("layout2T1")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout2T1.addItem(spacerItem)
        self.startAll = QtWidgets.QPushButton(self.groupBox)
        self.startAll.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startAll.setFont(font)
        self.startAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startAll.setObjectName("startAll")
        self.layout2T1.addWidget(self.startAll)
        self.pauseAll = QtWidgets.QPushButton(self.groupBox)
        self.pauseAll.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pauseAll.setFont(font)
        self.pauseAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pauseAll.setObjectName("pauseAll")
        self.layout2T1.addWidget(self.pauseAll)
        self.clearAll = QtWidgets.QPushButton(self.groupBox)
        self.clearAll.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clearAll.setFont(font)
        self.clearAll.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearAll.setObjectName("clearAll")
        self.layout2T1.addWidget(self.clearAll)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout2T1.addItem(spacerItem1)
        self.videoFolder = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.videoFolder.setFont(font)
        self.videoFolder.setObjectName("videoFolder")
        self.layout2T1.addWidget(self.videoFolder)
        self.openVideoFolder = QtWidgets.QPushButton(self.groupBox)
        self.openVideoFolder.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.openVideoFolder.setFont(font)
        self.openVideoFolder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openVideoFolder.setObjectName("openVideoFolder")
        self.layout2T1.addWidget(self.openVideoFolder)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout2T1.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.layout2T1)
        self.downloadWidget = QtWidgets.QTableWidget(self.groupBox)
        self.downloadWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.downloadWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.downloadWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.downloadWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.downloadWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.downloadWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.downloadWidget.setObjectName("downloadWidget")
        self.downloadWidget.setColumnCount(4)
        self.downloadWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.downloadWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.downloadWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.downloadWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.downloadWidget.setHorizontalHeaderItem(3, item)
        self.downloadWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.downloadWidget.horizontalHeader().setDefaultSectionSize(350)
        self.downloadWidget.horizontalHeader().setStretchLastSection(True)
        self.downloadWidget.verticalHeader().setVisible(False)
        self.downloadWidget.verticalHeader().setDefaultSectionSize(30)
        self.downloadWidget.verticalHeader().setMinimumSectionSize(35)
        self.verticalLayout_3.addWidget(self.downloadWidget)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab2, icon2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab3)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Layout_info = QtWidgets.QVBoxLayout()
        self.Layout_info.setSpacing(6)
        self.Layout_info.setObjectName("Layout_info")
        self.info = QtWidgets.QPlainTextEdit(self.tab3)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.Layout_info.addWidget(self.info)
        self.verticalLayout_2.addLayout(self.Layout_info)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/b2"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab3, icon4, "")
        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab4)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Layout_pay = QtWidgets.QVBoxLayout()
        self.Layout_pay.setSpacing(6)
        self.Layout_pay.setObjectName("Layout_pay")
        self.label_pay = QtWidgets.QLabel(self.tab4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pay.setFont(font)
        self.label_pay.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pay.setObjectName("label_pay")
        self.Layout_pay.addWidget(self.label_pay)
        self.Layout_2pay = QtWidgets.QHBoxLayout()
        self.Layout_2pay.setSpacing(6)
        self.Layout_2pay.setObjectName("Layout_2pay")
        self.alipay = QtWidgets.QLabel(self.tab4)
        self.alipay.setText("")
        self.alipay.setPixmap(QtGui.QPixmap(":/images/ali"))
        self.alipay.setObjectName("alipay")
        self.Layout_2pay.addWidget(self.alipay)
        self.weicat = QtWidgets.QLabel(self.tab4)
        self.weicat.setText("")
        self.weicat.setPixmap(QtGui.QPixmap(":/images/wecat"))
        self.weicat.setObjectName("weicat")
        self.Layout_2pay.addWidget(self.weicat)
        self.Layout_pay.addLayout(self.Layout_2pay)
        self.Layout_pay.setStretch(0, 1)
        self.Layout_pay.setStretch(1, 5)
        self.verticalLayout_4.addLayout(self.Layout_pay)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/b3"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab4, icon5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MWin.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MWin)
        self.statusBar.setObjectName("statusBar")
        MWin.setStatusBar(self.statusBar)

        self.retranslateUi(MWin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MWin)

        self.lineEdit_input.setFocus()
        self.downloadWidget.setColumnWidth(1, 60)
        self.downloadWidget.setColumnWidth(2, 80)
        self.downloadWidget.setColumnWidth(3, 150)

    def retranslateUi(self, MWin):
        _translate = QtCore.QCoreApplication.translate
        MWin.setWindowTitle(_translate("MWin", "哔哩哔哩工具箱 v1.1 - ©Tich"))
        self.lineEdit_input.setPlaceholderText(_translate("MWin", "在此输入av号或视频链接"))
        self.search.setText(_translate("MWin", "搜索"))
        self.download.setText(_translate("MWin", "下载"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MWin", "av号"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MWin", "标题"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MWin", "发布时间"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MWin", "UP主"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MWin", "分类"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MWin", "封面"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MWin", "弹幕"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MWin", "稿件描述"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MWin", "首页"))
        self.startAll.setText(_translate("MWin", "全部开始"))
        self.pauseAll.setText(_translate("MWin", "全部暂停"))
        self.clearAll.setText(_translate("MWin", "清空全部"))
        self.videoFolder.setText(_translate("MWin", "存储目录：./video"))
        self.openVideoFolder.setText(_translate("MWin", "打开目录"))
        item = self.downloadWidget.horizontalHeaderItem(0)
        item.setText(_translate("MWin", "标题"))
        item = self.downloadWidget.horizontalHeaderItem(1)
        item.setText(_translate("MWin", "p数"))
        item = self.downloadWidget.horizontalHeaderItem(2)
        item.setText(_translate("MWin", "切片数"))
        item = self.downloadWidget.horizontalHeaderItem(3)
        item.setText(_translate("MWin", "进度"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MWin", "下载"))
        self.info.setPlainText(_translate("MWin", "GitHub：LewisTian\n"
"Email：lewissmith@126.com\n"
"详细介绍：https://github.com/LewisTian/PyQt5-Apps/tree/master/bilibili-kit\n"
"-----\n"
"哔哩哔哩工具箱 V1.1\n"
"\n"
"增加下载多切片/多p视频的功能，但未提供合并视频的功能（欢迎会的大佬给我私信或者在Github上pr）\n"
"不再提供封面和弹幕的下载，可以手动复制链接到浏览器自行下载\n"
"每个视频下载完成后表格对应行不会删除，可以最后手动清除所有行\n"
"=====\n"
"哔哩哔哩工具箱 V1.0\n"
"\n"
"主要功能是下载B站视频封面、弹幕和视频源文件\n"
"没有cookies下载的是标清的视频\n"
"若是想下载高清的视频，需要先保存cookie\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MWin", "关于"))
        self.label_pay.setText(_translate("MWin", "若是你觉得好用欢迎投喂ο(=•ω＜=)ρ⌒☆"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab4), _translate("MWin", "投喂"))

import res_rc
