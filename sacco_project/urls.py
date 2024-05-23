"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from SaccoApp import views

urlpatterns = [

    # Other URL patterns may be present

    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
from django.urls import path
from . import views

urlpatterns = [
    path('SaccoApp/', views.sacco_transaction_view, name='sacco_transaction_view'),
]
]

    # Add more URL patterns as needed






