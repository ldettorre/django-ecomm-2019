from django.contrib import admin
from .models import Product, Category
# Register your models here.

#This will alow us to add new products through the admin panel

admin.site.register(Product)
admin.site.register(Category)