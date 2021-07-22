from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.RegisterUser.as_view()),
]