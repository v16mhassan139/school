from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home_page(request):
    # return HttpResponse ("home page views")
    return render(request ,'home.html')


def about_page(request):
    # return HttpResponse ("about page views")  
    return render(request ,'about.html')

def Sign_in(request):
    return render(request ,'sign_in.html' )
