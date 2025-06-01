from core.api.pumpfun_api import PumpFunAPI

class DevSniper:
    def __init__(self):
        self.api = PumpFunAPI()
        self.min_migration = 30  # Минимальный % миграций
        
    def check_new_coins(self):
        coins = self.api.get_new_coins()
        for coin in coins:
            dev_history = self.api.get_dev_history(coin["dev_wallet"])
            if dev_history["migration_rate"] >= self.min_migration:
                print(f"Найдена хорошая монета: {coin['symbol']}")
