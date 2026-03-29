import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_diesel_chart():
    try:
        df = pd.read_csv('ceny_nafty_cr.csv')
        df['datum'] = df['datum'].astype(str)
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x='obdobi_csu', y='cena', marker='o', sort=False)
        plt.title('Vývoj ceny nafty v čase')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        
        plt.show()
    except Exception as e:
        print(f"Graf nebylo možné vykreslit (asi málo dat): {e}")