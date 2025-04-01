from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('signin/',views.Signin, name='signin' ),
        path('login/',views.Login, name='login' ),
        path('pass_foget/',views.Password_Reset,name='pass_reset'),
        path('dashboard/',views.DashBoard, name = 'user-interface'),
        path('profile-details/', views.Profile_Details, name ="profile_details"),
        path('address/', views.Addres, name ="adres"),
          path('my_order/', views.My_order, name ="order"),

        path('logout/',views.Logout, name='logout'),

    

]
