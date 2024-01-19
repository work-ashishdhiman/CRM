from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout


def home(request):
  return render(request, "home.html")


# Create your views here.
