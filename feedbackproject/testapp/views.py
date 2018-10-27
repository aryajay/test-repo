from django.shortcuts import render
from . import forms

def feedbackview(request):
    form=forms.FeedBackForm()
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and printing information')
            print('Name:',form.cleaned_data['name'])
            print('Password:',form.cleaned_data['password'])
            print('Roll No:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('FeedBack:',form.cleaned_data['feedback'])
    return render(request,'testapp/feedback.html',{'form':form})


# Create your views here.
