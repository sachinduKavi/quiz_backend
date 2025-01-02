from django.urls import path
from . import views
from .controllers.testing import testing

urlpatterns = [
    path("login/", views.UserListCreate.as_view(), name="login"),
    path("testing/", testing, name="testing")
]

