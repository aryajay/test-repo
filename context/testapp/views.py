from django.shortcuts import render
import datetime
def dateinfo(request):
    date=datetime.datetime.now()
    my_dict={'msg':date}
    return render(request,'testapp/wish.html',context=my_dict)

# Create your views here.
