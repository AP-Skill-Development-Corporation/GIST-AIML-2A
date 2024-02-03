from django.urls import path
from BSApp import views

urlpatterns = [
	path('hme/',views.home,name="hm"),
	path('abt/',views.about,name="ab"), 
	path('ct/',views.contact,name="cnt"),
	path('',views.student,name="std"),
	path('stup/<int:a>/',views.stupdate,name="stupd"),
	path('stdt/<int:k>/',views.stdlte,name="stdd"),
]