from django.http import HttpResponse
from django.shortcuts import render

# allow us to send response to users when they request

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')
