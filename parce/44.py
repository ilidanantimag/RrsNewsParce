import requests
from bs4 import BeautifulSoup	
import time
import random
import os

headers = {
   'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
}
urls=[]
for line in open('link.txt').readlines():
    url = line.split()
    urls.append(url)

b = 0;
i = 1
while i != 0:
    def parc (b):    
        a = 0
        print(b)
        if b >= a:
            a =b 
        l=[]
        c = 0
        while a < len(urls):
            link = urls[0+a]
            link = str(link)
            link = link.replace('[','')
            link = link.replace(']','')
            link = link.replace("'",'')
            url = link
            r = requests.get(url, headers=headers,)
            if r.status_code == 200:
                if c == 9:
                    os.system('sudo protonvpn connect --cc NL')
                    b = a
                    parc(b)
                                  
                soup = BeautifulSoup(r.text, 'lxml')
                lin = soup.find('td', id='mctitleID')
                lin = lin.find_all('a')[1]
                print(lin)
                l=[lin.get('href')]
                a=a+1
                c = c+1         
                print('готово')
                print(a)
                print(l)
                with open("lins.txt", "a") as file:
                    print(*l, file=file, sep="\n")
                time.sleep(random.randint(3, 6))
            if r.status_code == 404:
                print(404)          
                os.system('sudo protonvpn connect --cc NL')
                a=a;
                b=a;
                parc(b)
        
            
            
    parc(b)

          
    



