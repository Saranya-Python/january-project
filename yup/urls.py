from django.urls import path
from .views import *

urlpatterns=[
  path('mypage',mypage),
  path ('home',homepage,name='myhomepage'),
  path('profile',profilepage,name='profile'),
  path('about',aboutpage,name='about'),
]