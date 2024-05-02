import pandas as pd

df2024 = pd.read_csv('99bikes_2024.csv')
df2017 = pd.read_excel('99Bikers_Raw_data.xlsx')




# mtb = df2024.loc[(df2024['bike_class'] == 'mountain')]
# road = df2024.loc[(df2024['bike_class'] == 'road')]
# hybrid = df2024.loc[(df2024['bike_class'] == 'hybrid')]
#
#
# mean_price_mtb_2024 = mtb.groupby('bike_class')['full_price'].mean().round(2)
# mean_price_road_2024 = road.groupby('bike_class')['full_price'].mean().round(2)
# mean_price_hybrid_2024 = hybrid.groupby('bike_class')['full_price'].mean().round(2)
#
# print(f'{mean_price_mtb_2024}, {mean_price_road_2024},  {mean_price_hybrid_2024} ')
#
#
# mtb = df2017.loc[(df2017['product_line'] == 'Mountain')]
# road = df2017.loc[(df2017['product_line'] == 'Road')]
# hybrid = df2017.loc[(df2017['product_line'] == 'Touring')]
#
#
# mean_price_mtb_2017 = mtb.groupby('product_line')['list_price'].mean().round(2)
# mean_price_road_2017 = road.groupby('product_line')['list_price'].mean().round(2)
# mean_price_hybrid_2017 = hybrid.groupby('product_line')['list_price'].mean().round(2)
#
# print(f'{mean_price_mtb_2017}, {mean_price_road_2017},  {mean_price_hybrid_2017} ')

average_price24 = df2024.groupby('bike_class')['full_price'].mean().round(2)
print(f'2024 metu kainos: {average_price24}')

average_price17 = df2017.groupby('product_line')['list_price'].mean().round(2)
print(f'2017 metu kainos {average_price17}')