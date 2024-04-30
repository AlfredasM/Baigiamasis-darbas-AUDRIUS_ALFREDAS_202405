import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import KFold, cross_val_score
from sklearn import preprocessing
from sklearn import utils


df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

# Sujungiame excelio tris datasheet
data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')
#print(data)

#numerical
data['DOB_YEAR'] = pd.DatetimeIndex(data['DOB']).year
data['DOB_YEAR'] = data['DOB_YEAR'].fillna(data['DOB_YEAR'].mean())
data['online_order'] = data['online_order'].fillna(0)



#categorical+
data['gender'] = data['gender'].replace({'M': 'Male', 'Femal': 'Female', 'U': 'Unknown', 'F': 'Female'})
data['state'] = data['state'].replace({'NSW': 'New South Wales', 'VIC': 'Victoria', 'QLD': 'Queensland'})
data['gender'] = data['gender'].replace({'Female': 'False', 'Male': 'True', 'Unknown': 'True'})
size = data['online_order'].value_counts()

print(size)

label_encoder = LabelEncoder()

data['gender'] = label_encoder.fit_transform(data['gender'])
data['state'] = label_encoder.fit_transform(data['state'])
data['product_size'] = label_encoder.fit_transform(data['product_size'])
data['owns_car'] = label_encoder.fit_transform(data['owns_car'])
data['brand'] = label_encoder.fit_transform(data['brand'])
data['product_line'] = label_encoder.fit_transform(data['product_line'])
data['product_class'] = label_encoder.fit_transform(data['product_class'])
data['wealth_segment'] = label_encoder.fit_transform(data['wealth_segment'])


X = data[['wealth_segment', 'product_line', 'product_class', 'owns_car', 'brand', 'list_price']]
y = data['online_order']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

y_scores = clf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)
print(f"ROC AUC: {roc_auc}")


plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area =%0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve')
plt.legend(loc="lower right")
plt.show()


