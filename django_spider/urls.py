"""django_spider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('welcome/', views.welcome),
    path('login/', views.login),
    path('register/', views.register),

    path('spider/', views.spider),
    path('userManagement/', views.user_management),
    path('userManagement/addUser/', views.addUser),
    path('userManagement/deleteUser/', views.deleteUser),
    path('spider/pie_sex', views.pie_sex),
    path('spider/funnel_level', views.funnel_level),
    path('spider/bar_followers', views.bar_followers),
    path('spider/pie_vip', views.pie_vip),
]

