from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.MovieList.as_view(), name="movie_list"),
    path("submit/", views.submit_movie, name="submit_movie"),
    path("my-reviews/", views.my_reviews, name="my_reviews"),
    path("movies/<slug:slug>/", views.movie_detail, name="movie_detail"),
]
