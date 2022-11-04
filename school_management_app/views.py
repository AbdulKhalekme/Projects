from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from school_management_app.EmailBackEnd import EmailBackEnd


# Create your views here.
#create a function in views.py for showing a demo page
def showDemoPage(request):
    return render(request,"demo.html")
def showLoginPage(request):
    return render(request,"Loginpage.html")
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponse("Email : "+request.POST.get("email")+"Password : "+request.POST.get("password"))
        else:
            return HttpResponse("Invalid Login")
def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")