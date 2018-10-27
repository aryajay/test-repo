from django.shortcuts import render
from django.http import HttpResponse
def hydjobsinfo(request):
    s='<h1> hyd jobs information</h1>'
    return HttpResponse(s)
def chejobsinfo(request):
    s='<h1> chennai jobs information</h1>'
    return HttpResponse(s)

def punjobsinfo(request):
    s='<h1> pune jobs information</h1>'
    return HttpResponse(s)

def banjobsinfo(request):
    s='<h1> bangalore jobs information</h1>'
    return HttpResponse(s)


# Create your views here.
