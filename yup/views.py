from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def homepage(request):
#     return HttpResponse('this is home page')


def mypage(request):
    return render(request,'base.html')

def homepage(request):
    return render(request,'home.html')


def profilepage(request):
    return render(request,'profile.html')

def aboutpage(request):
    return render(request,'about.html')