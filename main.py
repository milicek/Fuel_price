import pandas as pd
import os
from data_fetcher import fetch_actual_diesel_price
from plotter import show_diesel_chart

# 1. Stáhneme aktuální data z ČSÚ
result = fetch_actual_diesel_price()

if result is not None:
    file_name = 'ceny_nafty_cr.csv'
    
    # Zjistíme, jestli už soubor existuje a co v něm je
    if os.path.exists(file_name):
        df_existing = pd.read_csv(file_name)
        # Kontrola, jestli už máme tento týden (obdobi_csu) v souboru
        if str(result['obdobi_csu']) in df_existing['obdobi_csu'].astype(str).values:
            print(f"--- INFO: Data pro {result['obdobi_csu']} již v souboru jsou. Nepřepisuji. ---")
            do_write = False
        else:
            do_write = True
    else:
        do_write = True

    # 2. Uložíme pouze pokud jde o nový týden
    if do_write:
        df_new = pd.DataFrame([result])
        file_exists = os.path.isfile(file_name)
        df_new.to_csv(file_name, mode='a', header=not file_exists, index=False)
        print(f"Nová data pro {result['obdobi_csu']} uložena.")

    # 3. Zobrazíme graf (vždy)
    show_diesel_chart()
else:
    print("Nepodařilo se získat aktuální data.")