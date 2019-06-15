from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm

# Create your tests here.
class TestAccountsForms(TestCase):
    
    def test_user_registration_form(self):
     form = UserRegistrationForm({
         'username': 'admin', 
         'email':'example@example.com',
         'password1':'String1',
         'password2':'String1'
         
     })
     self.assertTrue(form.is_valid())
     
     
    def test_user_login_form(self):
     form = UserLoginForm({
         'username': 'admin',
         'password':'String1'
         
     })
     self.assertTrue(form.is_valid())
     
     
    def test_password_is_required_for_login(self):
     form = UserLoginForm({
         'username': 'admin',
         'password':''
         
     })
     self.assertFalse(form.is_valid())
     self.assertEqual(form.errors['password'], ['This field is required.'])
    
    
    def test_username_is_required_for_login(self):
     form = UserLoginForm({
         'username': '',
         'password':'String1'
         
     })
     self.assertFalse(form.is_valid())
     self.assertEqual(form.errors['username'], ['This field is required.'])
     
     
    def test_registration_passwords_must_match(self):
     form = UserRegistrationForm({
         'username': 'admin', 
         'email':'example@example.com',
         'password1':'String1',
         'password2':'String2'
         
     })
     self.assertFalse(form.is_valid())
     self.assertEqual(form.errors['password2'], ['Passwords must match'])