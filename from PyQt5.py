from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon

import sys
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Menu Bar")
        self.setGeometry(350, 350, 600, 500)
 
        # Create menu bar
        mainMenu = self.menuBar()
        self.createMenus(mainMenu)
 
    # Create menus
    def createMenus(self, mainMenu):
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        searchMenu = mainMenu.addMenu("Search")
        toolsMenu = mainMenu.addMenu("Tools")
 
        # Create actions
        newAction = QAction("New", self)
        openAction = QAction("Open File", self)
        saveAction = QAction(QIcon("images/save.png"), "Save", self)
        saveAsAction = QAction("Save As", self)
        exitAction = QAction(QIcon("images/exit.jpg"), "Exit", self)
        viewHelpAction = QAction("View Help", self)
        findAction = QAction("Find", self)
        replaceAction = QAction("Replace", self)
        customAction = QAction("Customize Toolbar", self)
 
        # Add actions
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(exitAction)
        viewMenu.addAction(viewHelpAction)
        searchMenu.addAction(findAction)
        searchMenu.addAction(replaceAction)
        toolsMenu.addAction(customAction)
        
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())