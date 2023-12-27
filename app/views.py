from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
  
def index(request): 
    return render(request, 'index.html')

def ganga_haridwar(request):
    return render(request, 'ganga_haridwar.html')

def saryu_ayodhya(request):
    return render(request, 'saryu_ayodhya.html')

def ganga_varanasi(request):
    return render(request, 'ganga_varanasi.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def updates(request):
    return render(request, 'polution_check.html')

def rivers(request):
    return render(request, 'rivers.html')