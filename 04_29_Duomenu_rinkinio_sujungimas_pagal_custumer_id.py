import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')

# Sujungiame excleio du datasheet
data = pd.merge(df1, df2, on='customer_id')
DataFrame_info = data.info()
print(DataFrame_info)
# print(data)
# sutvarkome duomenis
data['gender'] = data['gender'].replace({'M': 'Male', 'Femal': 'Female', 'U': 'Unknown', 'F': 'Female'})
#suskaiciuojame kiek yra skirtingu reiksmiu
kiek_pirko_pagal_lyti = data['gender'].value_counts()
print(kiek_pirko_pagal_lyti)

#nusibraizome grafika
sns.barplot(x=kiek_pirko_pagal_lyti.index, y=kiek_pirko_pagal_lyti.values, palette='tab10')
plt.title('Koks yra pirkeju pasiskirstymas pagal lyti')
plt.xlabel('Vyras/Moteris/Nezinomas')
plt.ylabel('Kiekis')
plt.legend()
plt.show()
