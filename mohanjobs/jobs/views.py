from django.shortcuts import render
from django.http import HttpResponse
def hydjobs(request):
    s='<h1>hyd jobs information</h1>'
    return HttpResponse(s)
def chejobs(request):
    s='<h1>chennai jobs information</h1>'
    return HttpResponse(s)
def banjobs(request):
    s='<h1>bangalore jobs information</h1>'
    return HttpResponse(s)
def punjobs(request):
    s='<h1>pune jobs information</h1>'
    return HttpResponse(s)


# Create your views here.
