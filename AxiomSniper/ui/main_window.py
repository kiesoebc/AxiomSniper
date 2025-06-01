from PyQt6.QtWidgets import QMainWindow, QTabWidget
from ui.tabs.dev_tab import DevSniperTab
from ui.tabs.twitter_tab import TwitterTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Axiom Sniper Pro")
        self.setGeometry(100, 100, 1000, 700)
        
        # Вкладки
        self.tabs = QTabWidget()
        self.tabs.addTab(DevSniperTab(), "Dev Sniper")
        self.tabs.addTab(TwitterTab(), "Twitter Checker")
        
        self.setCentralWidget(self.tabs)
