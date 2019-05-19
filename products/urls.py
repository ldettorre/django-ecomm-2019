from django.conf.urls import url, include
from .views import all_products, product_details

urlpatterns = [
    url(r'^all/$', all_products, name="all_products"),
    url(r'^(?P<product_id>\d+)$', product_details, name="product_details"),
    ]