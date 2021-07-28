from __future__ import absolute_import
import os,sys
from celery import Celery
from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
app = Celery("news")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()









from celery.schedules import crontab

app.conf.beat_schedule = {

        'update': {
        'task': 'update',
        'schedule': crontab(minute=0, hour=0)
    },
}

app.conf.timezone = 'Europe/Minsk'


@app.task(name='update')
def feed_name():
    from rrs.models import Categories, Sources, RrsFeedItems, CategoriesPost
    import requests
    from bs4 import BeautifulSoup
    import time
    import datetime
    from dateutil.parser import parse
    from django.db.models import Count
    import os


    #Вынес из обновления в одельные функции для наглядности 









    #Достаю картинки из описания
    def add_image():
        print('Достаю картинки из описания')
        img = RrsFeedItems.objects.all()
        a=0
        for i in img:
            if i.image_post == '':
                soup = BeautifulSoup(i.description_post, 'lxml')
                if soup.find('img') is None:
                    print("None")
                else:    
                    lin = soup.find_all('img')[0]
                    l=lin.get('src')
                    l = l.replace('[','')
                    l= l.replace(']','')
                    l = l.replace("'",'')
                    l = l.replace(",",'')
                    i.image_post = l
                    i.save()
                    a=a+1
                    print(a)
                    print('Достаю картинки из описания')
    
    #Добавляю категории к новостям
    def cat_post():
        print("Добавляю категории к новостям")
        items = RrsFeedItems.objects.all()
        cat=Categories.objects.get(title='Хоккей')
        a=0
        sour = Sources.objects.all()
        for s in sour:
            cat = Categories.objects.filter(categories=s)
            for c in cat:
                item = RrsFeedItems.objects.filter(soures=s.id)
                for i in item:
                    for p in CategoriesPost.objects.filter(title=c.title):
                        i.categories.add(p)
                        a=a+1
                        print(a)
                        print("Добавляю категории к новостям")
        add_image()


        #строку в DataTime
    def date_time():
        print("строку в DataTime")
        items = RrsFeedItems.objects.all()
        a=0
        for i in items:
            print(i.title_post)
            print(i.pub_date)
            if i.pub_date is None:
                print('Нет дат')
            else:
                try:
                    data = parse(i.pub_date)
                    i.data_time=data
                    i.save()
                    a=a+1
                    print(a) 
                    print(i.data_time)
                    print("Преобразовываю спаршеную строку в DataTime")
                except:
                    print('error')        
        cat_post()











#Update_)))
    def update():
        print("обновление")
        sour = Sources.objects.all()
        a=0
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
        for i in sour:
            time.sleep(0)
            b=0
            url = i.link
            try: 
                r = requests.get(url, headers=headers)
            except:
                print("error")    
            print(url)
            if r.status_code == 200:
                print("200")
                soup = BeautifulSoup(r.content, 'xml')
                if soup.find_all('item') == []:
                    if soup.find('feed') is None:
                        pub ='Нет дат'
                    else:
                        pub = soup.find('feed')    
                        pub= pub.find_all('entry')[0]
                        if pub.find('published') is None:
                            pub = "Нет дат"
                        else:
                            pub = pub.find('published').text
                else:
                    pub = soup.find_all('item')[0]
                    if pub.find('pubDate') is None:
                        if pub.find('dc:date') is None:
                            pub ='Нет дат'
                        else:    
                            pub = pub.find('dc:date').text
                            
                    else:    
                        pub = pub.find('pubDate').text
                print(pub)
                if i.lastBuildDate == pub:
                    print('Обновления не требуются')                       
                if i.lastBuildDate != pub:
                    feedItem = RrsFeedItems.objects.filter(soures=i).delete()
                    i.lastBuildDate = pub
                    i.save()     
                    item = soup.find_all('item')
                    if item == []:
                        entry = soup.find('feed')
                        entry = soup.find_all('entry')
                        for en in entry:
                            if b !=5:
                                if en.find('title') is None:
                                    title_post="Нет заголовка"
                                else:       
                                    title_post = en.find('title').text
                                print(title_post)
                                if en.find('id') is None:
                                    link_post ="Нет ссылки"
                                else:    
                                    link_post = en.find('id').text
                                print(link_post)
                                if en.find('content') is None:
                                    description_post="Нет описания"
                                else:    
                                    description_post = en.find('content').text
                                if en.find('published') is None:
                                    pub_date="Нет даты"
                                else:     
                                    pub_date = en.find('published').text
                                print(pub_date)
                                if en.find('enclosure') is None:
                                    if en.find('image') is None:
                                        pub_image=""
                                    else:
                                        pub_image=en.find('image').get('url')   
                                else:          
                                    pub_image=en.find('enclosure').get('url')
                                print(pub_image)    
                                new_pub = RrsFeedItems.objects.create(title_post=title_post, link_post=link_post,
                                description_post=description_post, pub_date=pub_date, image_post=pub_image, soures=i )
                                b = b+1
                                print('Ok')   

                    for it in item:
                        if b !=5:
                            if it.find('title') is None:
                                title_post="Нет заголовка"
                            else:       
                                title_post = it.find('title').text
                            print(title_post)
                            if it.find('link') is None:
                                link_post ="Нет ссылки"
                            else:    
                                link_post = it.find('link').text
                            print(link_post)
                            if it.find('description') is None:
                                description_post="Нет описания"
                            else:    
                                description_post = it.find('description').text
                            if it.find('pubDate') is None:
                                pub_date="Нет даты"
                            else:     
                                pub_date = it.find('pubDate').text
                            print(pub_date)
                            if it.find('enclosure') is None:
                                if it.find('image') is None:
                                    pub_image=""
                                else:
                                    pub_image=it.find('image').get('url')   
                            else:          
                                pub_image=it.find('enclosure').get('url')
                            print(pub_image)    
                            new_pub = RrsFeedItems.objects.create(title_post=title_post, link_post=link_post,
                            description_post=description_post, pub_date=pub_date, image_post=pub_image, soures=i )
                            b = b+1

                            print('Ok')    
            a =a+1     
            print(a)
            i.save()
                
            if r.status_code !=200:
                print("404")
        date_time()            


    update(),
    
    
    
