from django.shortcuts import render
from products.models import Category

def all_categories(request):
    all_categories = Category.objects.all()
    return{'all_categories':all_categories}
    
