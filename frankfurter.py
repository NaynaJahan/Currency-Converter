from api import get_url
import json
from datetime import date

BASE_URL = "https://api.frankfurter.app"

def get_currencies_list():
    
    url = f"{BASE_URL}/currencies"
    status_code, content = get_url(url)
    if status_code == 200:
        currencies = json.loads(content)
        return list(currencies.keys())
    else:
        return None
    

    

def get_latest_rates(from_currency, to_currency, amount):
    
    url = f"{BASE_URL}/latest?from={from_currency}&to={to_currency}"
    
    status_code, content = get_url(url)
    
    if status_code == 200:
        data = json.loads(content)
        today = str(date.today())
        return today, data["rates"][to_currency]
    else:
        return None, None
    
    

def get_historical_rate(from_currency, to_currency, from_date, amount):
    
    url = f"{BASE_URL}/{from_date}?from={from_currency}&to={to_currency}"
    
    status_code, content = get_url(url)
    
    if status_code == 200:
        data = json.loads(content)
        return data["rates"][to_currency]
    else:
        return None


