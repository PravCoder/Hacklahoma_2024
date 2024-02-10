from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("view_project/<str:pk>", views.view_project, name="view-project"),

]