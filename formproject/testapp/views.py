from django.shortcuts import render
from . import forms
def StudentRegister_view(request):
    form=forms.StudentRegister()
    return render(request,'testapp/register.html',{'form':form})

# Create your views here.
