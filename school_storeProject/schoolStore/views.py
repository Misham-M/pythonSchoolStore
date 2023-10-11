from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Details
# Create your views here.

def index(request):
    return render(request,"index.html")
def details(request):
    if request.method == 'POST':
        name=request.POST.get('user')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        mail=request.POST.get('email')
        dep=request.POST.get('dep')
        course=request.POST.get('course')
        purpose=request.POST.get('purpose')
        pen=request.POST.get('pen')
        paper=request.POST.get('paper')
        print(name,dob,age,gender,phone,address,dep,course,purpose,pen,paper)
        detail=Details(name=name,dob=dob,age=age,gender=gender,phone=phone,address=address,mail=mail,dep=dep,course=course,purpose=purpose,pen=pen,paper=paper)
        detail.save()
        return redirect("confirmed")
    return render(request,'details.html')

def confirmed(request):
    return render(request,"confirm.html")