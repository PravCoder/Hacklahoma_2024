from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view-project/<str:pk>", views.view_project, name="view-project"),
    path("create-large-project/", views.create_large_project, name="create-large-project"),
    path("create-small-project/", views.create_small_project, name="create-small-project"),




    path("login/", views.login_page, name="login-page"),
    path("register/", views.register, name="register"),

]