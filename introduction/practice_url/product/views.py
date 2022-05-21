from django.shortcuts import render

# Create your views here.
def product(req):
    return render(req,'product.html')
def productfirst(req):
    return render(req,'productfirst.html')