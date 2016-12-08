# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Afif\Desktop\Python\Folder Unhide\unhider.ui'
#
# Created: Thu Dec 08 19:45:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import win32api
import os

class Ui_FolderUnhider(object):
    def setupUi(self, FolderUnhider):
        FolderUnhider.setObjectName("FolderUnhider")
        FolderUnhider.resize(211, 103)
        FolderUnhider.setMinimumSize(QtCore.QSize(211, 103))
        FolderUnhider.setMaximumSize(QtCore.QSize(211, 103))
        self.formLayoutWidget = QtGui.QWidget(FolderUnhider)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 191, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.selectDrives = QtGui.QComboBox(self.formLayoutWidget)
        self.selectDrives.setObjectName("selectDrives")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.selectDrives)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.unhideButton = QtGui.QPushButton(FolderUnhider)
        self.unhideButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.unhideButton.setObjectName("unhideButton")
        self.label = QtGui.QLabel(FolderUnhider)
        self.label.setGeometry(QtCore.QRect(60, 80, 91, 21))
        self.label.setObjectName("label")

        self.retranslateUi(FolderUnhider)
        QtCore.QMetaObject.connectSlotsByName(FolderUnhider)

         # get string of drives letters
        drives = win32api.GetLogicalDriveStrings() 
        # split the string into array
        drives = drives.split('\000')[:-1] 
        # populate combo box with drives letters
        self.selectDrives.addItems(drives)

        # check if button unhide is clicked, call function
        self.unhideButton.clicked.connect(self.processFunc)

    def processFunc(self):
        # get choosen drive letter
        drive = self.selectDrives.currentText()
        os.system("attrib -h -r -s /s /d "+drive+"*.* ")

    def retranslateUi(self, FolderUnhider):
        FolderUnhider.setWindowTitle(QtGui.QApplication.translate("FolderUnhider", "Folder Unhider", None, QtGui.QApplication.UnicodeUTF8))
        FolderUnhider.setWindowIcon(QtGui.QIcon("./res/icon.ico"))
        self.label_2.setText(QtGui.QApplication.translate("FolderUnhider", "Select Drive Letter: ", None, QtGui.QApplication.UnicodeUTF8))
        self.unhideButton.setText(QtGui.QApplication.translate("FolderUnhider", "Unhide!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FolderUnhider", "Afif Zafri © 2016", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FolderUnhider = QtGui.QDialog()
    ui = Ui_FolderUnhider()
    ui.setupUi(FolderUnhider)
    FolderUnhider.show()
    sys.exit(app.exec_())

