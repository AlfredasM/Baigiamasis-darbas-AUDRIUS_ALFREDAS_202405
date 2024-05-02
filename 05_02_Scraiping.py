import requests
from bs4 import BeautifulSoup
import pandas as pd

# urls = ["https://www.99bikes.com.au/bikes/road", "https://www.99bikes.com.au/bikes/mountain",
#         "https://www.99bikes.com.au/electric/commuter"]
bikes_list = []

for i in range(1, 4):
    url = f"https://www.99bikes.com.au/bikes/road?page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    bikes = soup.find_all('li', class_='item product product-item')

    for bike in bikes:
        bike_name = bike.find('strong', class_='product name product-item-name').text.strip()
        full_price = bike.find('span', class_='full-price').text.strip().replace('$', '')
        club_price = bike.find('span', class_='special-price').text.strip().replace('$', '')
        bike_class = 'road'

        bikes_list.append({
            'bike_name': bike_name,
            'full_price': full_price,
            'club_price': club_price,
            'bike_class': bike_class

        })
for i in range(1, 11):
    url = f"https://www.99bikes.com.au/bikes/mountain?page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    bikes = soup.find_all('li', class_='item product product-item')

    for bike in bikes:
        bike_name = bike.find('strong', class_='product name product-item-name').text.strip()
        full_price = bike.find('span', class_='full-price').text.strip().replace('$', '')
        club_price = bike.find('span', class_='special-price').text.strip().replace('$', '')
        bike_class = 'mountain'

        bikes_list.append({
            'bike_name': bike_name,
            'full_price': full_price,
            'club_price': club_price,
            'bike_class': bike_class

        })
for i in range(1, 3):
    url = f"https://www.99bikes.com.au/electric/commuter?p={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    bikes = soup.find_all('li', class_='item product product-item')

    for bike in bikes:
        bike_name = bike.find('strong', class_='product name product-item-name').text.strip()
        full_price = bike.find('span', class_='full-price').text.strip().replace('$', '')
        club_price = bike.find('span', class_='special-price').text.strip().replace('$', '')
        bike_class = 'hybrid'

        bikes_list.append({
            'bike_name': bike_name,
            'full_price': full_price,
            'club_price': club_price,
            'bike_class': bike_class

        })

df = pd.DataFrame(bikes_list)

#df.to_csv('99bikes_2024.csv', index=False)