from django.contrib import admin
from .models import Posting

from django.contrib import admin

from .models import Subscriber
from .models import Product

admin.site.register(Posting)



admin.site.register(Subscriber)


class PostAdmin(admin.ModelAdmin):
    # Добавим в начало столбец pk
    list_display = ('pk', 'text', 'pub_date', 'author') 
    search_fields = ('text',) 
    list_filter = ('pub_date',) 






@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
