from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254, default="", blank=False)
    
    def __str__(self):
        return self.name
    
#Below is the basic model for our product item we will list on the site.
class Product(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name