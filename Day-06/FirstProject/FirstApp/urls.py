from django.urls import path
from FirstApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('ab/',views.about,name="abt"),
	path('reg/',views.register,name="rg"),
]