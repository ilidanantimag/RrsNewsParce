from django.shortcuts import render
from .models import Categories, Sources, RrsFeedItems, CategoriesPost
from bs4 import BeautifulSoup
from django.db.models import Count
import os
import transliterate
import requests
import time
import datetime
from dateutil.parser import parse
from django.http import HttpResponse
import feedparser
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_detail(request, pk=None):
    news = RrsFeedItems.objects.filter(id=pk)
    cat=CategoriesPost.objects.all()
    return render(request,
            'detail.html',
                context={
                    'cat':cat,
                    'news': news,
               
  

            },)




def index(request, slug=None, id =None):   
    cat=CategoriesPost.objects.all()
    l =[]
    feed = feedparser.parse('http://127.0.0.1:8000/rrs/feed/glavnye-novosti-ru')
    paginator = Paginator(feed['items'],10)
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        posts = paginator.page(1)  
    except EmptyPage:  
        posts = paginator.page(paginator.num_pages)
    
    
    return render(request,
            'reader.html',
                context={
                    'cat': cat,
                    'page': page,
                    'posts':posts,

            },)

###Страница канала ###
def chanal(request, slug=None, id=None ):   
    cat=CategoriesPost.objects.all()
    l =[]
    feed = feedparser.parse('http://127.0.0.1:8000/rrs/feed/'+slug)
    paginator = Paginator(feed['items'],10)
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        posts = paginator.page(1)  
    except EmptyPage:  
        posts = paginator.page(paginator.num_pages)
    
    
    return render(request,
            'reader.html',
                context={
                    'cat': cat,
                    'page': page,
                    'posts':posts,

            },)



#Все функции можно открыть через урл







                
                    






# Имена каналов для импорта
def feed_name():
    cat=CategoriesPost.objects.all()
    z=[]
    for c in cat:
        rep = c.slug.replace('-','_') 
        a='Feed'+rep+','
        z.append(a)
    module_dir = os.path.dirname(__file__)  
    path = os.path.join(module_dir, 'feed_name.txt')
    with open(path, 'w') as file:
        print(*z, file=file, sep=' ')    


#Генерирую ссылки для каналов 
def rrs_link():
    cat=CategoriesPost.objects.all()
    z =[]
    for c in cat:
        rep = c.slug.replace('-','_')
        url =  "url(r'^feed/"+c.slug+"'"", Feed"+rep+"(), name='post_feed'),"
        z.append(url)
    module_dir = os.path.dirname(__file__)  
    path = os.path.join(module_dir, 'rrs_url.txt')
    with open(path, 'w') as file:
        print(*z, file=file, sep='\n')


#Создаю каналы feed.py
def rrs_generator():
    cat=CategoriesPost.objects.all()
    z=[]
    for c in cat:
        rep = c.slug.replace('-','_') 
        a='class Feed'+rep+'(Feed):'  
        b="    title = '"+c.title+"'"      
        y="    link = '/"+c.slug+"'"  
        d="    description = '/'"
        f="    def items(self):"
        i="        cat = CategoriesPost.objects.get(slug = '"+c.slug+"')"  
        e="        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')" 
        g="    def item_title(self, item):"  
        h="        return item.title_post"
        aa="    def item_enclosure_url(self, item):"
        bb="        return item.image_post"
        cc="    def item_pubdate(self, item):"
        dd="        return item.data_time" 
        l="    def item_link(self, item):"
        o="        return reverse('post_detail', args=[item.pk])"
        p="    def item_description(self, item):"
        w="        return item.description_post"
        x ="   "
        z.append(a)
        z.append(b)
        z.append(y)
        z.append(d)
        z.append(f)
        z.append(i)
        z.append(e)
        z.append(g)
        z.append(h)
        z.append(aa)
        z.append(bb)
        z.append(cc)
        z.append(dd)
        z.append(l)
        z.append(o)
        z.append(p)
        z.append(w)
        z.append(x)
    print(z)   
    module_dir = os.path.dirname(__file__)  
    path = os.path.join(module_dir, 'rrs_generator.txt')
    with open(path, 'w') as file:
        print(*z, file=file, sep='\n')
    













#Update_)))
def update():
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
                #Не заморачивался с фильтром просто удалил все новости с этого источника 
                #И добавил новые 
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
    return render(request,
    'index.html'
    )               

#Добавляю категории к новостям

def cat_post(request):
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
                
#Достаю картинки из описания
def add_image():
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





#Преобразовываю спаршеную строку в DataTime

def date_time(requests):
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
            except:
                print('error')        
    return render(request,
    'index.html'
    )   









#Создание базы данных


#Добавляю категории к источникам

def add_cat():
    rr = Categories.objects.all()
    cat = []
    col = []
    a = 0
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'cat.txt')
    module_col = os.path.dirname(__file__)  
    col_path = os.path.join(module_col, 'col.txt')
    for line in open(file_path).readlines():
        c = line.split()
        cat.append(c)
    for l in open(col_path).readlines():
        coli = l.split()
        col.append(coli)    
    
    while a < len(cat):
            title = cat[0+a]
            num = col[0+a]
            title = str(title)
            num = str(num)
            num = num.replace('(','')
            num = num.replace(')','')
            num = num.replace('[','')
            num = num.replace(']','')
            num = num.replace("'",'')
            num = num.replace(',','')
            title = title.replace('[','')
            title = title.replace(']','')
            title = title.replace("'",'')
            title = title.replace(",",'')
            add_num = num
            add_title = title
            add_slug = transliterate.slugify(title)
            
            new_cat = CategoriesPost.objects.create(title=add_title, slug=add_slug)
            a=a+1   
   
#Добавляю источники    
def add_chanal():
    cat = []
    col = []
    a = 0
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'title.txt')
    module_col = os.path.dirname(__file__)  
    col_path = os.path.join(module_dir, 'lins.txt')
    for line in open(file_path).readlines():
        c = line.split()
        cat.append(c)
    for l in open(col_path).readlines():
        coli = l.split()
        col.append(coli)    
    
    while a < len(cat):
            title = cat[0+a]
            num = col[0+a]
            title = str(title)
            num = str(num)
            num = num.replace('[','')
            num = num.replace(']','')
            num = num.replace("'",'')
            num = num.replace(',','')
            title = title.replace('[','')
            title = title.replace(']','')
            title = title.replace("'",'')
            title = title.replace(",",'')
            add_num = num
            add_title = title
            
            
            new_cat = Sources.objects.create(title=add_title, link=add_num, )
            a=a+1   


# удаляю повторяющиеся источники    
def filter(reqest):
    for row in Sources.objects.all().reverse():
        if Sources.objects.filter(link=row.link).count() > 1:
            row.delete()  
   
#добавляю к истоникам категории    
def filter_cat(request):
    module_dir = os.path.dirname(__file__)  
    link_path = os.path.join(module_dir, 'lins.txt')
    link = []
    link2 = []
    sour=Sources.objects.all()
    a=0    
    for line in open(link_path).readlines():
        c = line.split()
        link.append(c)
        link2.append(c)        
    b=0
    c=0
    for i in Categories.objects.all():
        link = link2
        i.col=int(i.col)
        c=i.col 
        print('ЦИКЛ ФОР')
        a=0
        link=link[b:]        
        while a < c:
            add_link = link[0+a]              
            add_link = str(add_link)
            add_link = add_link.replace('[','')
            add_link = add_link.replace(']','')
            add_link = add_link.replace("'",'')
            add_link = add_link.replace(",",'')
            sour = Sources.objects.get(link=add_link)
            print(sour.title)
            print(i)
            b=b+1
            a=a+1
            sour.categories.add(i)
            print(b)
    return render(request,
    'index.html'
    )   










	

		



    
    
    
    
