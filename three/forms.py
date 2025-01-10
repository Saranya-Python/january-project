from django import forms
from .models import Product



class StudentForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()


# widget - django representation of html inputs

class ProductForm(forms.ModelForm):         #idh outer class aanu
     name=forms.CharField(widget=forms.TextInput(
          attrs={'class':'name-input','placeholder':'please enter your name'}
     ))


     class Meta:                            #idh inner class aanu
          model=Product
        #   fields='__all__'
          fields= ['name','pimg','category']