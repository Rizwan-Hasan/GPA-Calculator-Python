import os
import sys
import pandas
import resources

# My Imports
from cgpa_calculator import CGPA_Calculator

# PyQt5 Imports
import PyQt5
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont, QPixmap, QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QPushButton, QErrorMessage
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, QSize, pyqtSignal, QThread


# Application root location ↓
appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        # Loading Main UI Design Files ↓
        uic.loadUi(appFolder + 'interface.ui', self)

        # Icon Variables
        self.icon = QIcon(':/icon/icon.png')

        with open(appFolder + 'stylesheet.qss', 'r') as styleSheetFile:
            self.setStyleSheet(styleSheetFile.read())

        self.mainWindow()

    def mainWindow(self):
        self.setWindowTitle("CGPA Calculator")
        self.setWindowIcon(self.icon)

        #
        self.labelCGPA.setFont(QFont('Comic Sans MS', 72))
        self.labelCGPA.setStyleSheet('color: #353535')
        self.labelCGPA.setText('0.00')

        #
        self.statusBar().showMessage("Fill all 3 boxes")

        #
        self.pushButtonCalculate.clicked.connect(self.calculateButton)
        self.pushButtonClear.clicked.connect(self.clearButton)

    @pyqtSlot()  # PyQt5 Decorator
    def calculateButton(self):
        try:
            self.pushButtonCalculate.disconnect()
        except (TypeError, AttributeError):
            pass
        cgpa = self.cgpaCalc()
        self.labelCGPA.setFont(QFont("Comic Sans MS", 72))
        self.labelCGPA.setText(cgpa)
        self.pushButtonCalculate.clicked.connect(self.calculateButton)

    def clearButton(self):
        try:
            self.pushButtonClear.disconnect()
        except (TypeError, AttributeError):
            pass

        self.lineEditTheory.clear()
        self.lineEditLab.clear()
        self.lineEditTotalCredit.clear()
        self.labelCGPA.setFont(QFont("Comic Sans MS", 72))
        self.labelCGPA.setText('0.00')
        self.pushButtonClear.clicked.connect(self.clearButton)

    def cgpaCalc(self):
        try:
            subGrades = self.lineEditTheory.text()
            labGrades = self.lineEditLab.text()
            totalCredit = self.lineEditTotalCredit.text()
            cgpa = CGPA_Calculator(subGrades, labGrades, totalCredit)
            cgpa = cgpa.getCGPA()
            if float(cgpa) <= 4.00:
                return str(cgpa)
            else:
                self.errorMessage('Error', 'Error!', 'Wrong information')
                return '0.00'
        except (UnboundLocalError, ValueError):
            self.errorMessage('Error', 'Error!', 'Wrong information')
            return '0.00'

    def errorMessage(self, title, text, infoText):
        msg = QMessageBox()
        msg.setWindowIcon(self.icon)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setInformativeText(infoText)
        msg.exec_()


# Main Function ↓
def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


# Start Application ↓
if __name__ == '__main__':
    main()
