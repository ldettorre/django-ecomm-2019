from django.contrib import admin
from .models import Product, Category
# Register your models here.

#This will alow us to add new products through the admin panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'new_in')
    search_fields = ('name', 'price', 'category', 'new_in')#This allows admin to use a search feature when looking for specific products
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)

