import requests
import pandas as pd
import io
from datetime import datetime

def fetch_actual_diesel_price():
    url = "https://data.csu.gov.cz/opendata/sady/CENPHMT/distribuce/csv"
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            csv_data = io.StringIO(response.text)
            # Načteme CSV (použijeme quotechar, protože názvy jsou v uvozovkách)
            df = pd.read_csv(csv_data, quotechar='"')
            
            # FILTR NASTAVENÝ PŘESNĚ PODLE TVÉHO VÝPISU
            ukazatel_nazev = "Průměrná cena pohonných hmot (Kč/litr)"
            palivo_nazev = "Motorová nafta"
            
            mask = (df['Ukazatel'] == ukazatel_nazev) & (df['Druh PHM'] == palivo_nazev)
            diesel_data = df[mask]
            
            if not diesel_data.empty:
                posledni = diesel_data.iloc[-1]
                
                # Převod ceny (čárka -> tečka)
                cena_raw = str(posledni['Hodnota']).replace(',', '.')
                cena = float(cena_raw)
                obdobi = posledni['Týdny']
                
                print(f"Úspěch! Aktuální cena pro ČR: {cena} Kč (Týden: {obdobi})")
                
                return {
                    "datum": datetime.now().strftime("%Y-%m-%d"),
                    "obdobi_csu": obdobi,
                    "cena": cena
                }
            else:
                print("Chyba: V datech nebyla nalezena Motorová nafta s průměrnou cenou.")
                
    except Exception as e:
        print(f"Kritická chyba: {e}")
        
    return None