from django.shortcuts import get_object_or_404
from products.models import Product

#This app focuses on keeping the items in a session and then it removes them upon logging out

def cart_contents(request):
    """ Makes cart contents viewable on every page """
    cart = request.session.get('cart', {})
    
    cart_items = []
    delivery_charge = 15
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({"id":id, "quantity":quantity,"product":product})
    # The below code adds a 'delivery charge' if the total is below the minimum required
    if total <= 49.99:
        total = total + delivery_charge
    else:
        total = total
        
    return { "cart_items":cart_items, "total":total,"product_count":product_count }
    
    
    