from django.shortcuts import render
from.models import Issue
from django.http import HttpResponse

def issue_list(request):
    issues = Issue.objects.all().order_by('date')
    return render(request, 'issues/issue_list.html', {'issues':issues})

def issue_detail(request, slug):
    #return HttpResponse(slug)
    issue = Issue.objects.get(slug = slug)
    return render(request, 'issues/issue_detail.html', {'issue':issue})
