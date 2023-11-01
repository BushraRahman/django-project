from django.urls import path

from . import views

urlpatterns = [
    path("form", views.create, name="index"),
    path("list",views.list, name="listView")
]