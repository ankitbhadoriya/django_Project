from django.shortcuts import render
from django.http import  HttpResponse


posts=[{
        "title":"My 1st Post",
        "author":"animX",
        "date_posted":"24th Feb 2019",
        "content":"its a good day to be alive" },
        {
        "title":"My 2nd Post",
        "author":"animX",
        "date_posted":"24th Feb 2019",
        "content":"its a good day to be alive" },
        {
        "title":"My 3rd Post",
        "author":"animX",
        "date_posted":"24th Feb 2019",
        "content":"its a good day to be alive" }]

def home(request):
    # return HttpResponse('<h1> Welcome to Blog Home </h1>')
    context={"posts":posts}
    return render(request,'blog/home.html' , context)



def about(request):
    return render (request , "blog/about.html" , context={"title":"About Page"})

