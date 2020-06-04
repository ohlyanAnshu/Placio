from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
     path('post-your-requirement/', views.postYourRequirement, name="postyourrequirement"),
     path('franchise/', views.franchise_request, name="franchise"),
     path('why-us/', views.whyus, name="whyus"),
     path('pay-rent', views.payrent, name="payrent"),
     path('about-us/', views.aboutus, name="aboutus"),
     path('amity/', views.aboutus, name="amity")
]