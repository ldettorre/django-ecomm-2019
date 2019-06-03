from django.conf.urls import url, include
from .views import contact_submission

urlpatterns = [
    url(r'^contact_submission/$', contact_submission, name="contact_submission"),
    
    ]