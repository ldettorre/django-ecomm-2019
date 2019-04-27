from django.db import models

# Create your models here.

#Below is the basic model for our product item we will list on the site.
class Product(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images")
    
    def __str__(self):
        return self.name