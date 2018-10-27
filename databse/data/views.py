from django.shortcuts import render
from django.http import HtpResponse
from data.models import Employee
def empview(request):
    emp_list=Employee.objects.all()
    return HttpResponse('<h1> sample data </h1>')
print(emp_list)
# Create your views here.
