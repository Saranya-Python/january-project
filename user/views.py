from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from yup.views import homepage

from django.contrib import messages
from . forms import *

from . models import Profile

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def loginpage(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    # print(username,password)
    user=authenticate(request,username=username,password=password)
    # print(user)
    if user:
        login(request,user)
        messages.success(request,'user has been logged in')
        return redirect(homepage)
    

    return render(request,'login.html')



def logoutpage(request):
    logout(request)
    messages.success(request,'user has been logged out')
    return redirect(homepage)


def adduser(request):
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            a=form.save()
            uemail=a.email
            name=a.username
            subject='Welcome to our website'
            message=f'Thank you for registering with us {name}'
            from_email=settings.EMAIL_HOST_USER
            to_list=[uemail]
            send_mail(subject,message,from_email,to_list)
            Profile.objects.create(user=a)
            return redirect(loginpage)
            

            # messages.success(request,'user has been created')
            # return redirect(homepage)
    else:

         form=RegisterUser()
    return render(request,'register.html',{'form':form})



def profilepage(request):
    a=Profile.objects.get(user=request.user)

    return render(request,'profile.html',{'a':a})




def allcountz(request):
    c= request.session.get('count',0)
    c+=1
    request.session['count']=c
    return render(request,'count.html',{'c':c})