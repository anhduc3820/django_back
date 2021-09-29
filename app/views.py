from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .auth import AuthBackEnd


def loginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = AuthBackEnd.authenticate(
            request, username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            user_type = user.user_type
            # return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')

            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')

            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')


def get_user_details(request):
    if request.user:
        return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
