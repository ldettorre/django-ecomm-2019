from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'email', 'details', 'submission_date')
    search_fields = ('full_name', 'phone_number', 'email') #This allows admin to use a search feature when looking for specific contact submissions
    
    
admin.site.register(Contact, ContactAdmin)

# Register your models here.