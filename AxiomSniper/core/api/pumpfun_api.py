import requests

class PumpFunAPI:
    BASE_URL = "https://api.dexscreener.com/latest/dex/search?q=pump.fun"
    
    def get_new_coins(self):
        response = requests.get(f"{self.BASE_URL}/coins")
        return response.json()
    
    def get_dev_history(self, dev_wallet: str):
        response = requests.get(f"{self.BASE_URL}/dev/{dev_wallet}/history")
        return response.json()
