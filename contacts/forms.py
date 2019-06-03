from django import forms
from .models import Contact


class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =('full_name','email','phone_number','details')