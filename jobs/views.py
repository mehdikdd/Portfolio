from django.shortcuts import render, HttpResponse
from .models import Job
# import requests


# Create your views here.
def home(request):
    client_ip = request.META.get('HTTP_X_REAL_IP')
    if client_ip == "5.113.51.249" :
        return HttpResponse('<h1>Your Not allowed to reach out'
                            ' this website, apologize! Your Country is fucked up!!   ' + client_ip + '</h1>')
    else:
        jobs = Job.objects
        return render(request, 'jobs/home.html', {'jobs':jobs})