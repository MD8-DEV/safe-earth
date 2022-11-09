from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *

TEMPLATE_DIR = "user_auth/"

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            print("done")
            return redirect("dash")
        return render(request, TEMPLATE_DIR + "login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dash')
        else:
            return HttpResponse("User doesn't exist")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("dash")
        return render(request, TEMPLATE_DIR + "sign_up.html")
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = User.objects.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
            )
        login(request, user)
        return redirect("dash")

class Dashboard(View):
    def get(self, request):
        return render(request, TEMPLATE_DIR + "dashboard.html")