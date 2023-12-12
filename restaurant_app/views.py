from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages


# Login view
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sales_report')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')


def create_account(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        email = request.POST.get('Email')
        user = authenticate(request, username=username, password=password, email=email)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'create_account.html', {'error_message': 'Invalid credentials'})
    return render(request, 'create_account.html')

def forget_password(request):
    if request.method=="POST":
        email = request.POST.get('Email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user:
            messages.success("password reset link sent to your email")
            return redirect('success')
        else:
            messages.error(request, 'User with this email does not exist.')
    return render(request, 'forget_password.html')

def logout(request):
    logout(request)
    return redirect('login')