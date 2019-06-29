from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    details = models.TextField(max_length=400)
    submission_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __str__(self):
        return self.full_name
    