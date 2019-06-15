from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Product, Category

class TestProductViews(TestCase):
    
    def test_all_products_page(self):
        all_products = self.client.get("/products/all/")
        self.assertEqual(all_products.status_code, 200)
       
    def test_get_page_for_product_that_does_not_exist(self):
        page = self.client.get("/products/999")
        self.assertEqual(page.status_code, 404)
        
    def test_product_details_page(self):
        category = Category(name="Jeans")
        category.save()
        product = Product(name="test item",description="This is a test of the description", price=40.00, category=category)
        product.save()

        product_details = self.client.get("/products/{0}".format(product.id))
        self.assertEqual(product_details.status_code, 200)
        self.assertTemplateUsed(product_details, "product_details.html")
