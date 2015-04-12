from django.conf.urls import url

from . import views

#url patterns for navigating to different pages
urlpatterns = [
  url(r'^$', views.index, name = 'index'), #route to url /imdb/
  url(r'^movies/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'), #route to url /imdb/movies/1,2,..etc
  url(r'^search/$', views.search, name='search'), #route to url /imdb/search
]