from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
	return HttpResponse("Welcome User!!!!")

def hlo(self):
	return HttpResponse("<h1>GOOD MORNING!!!</h1>")

def cy(request,b):
	return HttpResponse(f"Welcome User {b}")

def wd(request,s):
	return HttpResponse(f"<h3>Welcome User <span style='color:red'> {s}</span></h3>")

def student(request,a,b):
	return HttpResponse(f"<h1>student name:<span style='color:red'>{a}</span></h1><br><h1>student id:<span style='color:blue'>{b}</span></h1> ")

def hi(request,y,u):
	return HttpResponse("<style>span{color:red}i{background-color:magenta}</style><h2>welcome username: <span>"+y+"</span></h2><h5>Id: <i>"+u+"</i></h5>")

def dc(s):
	return HttpResponse("<script>alert('Hi welcome')</script>")

def sa(request,nb):
	return HttpResponse(f"<script>alert('Hi welcome User {nb}')</script>")

def dg(request):
	return render(request,'demo.html')

def emp(s,esal,ename,eid):
	return render(s,'employee.html',{'a':eid,'b':ename,'c':esal})






