from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    delivery_charge = 15
    if request.method=="POST":
        order_form = OrderForm(request.POST) #contains their personal details
        payment_form = MakePaymentForm(request.POST) #contains payment information
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now() 
            order.save()
            
            cart = request.session.get('cart', {})
            total = 0
            sub_total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                sub_total += quantity * product.price
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
                #The below code add's a delivery charge of 15 EUR to all orders below or equal to 50
                if total <= 50:
                    total = total + delivery_charge
                else:
                    total = total
            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data["stripe_id"],
                    )
            except stripe.error.CardError:
                messages.error(request,"Your card was declined.")
            
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart']= {}
                return redirect('index')
            else: 
                messages.error(request, "This payment was not successfull")
        else:
            print(payment_form.errors)
            messages.error(request,"We were unable to take a payment from this card.")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        
    return render(request, "checkout.html", {'order_form':order_form, 'payment_form':payment_form, 'publishable':settings.STRIPE_PUBLISHABLE})
                