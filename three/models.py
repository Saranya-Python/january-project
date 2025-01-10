from django.db import models

# Create your models here.


class Category(models.Model):
    cname=models.CharField(max_length=100)
    cimg=models.ImageField(upload_to='category')

    def __str__(self):
        return self.cname
    

#image kodukkn aadhym media setup cheyyanm
#image setup cheyyan mainproject le settings il STATIC_URL il media root kodukkanm
#MEDIA_URL=''
#MEDIA_ROOT=BASE_DIR/'media'   aadhym idh set cheyyanm ennit model il img feiled kodukknm
#appol terminal il error varum appol pip install pillow koduthaal pillow install aavum


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    description=models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    pimg=models.ImageField(upload_to='product')


    def __str__(self):
        return self.name

