from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
posts = [
    {
        'user' : 'steve',
        'problem' : 'room door is not closing properly',
        'date':'march 10,2023'
    },
    {
        'user':'harris',
        'problem':'gysers not working',
        'date' : 'march 12, 2023'
    }

]

def admin(request):
    return render(request, 'complaint/admin_login.html')

def user(request):
    return render(request, 'complaint/user_login.html')

def form(request):
    return render(request, 'complaint/contact form.htm')

def userhm(request):
    return render(request, 'complaint/userhmpg.html')

def home(request): #for home page
    context = {
        'posts': posts
    }
    return render(request,'complaint/home.html',context)

def about(request): #for about page
    return render(request, 'complaint/about.html')
