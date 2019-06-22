from django.shortcuts import render, get_object_or_404
from .models import Product, Category
# Create your views here.

def all_products(request):
    products = Product.objects.all() # returns all the products in the db.
    return render(request, "products.html", {"products":products})
    
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_details.html", {"product": product})
    

def view_category(request, category): 
    category = get_object_or_404(Category, name=category)
    products = Product.objects.filter(category = category) #returns products filtered by chosen category.
    return render(request, "products.html", {"products":products})

def new_in(request):
    products = Product.objects.filter(new_in=True) # returns all the products in the db that are marked as new items
    return render(request, "products.html", {"products":products})
    
    
    