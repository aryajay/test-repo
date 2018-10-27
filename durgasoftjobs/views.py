from django.shortcuts import render
from django.http  import HttpResponse
def hydjobs(request):
    s='<h1> hyd jobs information</h1>'
    return HttpResponse(s)
def chennaijobs(request):
    y='<h1> chennai jobs information</h1>'
    return HttpResponse(y)
def bangalorejobs(request):
    b='<h1> bangalore jobs information</h1>'
    return HttpResponse(b)
def punejobs(request):
    p='<h1> pune jobs information</h1>'
    return HttpResponse(p)

# Create your views here.
