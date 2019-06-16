from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User

# Create your tests here.
class TestAccountsForms(TestCase):
    
    def test_user_registration_form(self):
     form = UserRegistrationForm({
         "username": "admin", 
         "email":"example@example.com",
         "password1":"String1",
         "password2":"String1"
         
     })
     self.assertTrue(form.is_valid())
     
    def test_username_is_unique_for_registration(self):
     
     User.objects.create_user(
            username="admin",
            email="example@example.com")
            
     form = UserRegistrationForm({
         "username": "admin", 
         "email":"example@example.com",
         "password1":"String1",
         "password2":"String1"
         
     })
     self.assertFalse(form.is_valid())
     
     
    def test_user_login_form(self):
     form = UserLoginForm({
         "username": "admin",
         "password":"String1"
         
     })
     self.assertTrue(form.is_valid())
     
     
    def test_password_is_required_for_login(self):
     form = UserLoginForm({
         "username": "admin",
         "password":""
         
     })
     self.assertFalse(form.is_valid())
     self.assertEqual(form.errors["password"], ["This field is required."])
    
    
    def test_username_is_required_for_login(self):
     form = UserLoginForm({
         "username": "",
         "password":"String1"
         
     })
     self.assertFalse(form.is_valid())
     self.assertEqual(form.errors["username"], ["This field is required."])
     
     
    def test_registration_passwords_must_match(self):
     form = UserRegistrationForm({
         "username": "admin", 
         "email":"example@example.com",
         "password1":"String1",
         "password2":"String2"
         
     })
     self.assertFalse(form.is_valid())
     self.assertEqual(form.errors["password2"], ["Passwords must match"])
     
     
    def test_registration_email_must_be_unique(self):
        User.objects.create_user(
            username="admin",
            email="example@example.com")
            
        form = UserRegistrationForm({
            "username": "tester",
            "email": "example@example.com",
            "password1": "String1",
            "password2": "String1"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"], ["Email address must be unique"])