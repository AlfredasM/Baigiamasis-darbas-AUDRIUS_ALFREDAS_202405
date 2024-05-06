import pandas as pd
from matplotlib import pyplot as plt

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

# Sujungiame excelio tris datasheet
data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')
print(data.info())

#sutvarkome duomenis
data['gender'] = data['gender'].replace({'M': 'Male', 'Femal': 'Female', 'U': 'Unknown', 'F': 'Female'})

data['state'] = data['state'].replace({'NSW': 'New South Wales', 'VIC': 'Victoria', 'QLD': 'Queensland'})

#suskaiciuojame kiek yra skirtingu reiksmiu
kiek_pirko_pagal_lyti = data['gender'].value_counts()
print(kiek_pirko_pagal_lyti)

pardavimai_pagal_apskritis = data['state'].value_counts()
#print(pardavimai_pagal_apskritis)

#nusibraizome grafikus
fig, axs = plt.subplots(1, 2, figsize=(14, 7))
colors = ['orange', 'green', 'purple']

axs[0].bar(kiek_pirko_pagal_lyti.index, kiek_pirko_pagal_lyti.values, color=colors)
axs[0].set_xlabel('Female/Male/Unknown')
axs[0].set_ylabel('Quantity')
axs[0].set_title('Customers by gender')

axs[1].pie(pardavimai_pagal_apskritis, labels=pardavimai_pagal_apskritis.index, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Customers by living place/state')
plt.show()
