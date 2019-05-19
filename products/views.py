from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def all_products(request):
    products = Product.objects.all() # returns all the products in the db
    return render(request, "products.html", {"products":products})
    
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "product_details.html", {"product": product})


    
    