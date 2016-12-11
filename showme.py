# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Afif\Desktop\Python\Folder Unhide\res\showme.ui'
#
# Created: Sun Dec 11 18:15:59 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import win32api # library for getting drive letters
import res_rc # import resource file
import processThread # import our QThread class, for running background process in new thread

class Ui_FolderUnhide(object):
    def setupUi(self, FolderUnhide):
        FolderUnhide.setObjectName("FolderUnhide")
        FolderUnhide.setEnabled(True)
        FolderUnhide.resize(262, 124)
        FolderUnhide.setMinimumSize(QtCore.QSize(262, 124))
        FolderUnhide.setMaximumSize(QtCore.QSize(262, 124))
        self.unhideButton = QtGui.QPushButton(FolderUnhide)
        self.unhideButton.setGeometry(QtCore.QRect(90, 70, 85, 23))
        self.unhideButton.setCursor(QtCore.Qt.PointingHandCursor)
        self.unhideButton.setObjectName("unhideButton")
        self.label = QtGui.QLabel(FolderUnhide)
        self.label.setGeometry(QtCore.QRect(140, 100, 110, 21))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtGui.QWidget(FolderUnhide)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.selectDrives = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectDrives.sizePolicy().hasHeightForWidth())
        self.selectDrives.setSizePolicy(sizePolicy)
        self.selectDrives.setCursor(QtCore.Qt.PointingHandCursor)
        self.selectDrives.setObjectName("selectDrives")
        self.horizontalLayout.addWidget(self.selectDrives)
        self.refreshList = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.refreshList.setCursor(QtCore.Qt.PointingHandCursor)
        self.refreshList.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshList.setIcon(icon)
        self.refreshList.setIconSize(QtCore.QSize(25, 25))
        self.refreshList.setObjectName("refreshList")
        self.horizontalLayout.addWidget(self.refreshList)
        self.progressBar = QtGui.QProgressBar(FolderUnhide)
        self.progressBar.setGeometry(QtCore.QRect(10, 100, 71, 20))
        self.progressBar.setTextVisible(False)
        self.progressBar.setRange(0,1)
        self.progressBar.setObjectName("progressBar")
        self.delFiles = QtGui.QRadioButton(FolderUnhide)
        self.delFiles.setGeometry(QtCore.QRect(50, 40, 191, 31))
        self.delFiles.setObjectName("delFiles")

        # include stylesheet 
        styles = """QWidget {
                   background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e6fcff, stop: 1 #66edff);
                }
                QLabel {
                    color: #212121;
                    font-size: 13px;
                    font-weight: bold;
                    background: rgba(0, 0, 0, 0); 
                }
                QPushButton {
                    color: white;
                    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #00BCD4, stop: 0.1 #4deaff, stop: 0.49 #008799, stop: 0.5 #007180, stop: 1 #00cbe6);
                    border-width: 1px;
                    border-color: #339;
                    border-style: solid;
                    border-radius: 7;
                    padding: 3px;
                    font-size: 15px;
                    padding-left: 5px;
                    padding-right: 5px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #00BCD4;

                }
                QPushButton:pressed {
                    background-color: #009688;
                }
                QPushButton:disabled {
                    background-color:#dddddd;
                    border-color: #dddddd;
                }
                QComboBox {
                    border: 1px solid #00BCD4;
                    color: #212121;
                }
                QComboBox:disabled {
                    background-color:#dddddd;
                    border: 1px solid #dddddd;
                }
                QRadioButton {
                    background: rgba(0, 0, 0, 0); 
                    font-size: 13px;
                    color: #212121;
                    font-weight: bold;
                }

            """
        # set stylesheet
        FolderUnhide.setStyleSheet(styles)

        self.retranslateUi(FolderUnhide)
        QtCore.QMetaObject.connectSlotsByName(FolderUnhide)

        # call function to populate select box
        self.drivesList()

        # check if refresh button is clicked, call fuction
        self.refreshList.clicked.connect(self.drivesList)

        # check if unhide button is clicked, call function
        self.unhideButton.clicked.connect(self.processFunc)

    # get list of drives to populate select drive box
    def drivesList(self):
        # get string of drives letters
        drives = win32api.GetLogicalDriveStrings() 
        # split the string into array
        # need to use substring to exclude last item because it's null
        drives = drives.split('\000')[:-1] 
        # remove existing item
        self.selectDrives.clear()
        # populate combo box with drives letters
        self.selectDrives.addItems(drives)

    # process function
    def processFunc(self):
        
        # get choosen drive letter
        drive = self.selectDrives.currentText()
        # get delete file option radio status
        radiostat = self.delFiles.isChecked()
        
        self.onStart() # call function for disable button, loading cursor

        self.newThread = processThread.ProcessThread(drive,radiostat) # create new QThread
        self.newThread.finished.connect(self.onDone) # connect to finished() signal. When QThread finish, call onDone() function
        self.newThread.start() # start the thread
        
    # function for disable button, when process start
    def onStart(self):
        # set progress bar to busy (pulse progress bar)
        self.progressBar.setRange(0,0)
        # change cursor to loading 
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        # disabled input for safety precaution
        self.selectDrives.setDisabled(True)
        self.unhideButton.setDisabled(True)
        self.refreshList.setDisabled(True)

    # functiont to restore all disabled button, once process ended
    def onDone(self):
        # restore the progress bar
        self.progressBar.setRange(0,1)
        # restore the cursor
        QtGui.QApplication.restoreOverrideCursor()
        # alert success message
        self.alertBox("Success") 
        # enable back the input
        self.selectDrives.setDisabled(False)
        self.unhideButton.setDisabled(False)
        self.refreshList.setDisabled(False)
        # uncheck the radio button
        self.delFiles.setChecked(False)

    # create message box function
    def alertBox(self,msg):
        msgBox = QtGui.QMessageBox() 
        msgBox.setWindowTitle("Alert")
        msgBox.setText(msg)
        msgBox.setStyleSheet("""
                            QWidget {
                               background: QLinearGradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #e6fcff, stop: 1 #66edff);
                            }
                            QLabel {
                                color: #212121;
                                font-size: 13px;
                                font-weight: bold;
                                background: rgba(0, 0, 0, 0); 
                            }
                            """)
        msgBox.exec_()

    def retranslateUi(self, FolderUnhide):
        FolderUnhide.setWindowTitle(QtGui.QApplication.translate("FolderUnhide", "Show My Files", None, QtGui.QApplication.UnicodeUTF8))
        FolderUnhide.setWindowIcon(QtGui.QIcon(":/res/icon.png"))
        self.unhideButton.setToolTip(QtGui.QApplication.translate("FolderUnhide", "Click to start", "Click to start", QtGui.QApplication.UnicodeUTF8))
        self.unhideButton.setText(QtGui.QApplication.translate("FolderUnhide", "Show Me!", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setToolTip(QtGui.QApplication.translate("FolderUnhide", "Contact: FB: fb.me/afzafri, Twitter & Instagram: @afzafri", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FolderUnhide", "Afif Zafri © 2016", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("FolderUnhide", "Select Drive Letter: ", None, QtGui.QApplication.UnicodeUTF8))
        self.selectDrives.setToolTip(QtGui.QApplication.translate("FolderUnhide", "Choose your drive letter", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshList.setToolTip(QtGui.QApplication.translate("FolderUnhide", "Refresh drives list", None, QtGui.QApplication.UnicodeUTF8))
        self.delFiles.setToolTip(QtGui.QApplication.translate("FolderUnhide", "Delete shortcuts (.lnk), autorun.inf, .ini files. These files are usually associate with the virus. WARNING!: This also might accidently delete some of your files, do it on your own risk.", None, QtGui.QApplication.UnicodeUTF8))
        self.delFiles.setText(QtGui.QApplication.translate("FolderUnhide", "Delete suspicious files", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FolderUnhide = QtGui.QDialog()
    ui = Ui_FolderUnhide()
    ui.setupUi(FolderUnhide)
    FolderUnhide.show()
    sys.exit(app.exec_())

