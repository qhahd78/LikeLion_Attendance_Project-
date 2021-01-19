from django.shortcuts import render, redirect
from .models import Session_form


# Create your views here.

def createsession (request) :
    
    if request.method == 'POST': 
        session_form = Session_form()
        session_form.session_date = request.POST.get('session_date')
        session_form.title = request.POST.get('title')
        session_form.save()

        return redirect('sessionlist')
        

    return render(request, 'createsession.html')

def sessionlist (request) :
    Sessions = Session_form.objects 

    return render(request, 'sessionList.html', {'sessions': Sessions } )
