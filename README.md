# Diesel Price Tracker (Czechia)
Tento projekt automaticky sbírá data o cenách nafty v ČR podle polohy uživatele.

## Jak to funguje
1. Zjistí polohu (kraj) podle IP adresy.
2. Stáhne (aktuálně simuluje) cenu nafty z MPO.
3. Uloží data do `ceny_nafty.csv`.
4. Vykreslí graf vývoje cen.