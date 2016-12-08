# Show My Files
- Unhide folders and files in the drives easily
- Developed in Python 2.7 and PySide Qt Binding (GUI)

# Purpose
- Some of you maybe know about the "Shortcut Virus", which what the virus does is, it will hide all of your files and folders in the infected drive. Fortunately, this problem can be solve by tinkering in the windows folder and options setting, or run the ```attrib -h -r -s /s /d D:\*.*``` command in the CMD.
However, these steps may be a little bit complex for normal computer users or newbies. <br>
So, the purpose of this little programs is to make it easy for computer users to unhide all the hidden files and folder within a single click away.

# Usage
1. Method 1 - Windows Executeable
  - Run the ```showme.exe``` windows executeable
  - Select your drive letters which you wish to unhide
  - Click Unhide button
  - note: This method does not require Python and PySide QT Binding installed.
  
2. Method 2 - Python Script
  - cd into the project directory
  - ```python showme.py```
  - note: This method require Python 2.7 and PySide QT Binding installed
  
# Requirement (For developement)
- Python 2.7: https://wiki.qt.io/PySide
- PySide QT Binding: https://www.python.org/download/releases/2.7/

# License
This library is under MIT license, please look at the `LICENSE` file
