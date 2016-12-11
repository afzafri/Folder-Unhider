# QThread Class file
# We will use this class to run the process in separate Thread
# So that the main GUI will not freeze/hang while the process is running

from PySide import QtCore, QtGui
import subprocess # library for running os console command

class ProcessThread(QtCore.QThread):

    def __init__(self,drive,radiostat):
        QtCore.QThread.__init__(self)
        self.drive = drive # assigned received "drive" variables
        self.radiostat = radiostat # assigned received var

    def __del__(self):
        self.wait()

    def run(self):

    	# window os commands
    	unhide = "attrib -h -r -s /s /d "+self.drive+"*.*"  # command to change the folder and files attributes (to show hidden files/folder)
    	delAutorun = "DEL /F /S /Q /A "+self.drive+"*.lnk" # command to delete all shortcuts .lnk files
    	delShorcut = "DEL /F /S /Q /A "+self.drive+"autorun.inf" # command to delete autorun.inf file
    	delini = "DEL /F /S /Q /A "+self.drive+"*.ini" # command to delete all .ini files

    	# check if radio button is checked, run the command to delete suspicious files. If not, run unhide only
    	if self.radiostat == True:
    		# we now use subprocess.call instead of os.popen, since it is more efficient for background process
			# shell=True is to hide the output console window
			subprocess.call(unhide + " && " + delAutorun + " && " + delShorcut + " && " + delini + " && explorer "+self.drive, shell=True)
    	else:
    		subprocess.call(unhide + " && explorer "+self.drive, shell=True)
    	
	        