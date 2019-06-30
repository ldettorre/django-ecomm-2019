from django.conf.urls import url, include
from .views import contact_submission, faq_page, about_page

urlpatterns = [
    url(r'^contact_submission/$', contact_submission, name="contact_submission"),
    url(r'^faq_page/$', faq_page, name="faq_page"),
    url(r'^about_page/$', about_page, name="about_page"),
    
    ]