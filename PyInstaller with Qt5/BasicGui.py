# ---------------------------------------------------------------------------------
# Program: Basic program that will be compiled into an .exe with Py Installer
# Created by: Otto-G
# Created on: 2019-11-02
# License: Unlicense
# ---------------------------------------------------------------------------------

from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi('BasicGui.ui')
win.sho()
sys.exit(app.exec())