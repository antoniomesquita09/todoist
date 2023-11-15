from django.urls import path

from todoitem import views

urlpatterns = [
    path("/new", views.create, name="create"),
    path("/list", views.find_all, name="find_all"),
    path("/update/<id_arg>", views.update, name="update"),
    path("/delete/<id_arg>", views.delete, name="delete"),
    path("/<id_arg>", views.find_by_id, name="single"),
]
