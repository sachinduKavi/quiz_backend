from django.urls import path
from . import views
from .controller import Controller


urlpatterns = [
    path('register/', Controller.userRegistration)
]
