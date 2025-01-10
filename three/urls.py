from django.urls import path
from .views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('allcategory',allcategory),
    path('plist/<int:value>',prolist,name='productlist'),
    # path('prodet/<int:pid>',prodetails,name='productdetails'),
    path('prodet/<int:pk>',ProductDetails.as_view(),name='productdetails'),
    path('adddata',myinfo),
    path('success',success,name='success'),
    path('stuform',students),
    # path('addpro',addpro),
    path('addpro',AddMyProduct.as_view()),
    # path('allpro',allproducts),
    path('allpro',AllProducts.as_view(),name='prolist'),
    # path('proedit/<int:pid>',editprofile,name='editproduct'),
    path('proedit/<int:pk>',EditProduct.as_view(),name='editproduct'),
    # path('del/<int:pid>',productdelete,name='delpro'),
    path('del/<int:pk>',DeleteProduct.as_view(),name='delpro'),
    path('visit',visitedpro),
    # path('mypage',mypage),
    path('mypage',GoToMyPage.as_view()),
  
    
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)