from django.shortcuts import render, redirect, reverse
from contacts.forms import ContactSubmissionForm
from django.contrib import auth, messages

# Create your views here.
# Create your views here.
def view_cart(request):
    """ This renders the cart contents page """
    if request.method =="POST":
        form =  ContactSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = ContactSubmissionForm()
    return render(request, "cart.html", {'form':form})


def add_to_cart(request, id):
    """Adds a specified quantity to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """ Adjust the quantity of an item in the cart """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0 :
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))