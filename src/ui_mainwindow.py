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
        MainWindow.resize(802, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 551, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.newMapaButton = QtWidgets.QPushButton(self.centralwidget)
        self.newMapaButton.setGeometry(QtCore.QRect(680, 20, 101, 30))
        self.newMapaButton.setObjectName("newMapaButton")
        self.algoritmoSelector = QtWidgets.QSplitter(self.centralwidget)
        self.algoritmoSelector.setGeometry(QtCore.QRect(580, 60, 81, 42))
        self.algoritmoSelector.setOrientation(QtCore.Qt.Vertical)
        self.algoritmoSelector.setObjectName("algoritmoSelector")
        self.algoritmoLabel = QtWidgets.QLabel(self.algoritmoSelector)
        self.algoritmoLabel.setObjectName("algoritmoLabel")
        self.algoritmoComboBox = QtWidgets.QComboBox(self.algoritmoSelector)
        self.algoritmoComboBox.setObjectName("algoritmoComboBox")
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
        self.mapaSelector = QtWidgets.QSplitter(self.centralwidget)
        self.mapaSelector.setGeometry(QtCore.QRect(580, 10, 81, 42))
        self.mapaSelector.setOrientation(QtCore.Qt.Vertical)
        self.mapaSelector.setObjectName("mapaSelector")
        self.mapaLabel = QtWidgets.QLabel(self.mapaSelector)
        self.mapaLabel.setObjectName("mapaLabel")
        self.mapaComboBox = QtWidgets.QComboBox(self.mapaSelector)
        self.mapaComboBox.setObjectName("mapaComboBox")
        self.cargarMapaButton = QtWidgets.QPushButton(self.centralwidget)
        self.cargarMapaButton.setGeometry(QtCore.QRect(680, 60, 101, 30))
        self.cargarMapaButton.setObjectName("cargarMapaButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
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
        self.algoritmoLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Algoritmo</p></body></html>"))
        self.ejecutarButton.setText(_translate("MainWindow", "ejecutar"))
        self.informacionWidget.setTabText(self.informacionWidget.indexOf(self.infoTab), _translate("MainWindow", "información"))
        self.informacionWidget.setTabText(self.informacionWidget.indexOf(self.ejecutionTab), _translate("MainWindow", "ejecución"))
        self.mapaLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mapa</p></body></html>"))
        self.cargarMapaButton.setText(_translate("MainWindow", "Cargar mapa"))

