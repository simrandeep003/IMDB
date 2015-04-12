from django.contrib import admin

# Register your models here.

from .models import Movie, Director, Genre

#Registering classes in Admin view
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genre)