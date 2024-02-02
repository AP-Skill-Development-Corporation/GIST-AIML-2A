from django.shortcuts import render
from .forms import StForm

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def contact(request):
	return render(request,'html/ct.html')

def student(request):
	d = StForm()
	return render(request,'html/stdnt.html',{'t':d})
