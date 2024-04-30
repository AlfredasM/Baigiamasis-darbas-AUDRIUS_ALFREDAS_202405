import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

# Sujungiame excelio tris datasheet
data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')
#print(data)


data['DOB_YEAR'] = pd.DatetimeIndex(data['DOB']).year
data['DOB_YEAR'] = data['DOB_YEAR'].fillna(data['DOB_YEAR'].mean())
print(data['DOB_YEAR'])

features = data[['DOB_YEAR', 'list_price']].values
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(features_scaled)

plt.scatter(data['DOB_YEAR'], data['list_price'], c=data['Cluster'], cmap='plasma')
#plt.scatter(data['DOB_YEAR'] >= 1900, data['list_price'], c='red', marker='x', label='Noise')
plt.title('Klasterizacija KMeans')
plt.xlim(1950)
plt.xlabel('Date of birth')
plt.ylabel('Kaina')
plt.colorbar(label='Clusteris')
plt.show()
