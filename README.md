# Diesel Price Tracker (Czechia) 🇨🇿

Tento projekt automaticky sleduje a vizualizuje vývoj průměrné ceny motorové nafty v České republice na týdenní bázi. Data jsou čerpána přímo z otevřených datových sad Českého statistického úřadu (ČSÚ).

## 🚀 Jak to funguje
1. **Sběr dat:** Skript se připojuje k API ČSÚ a stahuje nejnovější týdenní statistiku průměrných cen pohonných hmot.
2. **Historie:** Data jsou ukládána do souboru `ceny_nafty_cr.csv`. Skript inteligentně kontroluje duplicity – pokud už data pro daný týden v souboru jsou, znovu je nezapisuje.
3. **Vizualizace:** Pomocí knihoven `Seaborn` a `Matplotlib` generuje lineární graf vývoje ceny v čase.
4. **Automatizace:** Díky GitHub Actions se aktualizace dat spouští automaticky každé pondělí dopoledne.

## 📊 Ukázka grafu
Graf zobrazuje vývoj ceny v Kč za litr. Díky historickému importu (backfill) projekt obsahuje data i několik měsíců zpětně.

## 🛠️ Použité technologie
* **Python 3.10+**
* **Pandas** (zpracování dat a CSV)
* **Requests** (stahování dat z API)
* **Seaborn & Matplotlib** (vizualizace)
* **GitHub Actions** (automatizace sběru)

## 📦 Instalace a spuštění
1. Klonování repozitáře:
   `git clone https://github.com/milicek/Fuel_price.git`
2. Instalace závislostí:
   `pip install -r requirements.txt`
3. Spuštění aplikace:
   `python main.py`

---
*Data jsou poskytována Českým statistickým úřadem podle dáné sady CENPHMT.*