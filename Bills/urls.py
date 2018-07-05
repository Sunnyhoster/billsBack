"""Bills URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from BillsApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('login/', views.login),
    url('register/', views.register),
    url('bill/list/', views.getBills),
    url('bill_list/new_bill/', views.addBills),
    url('bill_list/update_bill/', views.updateBills),
    url('bill_list/delete_bill/', views.deleteBills),
    url('image/', views.sendImage),
    url('prediction/', views.consumePrediction),
    url('test/',views.testM) #测试models
]
