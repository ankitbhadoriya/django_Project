from django.shortcuts import render
from django.http import  HttpResponse
from .models import Post

def home(request):
    # return HttpResponse('<h1> Welcome to Blog Home </h1>')
    context={"posts":Post.objects.all()}
    return render(request,'blog/home.html' , context)



def about(request):
    return render (request , "blog/about.html" , context={"title":"About Page"})

