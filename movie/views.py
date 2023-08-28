from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.
def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    #return HttpResponse('<h1>Welcome to home page</h1>')
    movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm, 'movies':movies})

def about(request):
    #return HttpResponse('<h1>Welcome to home page</h1>')
    return render(request, 'about.html')