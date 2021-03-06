from django.contrib.syndication.views import Feed
from .models import Categories, Sources, RrsFeedItems,CategoriesPost
from django.urls import reverse



class Feedaviatsija(Feed):
    title = 'Авиация'
    link = '/aviatsija'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'aviatsija')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedavto_i_moto(Feed):
    title = 'Авто и мото'
    link = '/avto-i-moto'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'avto-i-moto')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedaktsii_obligatsii_syrevye_tovary(Feed):
    title = 'Акции облигации сырьевые товары'
    link = '/aktsii-obligatsii-syrevye-tovary'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'aktsii-obligatsii-syrevye-tovary')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedbanki(Feed):
    title = 'Банки'
    link = '/banki'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'banki')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedbasketbol(Feed):
    title = 'Баскетбол'
    link = '/basketbol'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'basketbol')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedbelarus(Feed):
    title = 'Беларусь'
    link = '/belarus'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'belarus')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedbiatlon(Feed):
    title = 'Биатлон'
    link = '/biatlon'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'biatlon')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedbiznes(Feed):
    title = 'Бизнес'
    link = '/biznes'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'biznes')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedbirzhi(Feed):
    title = 'Биржи'
    link = '/birzhi'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'birzhi')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedblogi_forumy_sotsialnye_seti(Feed):
    title = 'Блоги форумы социальные сети'
    link = '/blogi-forumy-sotsialnye-seti'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'blogi-forumy-sotsialnye-seti')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedv_mire(Feed):
    title = 'В мире'
    link = '/v-mire'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'v-mire')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedvzaimnye_fondy_i_etf(Feed):
    title = 'Взаимные фонды и ETF'
    link = '/vzaimnye-fondy-i-etf'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'vzaimnye-fondy-i-etf')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedglavnye_novosti_en(Feed):
    title = 'Главные новости en'
    link = '/glavnye-novosti-en'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'glavnye-novosti-en')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedglavnye_novosti_ru(Feed):
    title = 'Главные новости ru'
    link = '/glavnye-novosti-ru'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'glavnye-novosti-ru')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feeddengi(Feed):
    title = 'Деньги'
    link = '/dengi'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'dengi')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedderivativy_i_foreks(Feed):
    title = 'Деривативы и Форекс'
    link = '/derivativy-i-foreks'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'derivativy-i-foreks')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feeddizajn(Feed):
    title = 'Дизайн'
    link = '/dizajn'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'dizajn')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feededinoborstva(Feed):
    title = 'Единоборства'
    link = '/edinoborstva'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'edinoborstva')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedzhivotnyj_i_rastitelnyj_mir(Feed):
    title = 'Животный и растительный мир'
    link = '/zhivotnyj-i-rastitelnyj-mir'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'zhivotnyj-i-rastitelnyj-mir')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedzakonodatelstvo(Feed):
    title = 'Законодательство'
    link = '/zakonodatelstvo'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'zakonodatelstvo')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedzarubezhe(Feed):
    title = 'Зарубежье'
    link = '/zarubezhe'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'zarubezhe')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedzvezdy_shou_biznes_svetskaja_zhizn(Feed):
    title = 'Звёзды шоу-бизнес светская жизнь'
    link = '/zvezdy-shou-biznes-svetskaja-zhizn'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'zvezdy-shou-biznes-svetskaja-zhizn')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedzdorove_krasota_meditsina(Feed):
    title = 'Здоровье красота медицина'
    link = '/zdorove-krasota-meditsina'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'zdorove-krasota-meditsina')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedigry_i_razvlechenija(Feed):
    title = 'Игры и развлечения'
    link = '/igry-i-razvlechenija'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'igry-i-razvlechenija')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedinvestitsii(Feed):
    title = 'Инвестиции'
    link = '/investitsii'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'investitsii')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedinternet_kompjutery_programmy(Feed):
    title = 'Интернет компьютеры программы'
    link = '/internet-kompjutery-programmy'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'internet-kompjutery-programmy')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feediskusstvo_istorija_kultura_literatura_religija_traditsii(Feed):
    title = 'Искусство история культура литература религия традиции'
    link = '/iskusstvo-istorija-kultura-literatura-religija-traditsii'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'iskusstvo-istorija-kultura-literatura-religija-traditsii')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedkino_i_televidenie(Feed):
    title = 'Кино и телевидение'
    link = '/kino-i-televidenie'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'kino-i-televidenie')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedkulinarija(Feed):
    title = 'Кулинария'
    link = '/kulinarija'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'kulinarija')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedlegkaja_atletika(Feed):
    title = 'Лёгкая атлетика'
    link = '/legkaja-atletika'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'legkaja-atletika')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedmedia(Feed):
    title = 'Медиа'
    link = '/media'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'media')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedministerstva_i_vedomstva(Feed):
    title = 'Министерства и ведомства'
    link = '/ministerstva-i-vedomstva'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'ministerstva-i-vedomstva')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedmnenija_i_kommentarii(Feed):
    title = 'Мнения и комментарии'
    link = '/mnenija-i-kommentarii'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'mnenija-i-kommentarii')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedmoskva(Feed):
    title = 'Москва'
    link = '/moskva'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'moskva')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedmuzyka(Feed):
    title = 'Музыка'
    link = '/muzyka'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'muzyka')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feednauka_i_tehnologii_en(Feed):
    title = 'Наука и технологии en'
    link = '/nauka-i-tehnologii-en'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'nauka-i-tehnologii-en')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feednauka_i_tehnologii_ru(Feed):
    title = 'Наука и технологии ru'
    link = '/nauka-i-tehnologii-ru'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'nauka-i-tehnologii-ru')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feednedvizhimost(Feed):
    title = 'Недвижимость'
    link = '/nedvizhimost'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'nedvizhimost')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedobo_vsem(Feed):
    title = 'Обо всём'
    link = '/obo-vsem'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'obo-vsem')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedobrazovanie_rabota_karera(Feed):
    title = 'Образование работа карьера'
    link = '/obrazovanie-rabota-karera'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'obrazovanie-rabota-karera')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedobschestvo(Feed):
    title = 'Общество'
    link = '/obschestvo'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'obschestvo')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedobjavlenija_tovary_uslugi(Feed):
    title = 'Объявления товары услуги'
    link = '/objavlenija-tovary-uslugi'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'objavlenija-tovary-uslugi')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedoruzhie_i_vpk(Feed):
    title = 'Оружие и ВПК'
    link = '/oruzhie-i-vpk'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'oruzhie-i-vpk')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedotdyh_puteshestvija_turizm(Feed):
    title = 'Отдых путешествия туризм'
    link = '/otdyh-puteshestvija-turizm'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'otdyh-puteshestvija-turizm')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedpogoda(Feed):
    title = 'Погода'
    link = '/pogoda'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'pogoda')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedpolitika(Feed):
    title = 'Политика'
    link = '/politika'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'politika')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedproisshestvija_rassledovanija_kriminal(Feed):
    title = 'Происшествия расследования криминал'
    link = '/proisshestvija-rassledovanija-kriminal'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'proisshestvija-rassledovanija-kriminal')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedpromyshlennost_i_selskoe_hozjajstvo(Feed):
    title = 'Промышленность и сельское хозяйство'
    link = '/promyshlennost-i-selskoe-hozjajstvo'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'promyshlennost-i-selskoe-hozjajstvo')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedregiony_rf(Feed):
    title = 'Регионы РФ'
    link = '/regiony-rf'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'regiony-rf')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedreklama_marketing_pr(Feed):
    title = 'Реклама маркетинг PR'
    link = '/reklama-marketing-pr'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'reklama-marketing-pr')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedrossija(Feed):
    title = 'Россия'
    link = '/rossija'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'rossija')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedsankt_peterburg(Feed):
    title = 'Санкт-Петербург'
    link = '/sankt-peterburg'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'sankt-peterburg')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedsport_en(Feed):
    title = 'Спорт en'
    link = '/sport-en'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'sport-en')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedsport_ru(Feed):
    title = 'Спорт ru'
    link = '/sport-ru'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'sport-ru')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedstati_i_issledovanija(Feed):
    title = 'Статьи и исследования'
    link = '/stati-i-issledovanija'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'stati-i-issledovanija')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedstil_zhizni_i_moda(Feed):
    title = 'Стиль жизни и мода'
    link = '/stil-zhizni-i-moda'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'stil-zhizni-i-moda')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedtelekommunikatsii(Feed):
    title = 'Телекоммуникации'
    link = '/telekommunikatsii'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'telekommunikatsii')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedtennis(Feed):
    title = 'Теннис'
    link = '/tennis'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'tennis')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedtehnika_i_elektronika(Feed):
    title = 'Техника и электроника'
    link = '/tehnika-i-elektronika'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'tehnika-i-elektronika')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedukraina(Feed):
    title = 'Украина'
    link = '/ukraina'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'ukraina')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedfinansy_i_ekonomika_en(Feed):
    title = 'Финансы и экономика en'
    link = '/finansy-i-ekonomika-en'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'finansy-i-ekonomika-en')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedfinansy_i_ekonomika_ru(Feed):
    title = 'Финансы и экономика ru'
    link = '/finansy-i-ekonomika-ru'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'finansy-i-ekonomika-ru')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedformula_1(Feed):
    title = 'Формула-1'
    link = '/formula-1'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'formula-1')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedfutbol(Feed):
    title = 'Футбол'
    link = '/futbol'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'futbol')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   
class Feedhokkej(Feed):
    title = 'Хоккей'
    link = '/hokkej'
    description = '/'
    def items(self):
        cat = CategoriesPost.objects.get(slug = 'hokkej')
        return RrsFeedItems.objects.filter(categories=cat.id).order_by('-data_time')
    def item_title(self, item):
        return item.title_post
    def item_enclosure_url(self, item):
        return item.image_post
    def item_pubdate(self, item):
        return item.data_time
    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])
    def item_description(self, item):
        return item.description_post
   