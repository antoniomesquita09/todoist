from django.urls import path

from todoitem import views

urlpatterns = [
    path("", views.TodoitemView.as_view(), name="todoitem"),
]
