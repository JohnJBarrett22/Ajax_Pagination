from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "pagination_app/index.html")

def add(request):
    return render(request, "pagination_app/add.html")

def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'])
    return redirect(request, "pagination_app/index.html")
