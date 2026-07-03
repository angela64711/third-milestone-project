from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("movies/", views.MovieList.as_view(), name="movie_list"),
    path("submit/", views.submit_movie, name="submit_movie"),
    path("my-reviews/", views.my_reviews, name="my_reviews"),
    path("reviews/<int:review_id>/edit/", views.edit_review, name="edit_review"),
    path("reviews/<int:review_id>/delete/", views.delete_review, name="delete_review"),
    path("movies/<slug:slug>/", views.movie_detail, name="movie_detail"),
    path("movies/<slug:slug>/edit/", views.edit_movie, name="edit_movie"),
]
