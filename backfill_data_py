import requests
import pandas as pd
import io
import os

def backfill_history(weeks=20):
    url = "https://data.csu.gov.cz/opendata/sady/CENPHMT/distribuce/csv"
    file_name = 'ceny_nafty_cr.csv'
    
    print(f"--- Zahajuji historický import (posledních {weeks} týdnů) ---")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            csv_data = io.StringIO(response.text)
            df = pd.read_csv(csv_data, quotechar='"')
            
            # Filtrujeme naftu a průměrnou cenu
            ukazatel = "Průměrná cena pohonných hmot (Kč/litr)"
            mask = (df['Ukazatel'] == ukazatel) & (df['Druh PHM'] == 'Motorová nafta')
            history_df = df[mask].copy()
            
            # Vezmeme posledních X týdnů
            history_df = history_df.tail(weeks)
            
            # Připravíme data pro náš formát
            final_data = []
            for _, row in history_df.iterrows():
                cena = float(str(row['Hodnota']).replace(',', '.'))
                # Jelikož v historii nemáme přesné datum spuštění, 
                # použijeme pro graf označení období z ČSÚ
                final_data.append({
                    "datum": row['Týdny'], # Pro historii použijeme týden jako osu X
                    "obdobi_csu": row['Týdny'],
                    "cena": cena
                })
            
            new_df = pd.DataFrame(final_data)
            
            # Uložíme (přepíšeme starý soubor, abychom měli čistou historii)
            new_df.to_csv(file_name, index=False)
            print(f"Úspěšně naimportováno {len(new_df)} týdnů do {file_name}")
            
    except Exception as e:
        print(f"Chyba při importu: {e}")

if __name__ == "__main__":
    backfill_history()