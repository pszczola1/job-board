from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm

# Create your views here.

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "auth/login.html"

def logout_user(request):
    logout(request)
    return redirect("/")


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(email=user.email, password=user.password)
            login(request, user)
            return redirect("/")

    form = RegistrationForm()
    context = {"form": form}
    return render(request, "auth/register.html", context)