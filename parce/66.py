import requests
from bs4 import BeautifulSoup

url = 'https://www.michael-smirnov.ru/'
response = requests.get(url)
l=[]
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('td', id='category')
for link in table.find_all('a', class_='source-title a14'):
    l.append(link.text)
with open('cat.txt', 'w') as file:
    print(*l, file=file, sep='\n')
    
