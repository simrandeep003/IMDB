from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Movie
# Create your views here.

def index(request):
  movie_list = Movie.objects.all()
  paginator = Paginator(movie_list, 10)
  page = request.GET.get('page')
  try:
    movies = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    movies = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    movies = paginator.page(paginator.num_pages)
  return render(request, 'imdb/index.html', {'movies' : movies})

def movie_detail(request, movie_id):
  movie = Movie.objects.get(pk=movie_id)
  return render(request, 'imdb/movies/detail.html', {'movie' : movie})

def search(request):
  if request.method == "GET":
    search_term = request.GET['search']
  else:
    search_term = request.POST['search']

  movie_list = Movie.objects.filter(name__icontains=search_term)
  director_list = Movie.objects.filter(director__name__icontains=search_term)
  genre_list = Movie.objects.filter(genres__name__icontains=search_term)
  final_list = movie_list | director_list | genre_list
  final_list = final_list.distinct();

  paginator = Paginator(final_list,10)
  page = request.GET.get('page')
  try:
    movies = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    movies = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    movies = paginator.page(paginator.num_pages)
  return render(request, 'imdb/movies/search.html', {'movies' : movies, 'search_term' : search_term})