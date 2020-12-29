from django.shortcuts import render
from .models import CustomUser

from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from users.forms import CustomUserCreationFormView
from django.core.cache import cache
# Create your views here.


def index(request):

    return render(request, 'home.html')


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        ct = cache.get('count', version=user.pk)

        return render(request, "users/dashboard.html", {'ct': ct})
    else:

        return render(request, "users/dashboard.html")


def errorpage(request):
    return render(request, "users/error.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationFormView}
        )
    elif request.method == "POST":
        form = CustomUserCreationFormView(request.POST)
        if form.is_valid():
            CustomUser = form.save()
            login(request, CustomUser)
            return redirect(reverse('users:login'))
        else:

            return redirect(reverse('users:errorpage'))

    return render(request, 'users/register.html')
