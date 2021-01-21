from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['teacherid']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '비밀번호가 틀렸어요'})
    else:
        return render(request, 'login.html')


def logout(request):
        auth.logout(request)
        return redirect('login')

@login_required
def mypage(request):
    return render(request, 'mypage.html')
