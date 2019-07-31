from django.http import HttpResponse
from django.shortcuts import render

def home_page(request): 
    home_title = "Hello Baby..."
    return render(request, "hello_world.html", {"title": home_title})

def about_page(request):
    about_title = "About me" 
    return render(request, "hello_world.html", {"title": about_title})

def contact_page(request): 
    contact_title = "Contact Us"
    return render(request, "hello_world.html", {"title": contact_title})