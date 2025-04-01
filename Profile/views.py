from django.shortcuts import render,redirect, HttpResponseRedirect,get_object_or_404
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView


from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import PasswordResetForm


import os
# Create your views here.
def Signin(request):
    
    if request.method == "POST":
       First_name = request.POST.get('fname')
       Last_name = request.POST.get('lname')
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       confrim_pass = request.POST.get('cpassword')
       if User.objects.filter(username = username):
         messages.error(request, "Username Already taken, Please choose other one ")
         redirect('signin')
       elif User.objects.filter(email =email):
         messages.error(request, "Email Already taken, please choose other one ")
         redirect('signin')
       elif password != confrim_pass:
        messages.error(request, "Password is not match")
       else:
        User.objects.create_user(
           first_name =First_name,
           last_name = Last_name,
           email=email,
           username= username,
           password=password
           
       )
        authenticate(request, username=username, password = password)
        messages.success(request,"Account Created ")
        return render(request, 'signin.html')

    return render(request, 'signin.html')
def Login(request):
    
   if request.user.is_authenticated:
        return redirect('home')

   if request.method == 'POST':
        username = request.POST.get('username')
       
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')
            return render(request, 'login.html')

    
    
   
   return render(request, 'login.html')
  
def Password_Reset(request):
    return render(request, 'forget-password.html') 


def Logout(request):
     if request.user.is_authenticated:
         logout(request)
         return redirect('home')
     else:  
          return redirect('login') 
def DashBoard(request):
     if request.user.is_authenticated:
        username = request.user.username
        profiles = User.objects.filter(username = username)
        if profiles.exists():
         user = profiles.first()
        return render(request, 'dashboard.html',{'profiles':user})   
      
     
     
     return render(request, 'dashboard.html')   

def Profile_Details(request):
    if request.user.is_authenticated:
     username = request.user.username
     profiles = User.objects.filter(username = username)
     
     if profiles.exists():
      user = profiles.first()
     
      return render(request, 'profile-details.html',{'profiles':user})  
    return render(request, 'profile-details.html')       
def  Addres(request):
    return render(request, 'address.html')
def My_order(request):
    return render(request, 'order.html')
