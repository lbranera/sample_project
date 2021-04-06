from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'sample_app/home.html')

def about(request):
    return render(request, 'sample_app/about.html')

def contact(request):
    return render(request, 'sample_app/contact.html')