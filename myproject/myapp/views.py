from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Добро пожаловать в QNexus Advanced!")

def network_monitor(request):
    return render(request, 'network_monitor.html')
