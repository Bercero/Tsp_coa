#! /usr/bin/env python3.5
from tsp import tsp_as as tsp
#TODO es necesario hacer el import aqui y en tsp?
from pickle import load
from mapas import Mapa

from ui_mainwindow import Ui_MainWindow

from os.path import splitext, basename

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtCore import pyqtSlot, Qt

import sys


class MainWindow(Ui_MainWindow):
    def setupUi(self, window):
        super(MainWindow, self).setupUi(window)
        self.mapasList=[]
        #todo conectar la señal ^C
        self.cargarMapaButton.clicked.connect(self.addMapa)
        self.mapaComboBox.currentIndexChanged.connect(self.cargarMapa)

    #TODO filters, comprobar extensiones
    @pyqtSlot(bool)
    def addMapa(self, a):
        directory = "./mapas"
        mapas=QFileDialog.getOpenFileNames(self.centralwidget,"cargarMapa",directory)[0]
        for m in mapas:
            self.mapasList.append(m)
            self.mapaComboBox.addItem(splitext(basename(m))[0])

    @pyqtSlot(int)
    def cargarMapa(self, index):
        with open(self.mapasList[index],'rb') as m:
            self.mapa=load(m)
            #TODO print info en infoTab

if __name__ == '__main__':
    app = QApplication([])
    w = QMainWindow()
    u = MainWindow()
    u.setupUi(w)

    w.show()
    sys.exit(app.exec_())
