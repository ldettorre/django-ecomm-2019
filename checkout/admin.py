from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )
    list_display = ('full_name', 'contact_number', 'date')
    search_fields = ('full_name', 'contact_number', 'date') #This allows admin to use a search feature when looking for specific contact submissions
    
admin.site.register(Order, OrderAdmin)
