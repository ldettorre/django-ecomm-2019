from django.contrib import admin
from .models import Product
# Register your models here.

#This will alow us to add new products through the admin panel

admin.site.register(Product)