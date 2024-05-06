import pandas as pd
import matplotlib.pyplot as plt

df2017 = pd.read_excel('99Bikers_Raw_data.xlsx')
df2024 = pd.read_csv('99bikes_2024.csv')

# reiksmiu pakeitimas
values = {
    'Mountain': 'Mountain',
    'Road': 'Road',
    'Standard': 'Cruiser/Standart',
    'Touring': 'Touring/Hybrid'
}
# reiksmiu perrasymas, kad grafikas tiksliau atsispindetu
df2017['product_line'] = df2017['product_line'].replace(values)

average_price2017 = df2017.groupby('product_line')['list_price'].mean().round(2).sort_values()
average_price2024 = df2024.groupby('bike_class')['full_price'].mean().round(2).sort_values()
print(f'Average price for 2017: {average_price2017}\nAverage price for 2024: {average_price2024}')

plt.figure(figsize=(10, 8))
#  2017 metu grafikas
plt.bar(average_price2017.index, average_price2017.values, width=0.5, label='2017 price', color='red')
# 2024 metu grafikas
plt.bar(average_price2024.index, average_price2024.values, width=0.5, label='2024 price', color='green', align='edge')

plt.xlabel('Categories')
plt.ylabel('Average Price')
plt.title('Average Prices by Class for 2017 and 2024')
plt.legend()
plt.show()