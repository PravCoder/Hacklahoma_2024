from django.shortcuts import render

def register(request):
    pass

def login(request):
    pass

def home(request):
    context = {}
    return render(request, "base/home.html")

def view_project(request, pk):
    print(pk)
    context = {}
    return render(request, "base/view_project.html")
