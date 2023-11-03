from django.urls import path

from . import views

urlpatterns = [
    path('/list', views.list, name="list"),
    path("/form", views.create),
    path("/edit/<int:id>", views.edit),
    path("/delete/<int:id>", views.delete)
]