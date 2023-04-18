# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.figdir_path = QtWidgets.QLineEdit(self.centralwidget)
        self.figdir_path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.figdir_path.setObjectName("figdir_path")
        self.gridLayout.addWidget(self.figdir_path, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fig2pdf = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("得意黑")
        font.setPointSize(24)
        font.setItalic(True)
        self.fig2pdf.setFont(font)
        self.fig2pdf.setObjectName("fig2pdf")
        self.horizontalLayout.addWidget(self.fig2pdf)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.path_browsing = QtWidgets.QPushButton(self.centralwidget)
        self.path_browsing.setObjectName("path_browsing")
        self.gridLayout.addWidget(self.path_browsing, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_PDF = QtWidgets.QMenu(self.menubar)
        self.menu_PDF.setObjectName("menu_PDF")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_PDF.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fig2pdf.setText(_translate("MainWindow", "图像转PDF"))
        self.path_browsing.setText(_translate("MainWindow", "..."))
        self.menu_PDF.setTitle(_translate("MainWindow", "转PDF"))
