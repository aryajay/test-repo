from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def studentInfo(request):
    student_list=Student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'testapp/studentinfo.html',context=my_dict)


# Create your views here.
