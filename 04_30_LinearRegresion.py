import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

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



label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['state'] = label_encoder.fit_transform(data['state'])
data['product_size'] = label_encoder.fit_transform(data['product_size'])
data['owns_car'] = label_encoder.fit_transform(data['owns_car'])
data['brand'] = label_encoder.fit_transform(data['brand'])
data['product_line'] = label_encoder.fit_transform(data['product_line'])
data['product_class'] = label_encoder.fit_transform(data['product_class'])
data['wealth_segment'] = label_encoder.fit_transform(data['wealth_segment'])

X = np.array(data[['DOB_YEAR']]).reshape(-1, 1)
y = np.array(data[['past_3_years_bike_related_purchases']]).reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.scatter(X_train, y_train, color='blue', label='Mokymo duomenys')
plt.scatter(X_test, y_test, color='green', label='Testavimo duomenys')
plt.plot(X_test, y_pred, color='red', label='Prognoze')
plt.xlim(1950)
plt.ylim(40)
plt.xlabel('Pirkoeju amzius DOB')
plt.ylabel('Dviraciu daliu ir aksesuaru pirkimas  per paskutinius 3 metus')
plt.title('Pirkimo ir amziaus analize')
plt.legend()
plt.show()

# MSE R2 RMSE
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = sqrt(mean_squared_error(y_test, y_pred))

print('MSE: ', mse)
print('R2: ', r2)
print('RMSE: ', rmse)

