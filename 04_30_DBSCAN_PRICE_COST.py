import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.neighbors import NearestNeighbors
from kmodes.kmodes import KModes

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

# Sujungiame excelio tris datasheet
data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')
#print(data)

# sugrupavimas pagal 'standard_cost' ir 'list_price'
data['list_price'] = data['list_price'].fillna(data['list_price'].mean())
data['standard_cost'] = data['standard_cost'].fillna(data['standard_cost'].mean())


BIKE_SALES = data[['list_price', 'standard_cost']]

cost =[]

K = range(1, 20)
for num_clusters in list(K):
    kmode = KModes(n_clusters=num_clusters, init="random", n_init=5, verbose=1)
    kmode.fit_predict(BIKE_SALES)
    cost.append(kmode.cost_)

plt.plot(K, cost, 'bx-')
plt.xlabel('No. of clusters')
plt.ylabel('Cost')
plt.title('Elbow Method For Optimal k')
plt.show()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(BIKE_SALES)
dbscan = DBSCAN(eps=0.25, min_samples=2)
clusters = dbscan.fit_predict(X_scaled)
data['cluster'] = clusters

plt.figure(figsize=(10, 6))
plt.scatter(data['list_price'], data['standard_cost'], c=data['cluster'], cmap='viridis')
plt.scatter(data['list_price'][clusters == -1], data['standard_cost'][clusters == -1], c='red', marker='x', label='Noise')
plt.title("Dviraciu pardavimu sugrupavimas pagal /'list_price'/ ir /'standard_cost'/  DBSCAN")
plt.xlim(100)
plt.ylim(100)
plt.xlabel("Pagal 'list_price'")
plt.ylabel("Pagal 'standard_cost'")
plt.colorbar(label='cluster')
plt.show()
