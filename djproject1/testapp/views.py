from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydview(request):
    jobs_list=Hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)


# Create your views here.
