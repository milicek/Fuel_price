import pandas as pd
import os
# Importujeme tvou funkci z druhého souboru
from data_fetcher import get_my_region, fetch_actual_diesel_price
from plotter import show_diesel_chart

# 1. Zjistíme, kde jsme a kolik to stojí
region = get_my_region()
result = fetch_actual_diesel_price(region)

# 2. Pokud máme data, uložíme je
if result is not None:
    file_name = 'ceny_nafty.csv'
    df = pd.DataFrame([result])
    
    # Kontrola existence souboru přes os
    file_exists = os.path.isfile(file_name)
    df.to_csv(file_name, mode='a', header=not file_exists, index=False)
    
    print(f"Úspěšně uloženo: {region} -> {result['cena']} Kč")
else:
    print("Data se nepodařilo stáhnout.")
    
# Na konci skriptu vykresli graf
show_diesel_chart()