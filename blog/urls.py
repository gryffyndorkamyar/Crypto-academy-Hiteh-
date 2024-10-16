"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from post import views
from post import forms
from post.views import index
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('mag', views.mag, name='mag'),
    path('signup', views.signup , name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('ticket', views.ticket , name='ticket'),
    path('cart', views.cart, name='cart'),
    path('cryptoprice/', views.cryptoprice, name='crypto_price'),
    path('editprofile/', views.EditProfile , name='edit_profile'),
    path('editpassword/', views.EditPassword , name='edit_password'),
    path('approve_users/', views.approve_users, name='approve_users'),
    path('Profile' , views.Profile , name='Profile'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
