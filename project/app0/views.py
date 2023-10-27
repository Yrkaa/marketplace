from django.shortcuts import render
from django.urls import path

from app0.models import Product
from project import urls

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user(request):
    req = request.POST.get("request")
    data = Product.objects.all()
    products = list()
    if req != None:
        for i in data:
            if req.lower() in i.name.lower():
                products.append(i)
                

    #if req == None or req == '' or req == ' ':
        #products = Product.objects.all()
    #else:
        #products = Product.objects.filter(name = req.title())

    return render(request, 'user.html', context={'products':products})

def seller(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        new_product = Product(name=name, price=price)
        new_product.save()
        urls.urlpatterns.append(path(new_product.id, product_page, kwargs={'name': new_product.name, 'price': new_product.price}, name=None))
    return render(request, 'seller.html')

def product_page(request,name, price):
    return render(request, 'product_page.html', context={'name': name, 'price': price})