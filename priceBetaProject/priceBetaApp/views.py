from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# from priceBetaApp.forms import SignUpForm


def index(request):
     return render(request,'index.html')
