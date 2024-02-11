from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout
import datetime as dt



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
    for p in request.user.projects.all():
        print(p.name)
    context = {}
    return render(request, "base/home.html", context)

def view_project(request, pk):
    context = {}
    return render(request, "base/view_project.html", context)

def view_dashboard(request):
    user = request.user
    context = {"projects":user.projects.all()}
    return render(request, "base/dashboard.html", context)

def view_small_projects(request, pk):
    user = request.user
    large_project = LargeProject.objects.get(id=int(pk))
    print(large_project.name)

def create_large_project(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("projectName")
        description = request.POST.get("projectDescription")
        due_date = request.POST.get("dueDate")
        Lproject = LargeProject.objects.create(name=name, description=description, date_created=str(dt.datetime.now()), due_date=due_date)
        user.projects.add(Lproject)
        Lproject.save()
        user.save()

        context = {"projects":user.projects.all()}
        return render(request, "base/dashboard.html", context)

    
    context = {}
    return render(request, "base/create_large_project.html" , context)

def create_small_project(request):
    context = {}
    return render(request, "base/create_small_project.html", context)