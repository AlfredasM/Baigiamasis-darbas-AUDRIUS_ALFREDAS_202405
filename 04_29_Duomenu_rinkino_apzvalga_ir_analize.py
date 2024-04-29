import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_excel('99Bikers_Raw_data.xlsx')
DataFrame_info = df.info()
print(DataFrame_info)

Kokia_yra_metu_apyvarta = df['list_price'].sum().round(2)
Visu_metu_apyvalta_MLN = Kokia_yra_metu_apyvarta / 1000000
print(f'Visu metu apyvarta EUR. {Kokia_yra_metu_apyvarta}')
print(f'Visu metu apyvarta MLN_EUR {Visu_metu_apyvalta_MLN:.2f} milijonai euru')

# #Kas menesi apyvarta
df['month'] = df['transaction_date'].dt.month
pardavimai_kas_menesi = df.groupby('month')['list_price'].sum()


plt.figure(figsize=(10, 6))
pardavimai_kas_menesi.plot(kind='bar', color="red")
plt.title('Pardavimų sumos pagal menesiu')
plt.xlabel('Menesiai')
plt.ylabel('Pardavimu suma pagal men MLN.EUR')
plt.legend()
plt.xticks(range(0, 12), ['Sausis','Vasaris','Kovas','Balandis','Geguze',
                            'Birzelis','Liepa','Rugpjutis','Rugsejis','Spalis','Lapkritis','Gruodis'])
plt.xticks(rotation=20)
plt.show()





#vidutine_kaina_pagal_dviraciu_tipa

vidutine_kaina_pagal_dviraciu_tipa = df.groupby('product_line')[['list_price', 'standard_cost']].mean()
print(vidutine_kaina_pagal_dviraciu_tipa)

fig, ax = plt.subplots(figsize=(14,8))
color = 'tab:purple'
ax.set_xlabel('Dviraciu tipai ')
ax.set_ylabel('Midle sale price EUR', color=color)
bars = ax.bar(vidutine_kaina_pagal_dviraciu_tipa.index, vidutine_kaina_pagal_dviraciu_tipa['list_price'], alpha = 0.6, label='Average price', color=color)
ax.tick_params(axis='y', labelcolor=color)

ax.set_xticks(range(len(vidutine_kaina_pagal_dviraciu_tipa.index)))
ax.set_xticklabels(vidutine_kaina_pagal_dviraciu_tipa.index, rotation=20, ha='right')

ax1 = ax.twinx() #kai norime vaizduoti du matavimo vienetus vienoje grafoje
color = 'tab:cyan'
ax1.set_ylabel('Prime cost EUR', color=color)
bars2 = ax1.bar(range(len(vidutine_kaina_pagal_dviraciu_tipa.index)), vidutine_kaina_pagal_dviraciu_tipa['standard_cost'],
                color=color, alpha=0.4, width=0.4, label='Vidutine savikaina')
ax1.tick_params(axis='y', labelcolor=color)
#plt.savefig('average_metrics.png')
plt.title('Dviraciu tipu pasiskirstymas tarp savikainos ir pardavimo kainos')
plt.show()


#vidutine_kaina_pagal_dviraciu_kalse

vidutine_kaina_pagal_dviraciu_klase = df.groupby('product_class')[['list_price', 'standard_cost']].mean()
print(vidutine_kaina_pagal_dviraciu_klase)

fig, ax = plt.subplots(figsize=(14,8))
color = 'tab:orange'
ax.set_xlabel('Dviraciu klases ')
ax.set_ylabel('Midle sale price EUR', color=color)
bars = ax.bar(vidutine_kaina_pagal_dviraciu_klase.index, vidutine_kaina_pagal_dviraciu_klase['list_price'], alpha = 0.6, label='Average price', color=color)
ax.tick_params(axis='y', labelcolor=color)

ax.set_xticks(range(len(vidutine_kaina_pagal_dviraciu_klase.index)))
ax.set_xticklabels(vidutine_kaina_pagal_dviraciu_klase.index, rotation=20, ha='right')

ax1 = ax.twinx() #kai norime vaizduoti du matavimo vienetus vienoje grafoje
color = 'tab:green'
ax1.set_ylabel('Prime cost EUR', color=color)
bars2 = ax1.bar(range(len(vidutine_kaina_pagal_dviraciu_klase.index)), vidutine_kaina_pagal_dviraciu_klase['standard_cost'],
                color=color, alpha=0.4, width=0.4, label='Vidutine savikaina')
ax1.tick_params(axis='y', labelcolor=color)
#plt.savefig('average_metrics.png')
plt.title('Dviraciu klasiu pasiskirstymas tarp savikainos ir pardavimo kainos')
plt.show()



