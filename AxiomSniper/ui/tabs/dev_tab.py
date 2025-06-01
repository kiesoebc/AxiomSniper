from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, 
                            QTableWidget, QTableWidgetItem, 
                            QHeaderView, QPushButton)
from PyQt6.QtCore import QTimer
from core.api.pumpfun import PumpFunAPI  # Импорт нашего API

class DevSniperTab(QWidget):
    def __init__(self):
        super().__init__()
        self.api = PumpFunAPI()  # Инициализация API
        self.setup_ui()
        self.load_data()  # Первоначальная загрузка
        
    def setup_ui(self):
        """Настраиваем интерфейс"""
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Кнопка обновления
        self.btn_refresh = QPushButton("Обновить данные")
        self.btn_refresh.clicked.connect(self.load_data)
        layout.addWidget(self.btn_refresh)
        
        # Таблица
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        headers = ["Монета", "Цена", "Dev Кошелек", "Миграция", "Объем"]
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)
        
        # Автообновление каждые 60 сек
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_data)
        self.timer.start(60000)
    
    def load_data(self):
        """Загрузка реальных данных"""
        coins = self.api.get_new_coins()
        self.table.setRowCount(len(coins))
        
        for row, coin in enumerate(coins):
            self.table.setItem(row, 0, QTableWidgetItem(coin.get('symbol', 'N/A')))
            self.table.setItem(row, 1, QTableWidgetItem(str(coin.get('price', 0))))
            self.table.setItem(row, 2, QTableWidgetItem(coin.get('dev_wallet', '')))
            self.table.setItem(row, 3, QTableWidgetItem(f"{coin.get('migration_rate', 0)}%"))
            self.table.setItem(row, 4, QTableWidgetItem(str(coin.get('volume', 0))))
