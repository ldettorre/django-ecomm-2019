from django.shortcuts import render
# Create your views here.

def index(request):
    """ This will render an index/landing page """
    return render(request, "index.html")