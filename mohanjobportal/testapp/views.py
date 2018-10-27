from django.shortcuts import render
from testapp.models import *
def index(request):
    return render(request,'testapp/index.html')
def Hydview(request):
    jobs_list=Hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',contex=my_dict)

# Create your views here.
