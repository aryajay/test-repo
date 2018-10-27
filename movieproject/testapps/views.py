from django.shortcuts import render
from testapps.forms import MovieForm
from testapps.models import Movie

# Create your views here.
def index_view(request):
    return render(request,'testapps/index.html')

def add_movie_view(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_view(request)
    return render(request,'testapps/addmovie.html',{'form':form})

def list_movie_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapps/listmovie.html',{'movies_list':movies_list})
from django.shortcuts import render

# Create your views here.
