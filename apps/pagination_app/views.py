from django.shortcuts import render, redirect, HttpResponse
from . models import *

def index(request):
    users = User.objects.all()
    return render(request, "pagination_app/index.html", {"users": users})

def add(request):
    return render(request, "pagination_app/add.html")

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'])
    return redirect('/')

def find(request):
    users = User.objects.filter(first_name__startswith=request.POST['lead_name'])|User.objects.filter(last_name__startswith=request.POST['lead_name'])
    print(users)
    return render(request, "pagination_app/table.html", {"users": users})

def date(request):
    if len(request.POST['from_date']) < 1:
        from_date = '1900-01-01'
    else:
        from_date = request.POST['from_date']

    if len(request.POST['to_date']) < 1:
        to_date = '9999-12-31'
    else:
        to_date = request.POST['to_date']

    users = User.objects.filter(created_at__range=[from_date, to_date])
    print(users)
    return render(request, "pagination_app/table.html", {"users": users})