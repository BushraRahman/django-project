from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('form/', views.create, name="create"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<int:id>/', views.delete, name="delete")
]