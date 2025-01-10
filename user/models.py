from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True,null=True)
    pro_pic=models.ImageField(upload_to='profile',null=True)


    def __str__(self):
        self.user.username

