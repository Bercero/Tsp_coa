#! /usr/bin/env python3.5
from gui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    w=QtWidgets.QMainWindow()
    u=Ui_MainWindow()
    u.setupUi(w)
    w.show()
    sys.exit(app.exec_())
