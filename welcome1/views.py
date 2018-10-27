from django.shortcuts import render
from django.http import HttpResponse
def hello(request):
    s='<h1> welcome to thedjango project practice</h1>'
    return HttpResponse(s)


# Create your views here.