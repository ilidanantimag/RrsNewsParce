import requests
from bs4 import BeautifulSoup

#сслыки

url = 'https://www.michael-smirnov.ru/'
response = requests.get(url)
l=[]
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('td', id='category')
for link in table.find_all('a', class_='ahrefnews a13'):
    l.append(link.get('href'))
with open('link.txt', 'w') as file:
    print(*l, file=file, sep='\n')
    
