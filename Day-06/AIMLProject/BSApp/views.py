from django.shortcuts import render,redirect
from .forms import StForm
from .models import Student
from django.contrib import messages
 
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/abt.html')

def contact(request):
	return render(request,'html/ct.html')

def student(request):
	y = Student.objects.all()
	if request.method == "POST":
		d = StForm(request.POST)
		if d.is_valid():
			d.save()
			messages.success(request,"Student Created Successfully!!!!")
			return redirect('/')
	d = StForm()
	return render(request,'html/stdnt.html',{'t':d,'p':y})

def stupdate(request,a):
	h = Student.objects.get(id=a)
	if request.method == "POST":
		w = StForm(request.POST,instance=h)
		if w.is_valid():
			w.save()
			messages.warning(request,"Student Data Updated successfully")
			return redirect('/')	
	w = StForm(instance=h)
	return render(request,'html/stdupdate.html',{'n':w})

def stdlte(request,k):
	n = Student.objects.get(id=k)
	if request.method == "POST":
		n.delete()
		messages.info(request,"Student Record Deleted Successfully")
		return redirect('/')
	return render(request,'html/stundlte.html',{'e':n})


