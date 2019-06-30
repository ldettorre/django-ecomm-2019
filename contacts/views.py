from django.shortcuts import render, redirect
from .forms import ContactSubmissionForm
from .models import Contact

# Create your views here.


    
def contact_submission(request):
    if request.method =="POST":
        form =  ContactSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = ContactSubmissionForm()
    return render(request, 'contactpage.html', {'form':form})
    
def faq_page(request):
    """ This will render the frequently asked questions page """
    return render(request, "faq.html")
    
def about_page(request):
    """ This will render the frequently asked questions page """
    return render(request, "about.html")