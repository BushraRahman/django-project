from django.urls import path

from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('add_movie', views.create, name="create"),
    path('edit_movie/<int:id>/', views.edit, name="edit"),
    path('delete_movie', views.delete, name="delete"),
]