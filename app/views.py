from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .auth import AuthBackEnd
import logging

_logger = logging.getLogger(__name__)


def loginPage(request):
    _logger.info("start redirect login page !")
    return render(request, 'login.html')


def doLogin(request):
    if request.method != "POST":
        _logger.info("start redirect login page !")
        return redirect('login')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = AuthBackEnd.authenticate(
            request, username=email,
            password=password
        )
        if user:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')


def get_user_details(request):
    if request.user:
        return HttpResponse("User: " + request.user.email + " User Name: " + request.user.username)
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
