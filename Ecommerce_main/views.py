from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def Index(request):
 return render(request, 'index.html')
def Shop(request):
    return render(request, 'shop.html')
def Product_Single(request): 
    
    return render(request, 'product-single.html')
def Shope_Sider(request):
    return render(request, 'shop-sidebar.html')
def Cart(request):
    return render(request, 'cart.html')
def Checkout(request):
    return render(request, 'checkout.html')
def Pricing(request):
    return render(request, 'pricing.html')
def Confirm(request):
    return render(request, 'confirmation.html')

     
     