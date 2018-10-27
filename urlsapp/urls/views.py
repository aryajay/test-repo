from django.shortcuts import render
from django.http import HttpResponse

def hydjobsinfo(resuest):
    s='<h1> hyderabad jobs inormation </h1>'
    return HttpResponse(s)


# Create your views here.
