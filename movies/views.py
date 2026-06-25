from django.shortcuts import render
from django.views import generic
from .models import Movie

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
