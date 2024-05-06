from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from scikeras.wrappers import KerasClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

df1 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='Transactions')
df2 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerDemographic')
df3 = pd.read_excel('99Bikers_Raw_data.xlsx', sheet_name='CustomerAddress')

data = pd.merge(pd.merge(df1, df2, on='customer_id'), df3, on='customer_id')

median_price = data['list_price'].median()
data['Price_above_median'] = (data['list_price'] > median_price).astype(int)

features = ['product_line', 'past_3_years_bike_related_purchases', 'product_size', 'product_class', 'brand']
target = 'Price_above_median'

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['past_3_years_bike_related_purchases']),
        ('cat', OneHotEncoder(), ['product_line', 'product_size', 'product_class', 'brand'])
    ])


def create_model():
    model = Sequential([
        Dense(64, activation='relu', input_dim=X_train_preprocessed.shape[1]),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.4, random_state=42)

X_train_preprocessed = preprocessor.fit_transform(X_train)
X_test_preprocessed = preprocessor.transform(X_test)

model = KerasClassifier(build_fn=create_model, epochs=5, batch_size=1, verbose=1)
model._estimator_type = "classifier"
history = model.fit(X_train_preprocessed, y_train)

accuracy = model.score(X_test_preprocessed, y_test)
test_loss = model.score(X_test_preprocessed, y_test)
val_accuracy = model.score(X_train_preprocessed, y_train)
train_loss = model.score(X_train_preprocessed, y_train)

plt.figure(figsize=(10, 8))
plt.title('Accuracy and loss by epoch')
plt.plot(history.history_['accuracy'], label='Accuracy')
plt.plot(history.history_['loss'], label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='best')
plt.show()

print(f'Model accuracy: {accuracy:.4f}')

if 'val_accuracy' in history.history_:
    accuracy = history.history_['val_accuracy'][-1]
    print(f'Model accuracy: {accuracy:.4f}')
else:
    print('Validation accuracy not available in the history')

plt.figure(figsize=(10, 8))
plt.plot(history.history_['accuracy'], label='Train')
plt.plot(history.history_['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()
plt.show()

plt.figure(figsize=(10, 8))
plt.plot(history.history_['loss'], label='Train')
plt.plot(history.history_['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()
plt.show()

