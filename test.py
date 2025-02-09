import requests
from bs4 import BeautifulSoup


link = 'https://www.dns-shop.kz/catalog/actual/13963825-4034-4ce1-94d0-41fc78eb6d15/?stock=now-today-tomorrow-later&category=17a892f816404e77'

response = requests.get(link).text

soup = BeautifulSoup(response, 'lxml')



main_div = soup.find('div', class_ = 'css-products-page')

title_div = main_div.find_all('h4', class_ = 'css-products-page__content')


price_div = main_div.find_all('p', class_ = 'css-products-page__list')



for i in range(len(title_div)):
    with open('text.txt', 'a', encoding='utf-8') as file:
        file.write(f'{title_div[i].text}, {price_div[i].text} \n')