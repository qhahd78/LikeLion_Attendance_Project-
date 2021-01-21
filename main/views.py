from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request) : 
    students= Student.objects
    return render (request, 'main.html', {'students': students})