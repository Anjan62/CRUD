from django.shortcuts import render, redirect
from .forms import productform
from .models import product



# Create your views here.


def product_list(request):
    context = {'product_list':product.objects.all()}
    return render(request,"product/product_list.html",context) 


def product_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = productform()
        else:
            products = product.objects.get(pk=id)
            form = productform(instance=products)
        return render(request,"product/product_form.html",{'form':form})
    else:
        if id==0:
            form = productform(request.POST)
        else:
            products = product.objects.get(pk=id)
            form = productform(request.POST,instance= products)
        if form.is_valid():
            form.save()
        return redirect('/product/list')


def product_delete(request, id):
    products = product.objects.get(pk=id)
    products.delete()
    return redirect('/product/list')

