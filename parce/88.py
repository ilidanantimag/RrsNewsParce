import requests
from bs4 import BeautifulSoup

# Количество сслылок в категории
url = 'https://www.michael-smirnov.ru/'
response = requests.get(url)
l=[]
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('td', id='category')
for link in table.find_all('span', class_='a12 a12color'):
    l.append(link.text)
with open('col.txt', 'w') as file:
    print(*l, file=file, sep='\n')
    #!/usr/bin/python3

print("give me a bottle of rum!")
