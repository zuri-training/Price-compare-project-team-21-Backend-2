from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


# from priceBetaApp.forms import SignUpForm


def index(request):
     return HttpResponse(request,'templates/index.html')
