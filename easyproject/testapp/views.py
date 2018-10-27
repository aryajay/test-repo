from django.shortcuts import render
def hello(request):
    return render(request,'testapp/hello.html')

# Create your views here.
