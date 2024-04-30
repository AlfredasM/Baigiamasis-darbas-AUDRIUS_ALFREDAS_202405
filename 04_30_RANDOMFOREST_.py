import pandas as pd
from sklearn.metrics import recall_score, precision_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import seaborn as sns
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo
import numpy as np

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

# Sujungiame excelio tris datasheet
data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')
#print(data)

#numerical
data['DOB_YEAR'] = pd.DatetimeIndex(data['DOB']).year
data['DOB_YEAR'] = data['DOB_YEAR'].fillna(data['DOB_YEAR'].mean())

#categorical+
data['gender'] = data['gender'].replace({'M': 'Male', 'Femal': 'Female', 'U': 'Unknown', 'F': 'Female'})
data['state'] = data['state'].replace({'NSW': 'New South Wales', 'VIC': 'Victoria', 'QLD': 'Queensland'})

size = data['product_size'].value_counts()

print(size)

label_encoder = LabelEncoder()
one_encoder = OneHotEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['state'] = label_encoder.fit_transform(data['state'])
data['product_size'] = label_encoder.fit_transform(data['product_size'])
data['owns_car'] = label_encoder.fit_transform(data['owns_car'])
data['brand'] = label_encoder.fit_transform(data['brand'])
data['product_line'] = label_encoder.fit_transform(data['product_line'])
data['product_class'] = label_encoder.fit_transform(data['product_class'])
data['wealth_segment'] = label_encoder.fit_transform(data['wealth_segment'])

X = data[['DOB_YEAR', 'gender', 'state', 'product_size', 'owns_car', 'brand', 'product_line', 'product_class',
          'wealth_segment']]

y = data[['list_price']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestRegressor(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(16, 6))
plt.title('Parametru itaka kainai')
plt.xlabel('Svarbumas')
plt.ylabel('Parametras')
sns.barplot(x=importances[indices], y=X_train.columns[indices])
plt.show()
