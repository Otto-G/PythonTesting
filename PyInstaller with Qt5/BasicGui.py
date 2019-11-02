# ---------------------------------------------------------------------------------
# Program: Basic program that will be compiled into an .exe with Py Installer
# Created by: Otto-G
# Created on: 2019-11-02
# License: Unlicense
# ---------------------------------------------------------------------------------

from PyQt5 import QtWidgets, uic
import sys
import os


# Translate asset paths to usable format for PyInstaller


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # noinspection PyProtectedMember
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath('.'), relative_path)


app = QtWidgets.QApplication([])
win = uic.loadUi('BasicGui.ui')
win.show()
sys.exit(app.exec())
