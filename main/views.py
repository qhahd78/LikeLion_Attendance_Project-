from django.shortcuts import render
from .models import Student
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@login_required(login_url='login')
def home(request) : 
    students= Student.objects
    return render (request, 'main.html', {'students': students})

def name_list(request):
    N_list = Student.objects.all()
    context = {
        "names": names,
        "name_js": json.dumps([name_li.json() for name_li in names])
    }
    return render(request, "main.html", context)
