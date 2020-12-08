from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext

from intern.models import UserInsert


def index(request):
    return render(request,'home.html')

def login(request):
    if request.method=='POST' and 'button' in request.POST:
        username = request.POST["first_name"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/index")
        else:
            messages.info(request,'Invalid credentials!')
            return redirect("/login")
    else:
        return render(request,'login_form.html')
    

def signup(request):
    return render(request,'user_signup.html')
def signin(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("Hello, You are in the Admin Dashboard.")
        else:
            messages.info(request,'Invalid credentials!')
            return redirect("/signin")
    else:
        return render(request,'login_form.html')
    
def insert(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST["last_name"]
        email=request.POST["email"]
        phone=request.POST["phone_number"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1==password2:
            if User.objects.filter(username=firstname).exists():
                messages.info(request,"This User Is Already Registered!!!")
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already Registered!!!")
            else:
                user = User.objects.create_user(username=firstname,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                messages.success(request,'User Registration Successful.')
                return render(request,'home.html')
        else:
            messages.info(request,"Password Doesn't match!!!")
            return redirect('/signup')
        return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect("/index")

def demo(request):
    if request.method=='POST':
        name=request.POST['fullname']
        email=request.POST['email']
        phone=request.POST['mobilenumber']
        msg=request.POST['message']
        