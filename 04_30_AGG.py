import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import plotly.figure_factory as ff

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

# Sujungiame excelio tris datasheet
data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')

data['month'] = data['transaction_date'].dt.month

vidutiniai_pardavimai_kas_menesi = data.groupby('month')['list_price'].mean().reset_index()
print(vidutiniai_pardavimai_kas_menesi)

menesio_pardavimai = data[['month', 'list_price']].reset_index()
print(menesio_pardavimai)



scaler = StandardScaler()
menesio_pardavimai_scaled = scaler.fit_transform(menesio_pardavimai)

#linked_nuoma_sezonui_scaled = linkage(nuoma_sezonui.values.reshape(-1, 1), method='ward')

agg_clust = AgglomerativeClustering(n_clusters=9, linkage='ward')
agg_clust.fit(menesio_pardavimai_scaled)

silh_score = silhouette_score(menesio_pardavimai_scaled, agg_clust.labels_)
print(silh_score)


plt.scatter(menesio_pardavimai_scaled[:, 1], menesio_pardavimai_scaled[:, 2], c=agg_clust.labels_, edgecolor='k', s=50, cmap='viridis')
plt.title("Pirkimai pagal AgglomerativeClustering n_cl-9")
plt.xlabel("Menesis")
plt.ylabel("Pirkimu aktyvumas")
plt.colorbar(label='')
plt.show()