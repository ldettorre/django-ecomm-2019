from django.conf.urls import url, include
from .views import all_products, product_details, view_category

urlpatterns = [
    url(r'^all/$', all_products, name="all_products"),
    url(r'^(?P<product_id>\d+)$', product_details, name="product_details"),
    url(r'^(?P<category>[a-zA-Z]+)/$', view_category, name="category"),
    ]