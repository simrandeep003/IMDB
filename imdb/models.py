from django.db import models

# Create your models here.

class Genre(models.Model):
  name = models.CharField(max_length = 200)
  def __str__(self):
    return self.name

class Director(models.Model):
  name = models.CharField(max_length = 200)
  def __str__(self):
    return self.name

class Movie(models.Model):
  name = models.CharField(max_length = 200)
  popularity = models.FloatField()
  imdb_score = models.FloatField()
  director = models.ForeignKey(Director)
  genres = models.ManyToManyField(Genre)
  def __str__(self):
    return self.name