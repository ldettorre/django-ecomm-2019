from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User



class TestAccountsViews(TestCase):
    
    def test_get_login_page(self):
        login_page = self.client.get("/accounts/login", follow=True)
        self.assertEqual(login_page.status_code, 200)
        self.assertTemplateUsed(login_page, "login.html")
        
    def test_get_registration_page(self):
        registration_page = self.client.get("/accounts/register/")
        self.assertEqual(registration_page.status_code, 200)
        self.assertTemplateUsed(registration_page, "registration.html")
    
    def test_get_user_profile_page(self):
        user = User.objects.create_user(username="admin", password="String1")
        self.client.login(username="admin", password="String1")
        profile_page = self.client.get("/accounts/profile", follow=True)
        self.assertEqual(profile_page.status_code, 200)
        self.assertTemplateUsed(profile_page, "profile.html")
    
    
