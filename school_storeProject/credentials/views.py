from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        uname=request.POST['user']
        password=request.POST['password']
        # print(uname,password)
        user=auth.authenticate(username=uname,password=password)
        # print(user)
        if user is not None:
            auth.login(request,user)
            print("success")
            return redirect('details')
        else:
            messages.info(request,"error in login")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        uname=request.POST['user']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        print(uname)
        if password == cpassword :
            if User.objects.filter(username=uname).exists():
                messages.info(request,"USER EXIST")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,"Password mismatch")


    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')