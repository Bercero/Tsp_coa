# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_src/tsp_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.newMapaButton = QtWidgets.QPushButton(self.centralwidget)
        self.newMapaButton.setGeometry(QtCore.QRect(690, 20, 85, 30))
        self.newMapaButton.setObjectName("newMapaButton")
        self.selectorAlgoritmo = QtWidgets.QSplitter(self.centralwidget)
        self.selectorAlgoritmo.setGeometry(QtCore.QRect(580, 60, 81, 42))
        self.selectorAlgoritmo.setOrientation(QtCore.Qt.Vertical)
        self.selectorAlgoritmo.setObjectName("selectorAlgoritmo")
        self.labelAlgoritmo = QtWidgets.QLabel(self.selectorAlgoritmo)
        self.labelAlgoritmo.setObjectName("labelAlgoritmo")
        self.comboBoxAlgoritmo = QtWidgets.QComboBox(self.selectorAlgoritmo)
        self.comboBoxAlgoritmo.setObjectName("comboBoxAlgoritmo")
        self.ejecutarButton = QtWidgets.QPushButton(self.centralwidget)
        self.ejecutarButton.setGeometry(QtCore.QRect(630, 360, 85, 30))
        self.ejecutarButton.setObjectName("ejecutarButton")
        self.informacionWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.informacionWidget.setGeometry(QtCore.QRect(10, 430, 761, 161))
        self.informacionWidget.setObjectName("informacionWidget")
        self.infoTab = QtWidgets.QWidget()
        self.infoTab.setObjectName("infoTab")
        self.informacionWidget.addTab(self.infoTab, "")
        self.ejecutionTab = QtWidgets.QWidget()
        self.ejecutionTab.setObjectName("ejecutionTab")
        self.informacionWidget.addTab(self.ejecutionTab, "")
        self.selectorMapa = QtWidgets.QSplitter(self.centralwidget)
        self.selectorMapa.setGeometry(QtCore.QRect(580, 10, 81, 42))
        self.selectorMapa.setOrientation(QtCore.Qt.Vertical)
        self.selectorMapa.setObjectName("selectorMapa")
        self.labelMapa = QtWidgets.QLabel(self.selectorMapa)
        self.labelMapa.setObjectName("labelMapa")
        self.comboBoxMapa = QtWidgets.QComboBox(self.selectorMapa)
        self.comboBoxMapa.setObjectName("comboBoxMapa")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.informacionWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TSP ACO"))
        self.newMapaButton.setText(_translate("MainWindow", "Nuevo mapa"))
        self.labelAlgoritmo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Algoritmo</p></body></html>"))
        self.ejecutarButton.setText(_translate("MainWindow", "ejecutar"))
        self.informacionWidget.setTabText(self.informacionWidget.indexOf(self.infoTab), _translate("MainWindow", "información"))
        self.informacionWidget.setTabText(self.informacionWidget.indexOf(self.ejecutionTab), _translate("MainWindow", "ejecución"))
        self.labelMapa.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mapa</p></body></html>"))

