from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "pagination_app/index.html")

def add(request):
    return render(request, "pagination_app/add.html")
