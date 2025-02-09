import requests
from bs4 import BeautifulSoup


link = 'https://www.olx.kz/elektronika/igry-i-igrovye-pristavki/pristavki/karaganda/?search%5Bfilter_enum_console_manufacturers%5D%5B0%5D=2272'

response = requests.get(link).text

soup = BeautifulSoup(response, 'lxml')



main_div = soup.find('div', class_ = 'css-j0t2x2')

title_div = main_div.find_all('h4', class_ = 'css-1sq4ur2')


price_div = main_div.find_all('p', class_ = 'css-6j1qjp')



for i in range(len(title_div)):
    with open('text.txt', 'a', encoding='utf-8') as file:
        file.write(f'{title_div[i].text}, {price_div[i].text} \n')