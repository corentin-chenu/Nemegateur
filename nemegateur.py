#UTC-503 Projet
#CHENU Corentin
# Projet de création d'un navigateur en python 

#Importation des bibliothèques nécéssaires
import sys
from PyQt5 import QtGui

#Pour la réalisation de ce navigateur, je vais m'aider de la bibliothèque PyQt5 qui permet le développement d'applications et d'interfaces utilisateurs.
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *

# Création de la fenêtre personalisée de mon navigateur
class Fenetre(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Nom de ma fenêtre
        self.setWindowTitle("Nemegateur")
        self.setStyleSheet("background-color: #F5F5DC;")

        title = QLabel('Title')
        grid = QGridLayout()
        grid.setSpacing(10)

        #Ajout du moteur de recherche 
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.browser.setGeometry(200,200,250,200)

        #Ajout d'une barre d'outils
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        #Bouton retour
        prev_Btn = QAction('<',self)
        prev_Btn.triggered.connect(self.browser.back)
        nav_bar.addAction(prev_Btn)

        #Bouton retour en avant
        forward_Btn = QAction('>',self)
        forward_Btn.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_Btn)

        #Bouton de refresh
        refresh_Btn = QAction('Refresh',self)
        refresh_Btn.triggered.connect(self.browser.reload)
        nav_bar.addAction(refresh_Btn)

        #Ajout d'une barre de recherche
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        self.browser.urlChanged.connect(self.updateUrl)
        nav_bar.addWidget(self.searchBar)

        #Arrangement et taille des blocs
        self.setCentralWidget(self.browser)
        self.showMaximized()

    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))

         
    def updateUrl(self, url):
        self.searchBar.setText(url.toString())

app = QApplication.instance()
if not app :
    app = QApplication(sys.argv)

fen = Fenetre()
fen.show()
app.exec_()
