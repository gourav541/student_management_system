from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.

def showDemoPage(request):
    return render(request, 'demo.html')

def ShowLoginPage(request):
    return render(request,'login_page.html')

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        return HttpResponse(" Email: "+request.POST.get("email")+" Password "+request.POST.get("password"))
