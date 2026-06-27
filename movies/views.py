from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Movie, Review

# Create your views here.

# Home Page


def home(request):
    return render(request, "movies/home.html")


# Browse Movies Page (Class view)


class MovieList(generic.ListView):
    """
    Returns all submitted, approved movies in: model.Movie
    and displays them in a page of eight posts.
    **Context**

    ``queryset``
        All published instances of :model:`movie.Movie`
    ``paginate_by``
        Number of posts per page.

    **Template:**

    :template:`movies/browse.html`
    """

    queryset = Movie.objects.filter(approved=True)
    template_name = "movies/browse.html"
    paginate_by = 8


# Movie Details Page


def movie_detail(request, slug):
    """
    Display an individual approved movie and its approved reviews.
    """
    movie = get_object_or_404(Movie, slug=slug, approved=True)

    reviews = Review.objects.filter(movie=movie, approved=True).order_by("-created_on")

    return render(
        request,
        "movies/movie_detail.html",
        {
            "movie": movie,
            "reviews": reviews,
        },
    )
