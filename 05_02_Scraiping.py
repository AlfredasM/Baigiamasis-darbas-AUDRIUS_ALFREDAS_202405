import requests
from bs4 import BeautifulSoup
import pandas as pd

#pasirašome funkciją puslapiui nuskaityti
def obtain_page(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

#funkcija duomenims nusiurbti, kuriuos įmanoma nusiurbti ir sukelti į žodyną. Pasisekė, kad HTML kodas paprastas.
def parse_bikes(soup, bike_class):
    bikes_list = []
    bikes = soup.find_all('li', class_='item product product-item')
    for bike in bikes:
        bike_name = bike.find('strong', class_='product name product-item-name').text.strip()
        full_price = bike.find('span', class_='full-price').text.strip().replace('$', '').replace(',', '')
        club_price = bike.find('span', class_='special-price').text.strip().replace('$', '').replace(',', '')

        bikes_list.append({
            'bike_name': bike_name,
            'full_price': full_price,
            'club_price': club_price,
            'bike_class': bike_class
        })
    return bikes_list

#funkcija reikalinga suskirstyti dviračius pagal klases, čia panaudojam dvigubą ciklą gauti kiekvieną klasę ir
# nuskaityti visus puslapius. Taip gauname visus reikalingus duomenis.
def scrape_bikes():
    bike_types = {
        'Road': (1, 4, "https://www.99bikes.com.au/bikes/road?page="),
        'Mountain': (1, 11, "https://www.99bikes.com.au/bikes/mountain?page="),
        'Touring/Hybrid': (1, 3, "https://www.99bikes.com.au/electric/commuter?p="),
        'Cruiser/Standart': (1, 2, "https://www.99bikes.com.au/bikes/cruiser?p=")
    }

    all_bikes = []
    for bike_class, (first_page, last_page, base_url) in bike_types.items():
        for i in range(first_page, last_page):
            url = f"{base_url}{i}"
            soup = obtain_page(url)
            bikes = parse_bikes(soup, bike_class)
            all_bikes.extend(bikes)

    return all_bikes

#Liko gražiai viską sukelti į csv failą ir surikiuojam pagal pavadinimą. GOTCHA!
def main():
    bikes_list = scrape_bikes()
    df = pd.DataFrame(bikes_list).sort_values(by='bike_name')
    #print(df)
    df.to_csv('99bikes_2024.csv', index=False)
    print('GOTCHA!')


if __name__ == "__main__":
    main()