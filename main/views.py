from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request) : 
    students= Student.objects
    return render (request, 'main.html', {'students': students})