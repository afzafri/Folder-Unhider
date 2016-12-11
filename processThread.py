# QThread Class file
# We will use this class to run the process in separate Thread
# So that the main GUI will not freeze/hang while the process is running

from PySide import QtCore, QtGui
import subprocess # library for running os console command

class ProcessThread(QtCore.QThread):

    def __init__(self,drive):
        QtCore.QThread.__init__(self)
        self.drive = drive # assigned received "drive" variables

    def __del__(self):
        self.wait()

    def run(self):
        # run windows command to change the folder and files attributes (to show hidden files/folder)
        # we now use subprocess.call instead of os.popen, since it is more efficient for background process
        subprocess.call("attrib -h -r -s /s /d "+self.drive+"*.* ", shell=True) # shell=True is to hide the output console window