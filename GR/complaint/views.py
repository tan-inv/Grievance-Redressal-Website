from django.shortcuts import render
from django.http import HttpResponse
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

def home(request): #for home page
    context = {
        'posts':posts
    }
    return render(request,'complaint/home.html',context)

def about(request): #for about page
    return render(request, 'complaint/about.html')
