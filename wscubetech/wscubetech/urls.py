"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wscubetech import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name = 'homePage'),
    path('newsdetails/<slug>', views.newsDetails),
    # path('about/', views.about, name='about'),
    path('about-us/', views.about, name='about'),
    path('service/', views.service, name="service"),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('userform/', views.userForm, name='userform'),
    path('calculator', views.calculator, name='calculator'),
    path('saveevenodd', views.saveevenodd), 
    path('marksheet', views.marksheet),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('submitform/', views.submitform, name='submitform'),
    path('elements/', views.elements, name='elements'),
    path('generic/', views.generic, name='generic'),
]