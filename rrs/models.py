from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid

class Categories(models.Model): 
    title = models.CharField(max_length=200, db_index=True, help_text="Категория ленты")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    col = models.CharField(max_length=200, db_index=True, help_text="col")
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

class Sources(models.Model):
    title = models.CharField(max_length=200, db_index=True, help_text="Категория ленты")
    link = models.CharField(max_length=200, db_index=True, help_text="Сылка rrs")
    categories = models.ManyToManyField('Categories',null=True, related_name='categories' )
    lastBuildDate =  models.CharField(max_length=200, null=True,)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Источники'
        verbose_name_plural = 'Источники'


class CategoriesPost(models.Model): 
    title = models.CharField(max_length=200, db_index=True, help_text="Категория ленты")
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
    def get_absolute_url(self):
        return reverse('chanal', args=[str(self.slug)])    
    





class RrsFeedItems(models.Model):
    soures = models.ForeignKey('Sources', on_delete=models.SET_NULL, null=True)
    categories = models.ManyToManyField('CategoriesPost',null=True, related_name='categories_post' )
    title_post = models.CharField(db_index=True, max_length = 200,null=True,)
    link_post = models.CharField(db_index=True, max_length = 200,null=True,)
    image_post = models.CharField(max_length=200, null=True,)
    description_post = models.TextField(null=True,)
    pub_date = models.CharField(max_length=200, null=True,)
    date =  models.DateTimeField(auto_now_add=True, null=True)
    data_time = models.DateTimeField(null=True)
    def get_absolute_url(self):
        return reverse('post_feed', args=[str(self.id)])
 

