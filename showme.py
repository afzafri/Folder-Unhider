# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Afif\Desktop\Python\Folder Unhide\unhider.ui'
#
# Created: Thu Dec 08 19:45:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import win32api # library for getting drive letters
import os 

class Ui_FolderUnhide(object):
    def setupUi(self, FolderUnhide):
        FolderUnhide.setObjectName("FolderUnhide")
        FolderUnhide.resize(211, 103)
        FolderUnhide.setMinimumSize(QtCore.QSize(211, 103))
        FolderUnhide.setMaximumSize(QtCore.QSize(211, 103))
        self.formLayoutWidget = QtGui.QWidget(FolderUnhide)
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
        self.unhideButton = QtGui.QPushButton(FolderUnhide)
        self.unhideButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.unhideButton.setObjectName("unhideButton")
        self.label = QtGui.QLabel(FolderUnhide)
        self.label.setGeometry(QtCore.QRect(60, 80, 91, 21))
        self.label.setObjectName("label")

        self.retranslateUi(FolderUnhide)
        QtCore.QMetaObject.connectSlotsByName(FolderUnhide)

         # get string of drives letters
        drives = win32api.GetLogicalDriveStrings() 
        # split the string into array
        drives = drives.split('\000')[:-1] 
        # populate combo box with drives letters
        self.selectDrives.addItems(drives)

        # check if button unhide is clicked, call function
        self.unhideButton.clicked.connect(self.processFunc)

    # process function
    def processFunc(self):

        # disabled input for safety precaution
        self.selectDrives.setDisabled(True)
        self.unhideButton.setDisabled(True)

        # change cursor to loading 
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)

        # get choosen drive letter
        drive = self.selectDrives.currentText()

        # run windows command to change the folder and files attributes (to show hidden files/folder)
        os.system("attrib -h -r -s /s /d "+drive+"*.* ")

        # restore the cursor
        QtGui.QApplication.restoreOverrideCursor()

        self.alertBox("Success") # alert success message

        # enable back the input
        self.selectDrives.setDisabled(False)
        self.unhideButton.setDisabled(False)

    # create message box function
    def alertBox(self,msg):
        msgBox = QtGui.QMessageBox() 
        msgBox.setWindowTitle("Alert");
        msgBox.setText(msg);
        msgBox.exec_();

    def retranslateUi(self, FolderUnhide):
        FolderUnhide.setWindowTitle(QtGui.QApplication.translate("FolderUnhide", "Show My Files", None, QtGui.QApplication.UnicodeUTF8))
        FolderUnhide.setWindowIcon(QtGui.QIcon("./res/icon.ico"))
        self.label_2.setText(QtGui.QApplication.translate("FolderUnhide", "Select Drive Letter: ", None, QtGui.QApplication.UnicodeUTF8))
        self.unhideButton.setText(QtGui.QApplication.translate("FolderUnhide", "Unhide!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FolderUnhide", "Afif Zafri © 2016", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FolderUnhide = QtGui.QDialog()
    ui = Ui_FolderUnhide()
    ui.setupUi(FolderUnhide)
    FolderUnhide.show()
    sys.exit(app.exec_())

