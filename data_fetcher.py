import random
from datetime import datetime

def get_my_region():
    # Pro testování teď budeme vracet natvrdo Jihomoravský kraj
    # Později to zase zapneme na tu IP adresu
    return "Jihomoravský kraj"

def fetch_actual_diesel_price(region):
    # Simulujeme výkyvy cen kolem 36 Kč
    fake_price = round(random.uniform(35.5, 38.5), 2)
    
    return {
        "datum": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "kraj": region,
        "cena": fake_price
    }