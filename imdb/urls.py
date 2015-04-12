from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^movies/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
  url(r'^search/$', views.search, name='search'),
]