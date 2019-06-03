from django.shortcuts import render, get_object_or_404
from .forms import ContactSubmissionForm
from .models import Contact

# Create your views here.


    
def contact_submission(request):
    contact = Contact
    if request.method =="POST":
        form =  ContactSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            contact= form.save()
        return render(request, 'index.html')
    else:
        form = ContactSubmissionForm()
    return render(request, 'contactpage.html', {'form':form})