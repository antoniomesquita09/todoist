from django.urls import path

from todoitem import views

urlpatterns = [
    path("/list", views.TodoitemsView.as_view(), name="todoitem-list"),
    path("", views.TodoitemView.as_view(), name="todoitem"),
    path("/<id_arg>", views.TodoitemView.as_view(), name="todoitem"),
]
