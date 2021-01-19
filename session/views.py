from django.shortcuts import render

# Create your views here.

def createsession (request) :
    return render(request, 'createSession.html')

def sessionlist (request) :
    return render(request, 'sessionList.html')
