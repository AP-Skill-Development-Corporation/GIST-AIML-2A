"""AIMLProject URL Configuration

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
from django.urls import path,include
from AIMLApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('t/',views.demo),
    path('h/',views.hlo),
    path('y/<str:b>/',views.cy),
    path('a/<str:s>/',views.wd),
    path('abc/<str:a>/<str:b>/',views.student),
    path('e/<str:y>/<str:u>/',views.hi),
    path('z/',views.dc),
    path('p/<str:nb>/',views.sa),
    path('w/',views.dg),
    path('km/<str:eid>/<str:ename>/<int:esal>/',views.emp),
    path('ab/',views.htform),
    path('',include('BSApp.urls')),
]

