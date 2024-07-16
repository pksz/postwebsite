from django.contrib import admin
from django.urls import path
from . import views
#code

urlpatterns = [
    path('',views.Home.as_view(),name='blog-home' ),
    path('about/',views.About.as_view(),name='blog-about' ),
    
]