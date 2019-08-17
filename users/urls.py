from django.urls import include, path

from . import views

urlpatterns = [
    path('create-user/', views.CreateUser.as_view()),
]