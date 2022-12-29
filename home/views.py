from django.shortcuts import render

# Create your views here.

def landing(request):
    """ A view to return the landing page """
    
    return render(request, 'home/landing.html')

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index2.html')

def about(request):
    """ A view to return the index page """
    
    return render(request, 'home/about.html')
