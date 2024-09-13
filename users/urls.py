from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.logout_user, name="logout"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("register/", views.register, name="register")
]