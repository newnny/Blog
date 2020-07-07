from django.shortcuts import render
from.models import Portfolio
from django.http import HttpResponse

def port_list(request):
    portfolio = Portfolio.objects.all().order_by('date')
    return render(request, 'portfolio/port_list.html', {'portfolio':portfolio})

def port_detail(request, slug):
    #return HttpResponse(slug)
    port = Portfolio.objects.get(slug = slug)
    return render(request, 'portfolio/port_detail.html', {'port':port})
