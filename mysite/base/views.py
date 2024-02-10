from django.shortcuts import render

def home(request):
    context = {}
    return render(request, "base/home.html")

def register(request):
    pass

def login(request):
    pass