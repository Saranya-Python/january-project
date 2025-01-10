from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse
from .forms import StudentForm,ProductForm
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

def mypage(request):
    return render(request,'mypage.html',{'name':'saranya'})

class GoToMyPage(TemplateView):
    template_name='mypage.html'
    def get_context_data(self, **kwargs):
        return {'name':'saranyats'}






def allcategory(request):
    category=Category.objects.all()
    return render(request,'allcat.html',{'category':category})

def prolist(request,value):
    # print(value)
    p=Product.objects.filter(category=value)
    return render(request,'prolist.html',{'p':p})

def prodetails(request,pid):
    pro=Product.objects.get(id=pid)
    visited_product=request.session.get('visit',[])
    visited_product.append(pro.name)
    request.session['visit']=visited_product
    return render(request,'prodet.html',{'pro':pro})


class ProductDetails(DetailView):
    model=Product
    template_name='prodet.html'
    context_object_name='pro'





def visitedpro(request):
    visit=request.session.get('visit',[])
    p = Product.objects.filter(name__in=visit)
    return render(request,'visit.html',{'p':p})




# def myinfo(request):
#     nam=request.GET.get('name')
#     add=request.GET.get('address')
#     return render(request,'info.html')

def myinfo(request):
    nam=request.POST.get('name')
    add=request.POST.get('address')
    return render(request,'info.html')

def success(request):
    return HttpResponse('form submitted')

def students(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return redirect(success)
    else:
        form=StudentForm()
    return render(request,'student.html',{'form':form})



def addpro(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(success)
    else:

        form=ProductForm()
    return render(request,'addpro.html',{'form':form})



class AddMyProduct(CreateView):
    model=Product
    fields= ['name','pimg','category']
    template_name='addpro.html'
    success_url=reverse_lazy('success')

class AddMyProduct(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'addpro.html',{'form':form})
    def post(self,request):
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(success)





def allproducts(request):
    pro=Product.objects.all()
    return render(request,'products.html',{'pro':pro})


class AllProducts(ListView):
    model=Product
    template_name='products.html'
    context_object_name='pro'




def editprofile(request,pid):
    pro=Product.objects.get(id=pid)
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect(allproducts)
    else:
        form=ProductForm(instance=pro)
    return render(request,'editpro.html',{'form':form})


class EditProduct(UpdateView):
    model=Product
    fields= ['name','pimg','category']
    template_name='editpro.html'
    success_url=reverse_lazy('success')






def productdelete(request,pid):
    pro=Product.objects.get(id=pid)
    if request.method=='POST':
        pro.delete()
        return redirect(allproducts)
    return render(request,'delete.html',{'pro':pro})



class DeleteProduct(DeleteView):
    model=Product
    template_name='delete.html'
    context_object_name='pro'
    success_url=reverse_lazy('prolist')


# data - create cheyyam
#        update cheyyam
#        read cheyyam
#        delete cheyyam
#   CRUD