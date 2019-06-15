from django.test import TestCase
from .models import Product, Category

class TestProductModel(TestCase):
    
    def test_product_model(self):
        category = Category(name="Jeans")
        category.save()
        product = Product(name="test item",description="This is a test of the description", price=40.00, category=category)
        product.save()
        self.assertEqual(product.name,"test item")
        self.assertEqual(product.description,"This is a test of the description")
        self.assertEqual(product.price, 40.00)
        self.assertEqual(product.category,category)
        
    
    def test_product_name_is_string(self):
        product = Product(name="Generic name")
        self.assertEqual("Generic name", str(product))
        
        
    def test_category_name_is_string(self):
        category = Category(name="Jeans")
        self.assertEqual("Jeans", str(category))