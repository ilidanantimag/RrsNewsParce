from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include
from .feed import Feedaviatsija, Feedavto_i_moto, Feedaktsii_obligatsii_syrevye_tovary, Feedbanki, Feedbasketbol, Feedbelarus, Feedbiatlon, Feedbiznes, Feedbirzhi, Feedblogi_forumy_sotsialnye_seti, Feedv_mire, Feedvzaimnye_fondy_i_etf, Feedglavnye_novosti_en, Feedglavnye_novosti_ru, Feeddengi, Feedderivativy_i_foreks, Feeddizajn, Feededinoborstva, Feedzhivotnyj_i_rastitelnyj_mir, Feedzakonodatelstvo, Feedzarubezhe, Feedzvezdy_shou_biznes_svetskaja_zhizn, Feedzdorove_krasota_meditsina, Feedigry_i_razvlechenija, Feedinvestitsii, Feedinternet_kompjutery_programmy, Feediskusstvo_istorija_kultura_literatura_religija_traditsii, Feedkino_i_televidenie, Feedkulinarija, Feedlegkaja_atletika, Feedmedia, Feedministerstva_i_vedomstva, Feedmnenija_i_kommentarii, Feedmoskva, Feedmuzyka, Feednauka_i_tehnologii_en, Feednauka_i_tehnologii_ru, Feednedvizhimost, Feedobo_vsem, Feedobrazovanie_rabota_karera, Feedobschestvo, Feedobjavlenija_tovary_uslugi, Feedoruzhie_i_vpk, Feedotdyh_puteshestvija_turizm, Feedpogoda, Feedpolitika, Feedproisshestvija_rassledovanija_kriminal, Feedpromyshlennost_i_selskoe_hozjajstvo, Feedregiony_rf, Feedreklama_marketing_pr, Feedrossija, Feedsankt_peterburg, Feedsport_en, Feedsport_ru, Feedstati_i_issledovanija, Feedstil_zhizni_i_moda, Feedtelekommunikatsii, Feedtennis, Feedtehnika_i_elektronika, Feedukraina, Feedfinansy_i_ekonomika_en, Feedfinansy_i_ekonomika_ru, Feedformula_1, Feedfutbol, Feedhokkej


urlpatterns = [
   url(r'^add_cat/$', views.add_cat, name='add_cat'),
   url(r'^add_chanal/$', views.add_chanal, name='add_chanal'),
   url(r'^filter/$', views.filter, name='filter'),
   url(r'^filter_cat/$', views.filter_cat, name='filter_cat'),
   url(r'^update/$', views.update, name='update'),
   url(r'^cat_post/$', views.cat_post, name='cat_post'),
   url(r'^date_time/$', views.date_time, name='date_time'),
   url(r'^rrs_link/$', views.rrs_link, name='rrs_link'),
   url(r'^feed_name/$', views.feed_name, name='feed_name'),
   url(r'^rrs_generator/$', views.rrs_generator, name='rrs_generator'),
   url(r'^add_image/$', views.add_image, name='add_image'),
   path('', views.index, name='index'),
   url(r'^chanal/(?P<slug>[-\w]+)$',views.chanal, name='chanal'),
   url(r'^(?P<pk>\d+)$', views.post_detail, name='post_detail'),


url(r'^feed/aviatsija/', Feedaviatsija(), name='post_feed'),
url(r'^feed/avto-i-moto', Feedavto_i_moto(), name='post_feed'),
url(r'^feed/aktsii-obligatsii-syrevye-tovary', Feedaktsii_obligatsii_syrevye_tovary(), name='post_feed'),
url(r'^feed/banki', Feedbanki(), name='post_feed'),
url(r'^feed/basketbol', Feedbasketbol(), name='post_feed'),
url(r'^feed/belarus', Feedbelarus(), name='post_feed'),
url(r'^feed/biatlon', Feedbiatlon(), name='post_feed'),
url(r'^feed/biznes', Feedbiznes(), name='post_feed'),
url(r'^feed/birzhi', Feedbirzhi(), name='post_feed'),
url(r'^feed/blogi-forumy-sotsialnye-seti', Feedblogi_forumy_sotsialnye_seti(), name='post_feed'),
url(r'^feed/v-mire', Feedv_mire(), name='post_feed'),
url(r'^feed/vzaimnye-fondy-i-etf', Feedvzaimnye_fondy_i_etf(), name='post_feed'),
url(r'^feed/glavnye-novosti-en', Feedglavnye_novosti_en(), name='post_feed'),
url(r'^feed/glavnye-novosti-ru', Feedglavnye_novosti_ru(), name='post_feed'),
url(r'^feed/dengi', Feeddengi(), name='post_feed'),
url(r'^feed/derivativy-i-foreks', Feedderivativy_i_foreks(), name='post_feed'),
url(r'^feed/dizajn', Feeddizajn(), name='post_feed'),
url(r'^feed/edinoborstva', Feededinoborstva(), name='post_feed'),
url(r'^feed/zhivotnyj-i-rastitelnyj-mir', Feedzhivotnyj_i_rastitelnyj_mir(), name='post_feed'),
url(r'^feed/zakonodatelstvo', Feedzakonodatelstvo(), name='post_feed'),
url(r'^feed/zarubezhe', Feedzarubezhe(), name='post_feed'),
url(r'^feed/zvezdy-shou-biznes-svetskaja-zhizn', Feedzvezdy_shou_biznes_svetskaja_zhizn(), name='post_feed'),
url(r'^feed/zdorove-krasota-meditsina', Feedzdorove_krasota_meditsina(), name='post_feed'),
url(r'^feed/igry-i-razvlechenija', Feedigry_i_razvlechenija(), name='post_feed'),
url(r'^feed/investitsii', Feedinvestitsii(), name='post_feed'),
url(r'^feed/internet-kompjutery-programmy', Feedinternet_kompjutery_programmy(), name='post_feed'),
url(r'^feed/iskusstvo-istorija-kultura-literatura-religija-traditsii', Feediskusstvo_istorija_kultura_literatura_religija_traditsii(), name='post_feed'),
url(r'^feed/kino-i-televidenie', Feedkino_i_televidenie(), name='post_feed'),
url(r'^feed/kulinarija', Feedkulinarija(), name='post_feed'),
url(r'^feed/legkaja-atletika', Feedlegkaja_atletika(), name='post_feed'),
url(r'^feed/media', Feedmedia(), name='post_feed'),
url(r'^feed/ministerstva-i-vedomstva', Feedministerstva_i_vedomstva(), name='post_feed'),
url(r'^feed/mnenija-i-kommentarii', Feedmnenija_i_kommentarii(), name='post_feed'),
url(r'^feed/moskva', Feedmoskva(), name='post_feed'),
url(r'^feed/muzyka', Feedmuzyka(), name='post_feed'),
url(r'^feed/nauka-i-tehnologii-en', Feednauka_i_tehnologii_en(), name='post_feed'),
url(r'^feed/nauka-i-tehnologii-ru', Feednauka_i_tehnologii_ru(), name='post_feed'),
url(r'^feed/nedvizhimost', Feednedvizhimost(), name='post_feed'),
url(r'^feed/obo-vsem', Feedobo_vsem(), name='post_feed'),
url(r'^feed/obrazovanie-rabota-karera', Feedobrazovanie_rabota_karera(), name='post_feed'),
url(r'^feed/obschestvo', Feedobschestvo(), name='post_feed'),
url(r'^feed/objavlenija-tovary-uslugi', Feedobjavlenija_tovary_uslugi(), name='post_feed'),
url(r'^feed/oruzhie-i-vpk', Feedoruzhie_i_vpk(), name='post_feed'),
url(r'^feed/otdyh-puteshestvija-turizm', Feedotdyh_puteshestvija_turizm(), name='post_feed'),
url(r'^feed/pogoda', Feedpogoda(), name='post_feed'),
url(r'^feed/politika', Feedpolitika(), name='post_feed'),
url(r'^feed/proisshestvija-rassledovanija-kriminal', Feedproisshestvija_rassledovanija_kriminal(), name='post_feed'),
url(r'^feed/promyshlennost-i-selskoe-hozjajstvo', Feedpromyshlennost_i_selskoe_hozjajstvo(), name='post_feed'),
url(r'^feed/regiony-rf', Feedregiony_rf(), name='post_feed'),
url(r'^feed/reklama-marketing-pr', Feedreklama_marketing_pr(), name='post_feed'),
url(r'^feed/rossija', Feedrossija(), name='post_feed'),
url(r'^feed/sankt-peterburg', Feedsankt_peterburg(), name='post_feed'),
url(r'^feed/sport-en', Feedsport_en(), name='post_feed'),
url(r'^feed/sport-ru', Feedsport_ru(), name='post_feed'),
url(r'^feed/stati-i-issledovanija', Feedstati_i_issledovanija(), name='post_feed'),
url(r'^feed/stil-zhizni-i-moda', Feedstil_zhizni_i_moda(), name='post_feed'),
url(r'^feed/telekommunikatsii', Feedtelekommunikatsii(), name='post_feed'),
url(r'^feed/tennis', Feedtennis(), name='post_feed'),
url(r'^feed/tehnika-i-elektronika', Feedtehnika_i_elektronika(), name='post_feed'),
url(r'^feed/ukraina', Feedukraina(), name='post_feed'),
url(r'^feed/finansy-i-ekonomika-en', Feedfinansy_i_ekonomika_en(), name='post_feed'),
url(r'^feed/finansy-i-ekonomika-ru', Feedfinansy_i_ekonomika_ru(), name='post_feed'),
url(r'^feed/formula-1', Feedformula_1(), name='post_feed'),
url(r'^feed/futbol', Feedfutbol(), name='post_feed'),
url(r'^feed/hokkej', Feedhokkej(), name='post_feed'),
  
   
]
