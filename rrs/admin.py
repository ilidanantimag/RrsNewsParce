from django.contrib import admin
from .models import Categories, Sources, RrsFeedItems, CategoriesPost



@admin.register(RrsFeedItems)
class RrsFeedItemsAdmin(admin.ModelAdmin):
    list_display = ('title_post',)

@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(CategoriesPost)
class СategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')


@admin.register(Categories)
class СategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','col')
    
    
 

    
    
    


