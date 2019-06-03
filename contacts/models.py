from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    details = models.TextField(max_length=400)
    
    def __str__(self):
        return self.name
    