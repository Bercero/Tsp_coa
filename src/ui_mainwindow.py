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
        MainWindow.resize(910, 659)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.ejecucionTab = QtWidgets.QWidget()
        self.ejecucionTab.setObjectName("ejecucionTab")
        self.informacionWidget.addTab(self.ejecucionTab, "")
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
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 561, 411))
        self.graphicsView.setObjectName("graphicsView")
        self.itSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.itSpinBox.setGeometry(QtCore.QRect(710, 140, 61, 31))
        self.itSpinBox.setMinimum(1)
        self.itSpinBox.setMaximum(1000)
        self.itSpinBox.setProperty("value", 50)
        self.itSpinBox.setObjectName("itSpinBox")
        self.itLabel = QtWidgets.QLabel(self.centralwidget)
        self.itLabel.setGeometry(QtCore.QRect(580, 140, 111, 31))
        self.itLabel.setObjectName("itLabel")
        self.itSCLabel = QtWidgets.QLabel(self.centralwidget)
        self.itSCLabel.setGeometry(QtCore.QRect(590, 180, 201, 31))
        self.itSCLabel.setObjectName("itSCLabel")
        self.itSCBox = QtWidgets.QSpinBox(self.centralwidget)
        self.itSCBox.setGeometry(QtCore.QRect(800, 180, 61, 31))
        self.itSCBox.setMinimum(1)
        self.itSCBox.setMaximum(1000)
        self.itSCBox.setProperty("value", 20)
        self.itSCBox.setObjectName("itSCBox")
        self.nhSCBox = QtWidgets.QSpinBox(self.centralwidget)
        self.nhSCBox.setGeometry(QtCore.QRect(700, 220, 61, 31))
        self.nhSCBox.setMinimum(1)
        self.nhSCBox.setMaximum(50)
        self.nhSCBox.setProperty("value", 10)
        self.nhSCBox.setObjectName("nhSCBox")
        self.nhLabel = QtWidgets.QLabel(self.centralwidget)
        self.nhLabel.setGeometry(QtCore.QRect(580, 220, 111, 31))
        self.nhLabel.setObjectName("nhLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 910, 25))
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
        self.informacionWidget.setTabText(self.informacionWidget.indexOf(self.ejecucionTab), _translate("MainWindow", "ejecución"))
        self.mapaLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Mapa</p></body></html>"))
        self.cargarMapaButton.setText(_translate("MainWindow", "Cargar mapa"))
        self.itLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Max iterciones</p></body></html>"))
        self.itSCLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Max iteraciones sin cambios</p></body></html>"))
        self.nhLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Hormigas</p></body></html>"))

