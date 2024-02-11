from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("first-name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        p1 = request.POST.get("password1")
        p2 = request.POST.get("password2")

        if first_name != None and last_name != None  and email != None and p1 != None and p2 != None and p1==p2 and username != None:
            user = User.objects.create(first_name=first_name,last_name=first_name,email=email,password=p1, username=username)
            user.save()
            login(request, user)
            return redirect("home")
        else:
            print("An error has occured during registration")

    context = {"page":"register"}
    return render(request, "base/login_register.html", context)

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            print("User no exist with that email")

        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            print(user)
            print("Wrong Info")
    context = {"page":"login"}
    return render(request, "base/login_register.html", context)

def home(request):
    context = {}
    return render(request, "base/home.html", context)

def view_project(request, pk):
    context = {}
    return render(request, "base/view_project.html", context)

def create_large_project(request):
    context = {}
    return render(request, "base/create_large_project.html" , context)

def create_small_project(request):
    context = {}
    return render(request, "base/create_small_project.html", context)