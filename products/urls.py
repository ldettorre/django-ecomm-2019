from django.conf.urls import url, include
from .views import all_products, product_details

urlpatterns = [
    url(r'^$', all_products, name="products"),
    url(r'^products/(?P<product_id>\d+)$', product_details, name="product_details"),
    ]