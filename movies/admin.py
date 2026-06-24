from django.contrib import admin
from .models import Genre
from .models import Movie
from .models import Review

# Register your models here.

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Review)
