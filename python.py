from bs4 import BeautifulSoup
import requests
from csv import writer

url = "http://www.scrapethissite.com/pages/simple/"
page = requests.get(url)

document = BeautifulSoup(page.content, 'html.parser')
divs = document.find_all('div', class_='col-md-4 country')

with open('Population.csv', 'w', encoding='utf8', newline='') as file:
    thewriter = writer(file)
    header = ['Name', 'Capital', 'Population', 'Area']
    thewriter.writerow(header)
    for div in divs:
        name = div.find('h3', class_ = 'country-name').text.replace('\n', '')
        capital = div.find('span', class_ = 'country-capital').text.replace('\n', '')
        population = div.find('span', class_ = 'country-population').text.replace('\n', '')
        area = div.find('span', class_ = 'country-area').text.replace('\n', '')

        info = [name, capital, population, area]
        thewriter.writerow(info)
        print(info)
