from django.shortcuts import render,redirect
from .forms import RegForm

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def register(request):
	if request.method == "POST":
		g = RegForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/')
	g = RegForm()
	return render(request,'html/reg.html',{'j':g})