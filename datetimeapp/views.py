from django.shortcuts import render
from django.http import HttpResponse
import datetime
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.shifttime("%H"))
    msg='<h1> hello all are very'
    if h<12:
        msg=msg+'good morning'
    elif h<16:
        msg=msg+'good afternoon'
    elif h<21:
        msg=msg+'good evening'
    else:
        msg=msg+'good night'
    msg=msg+'</h1><hr>'
    msg=msg+'</h1> now server time is:'+str(date)+'</h1>'

# Create your views here.
