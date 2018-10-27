from django.shortcuts import render
from django.http import HttpResponse
def tempview(request):
    return render(request,'testapp/wish.html')

# Create your views here.
