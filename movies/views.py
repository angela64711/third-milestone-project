from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import SubmitMovieForm
from .models import Movie, Review

# Create your views here.

# Home Page


def home(request):
    """
    Display the homepage with the latest approved movie recommendations.
    """
    latest_movies = Movie.objects.filter(approved=True).order_by("-created_on")[:4]

    return render(
        request,
        "movies/index.html",
        {
            "latest_movies": latest_movies,
        },
    )


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


# Submit Movie Page


@login_required
def submit_movie(request):
    """
    Allow logged-in users to submit a new movie recommendation.

    The form creates two records:
    - one Movie
    - one linked Review
    """

    if request.method == "POST":
        form = SubmitMovieForm(request.POST)

        if form.is_valid():
            movie = Movie.objects.create(
                title=form.cleaned_data["title"],
                director=form.cleaned_data["director"],
                release_year=form.cleaned_data["release_year"],
                submitted_by=request.user,
                approved=False,
            )

            movie.genres.set(form.cleaned_data["genres"])

            Review.objects.create(
                movie=movie,
                author=request.user,
                rating=form.cleaned_data["rating"],
                review_text=form.cleaned_data["review_text"],
                approved=False,
                is_submission_review=True,
            )

            messages.success(
                request,
                "Thank you! Your movie recommendation has been submitted for review.",
            )

            return redirect("movie_list")

    else:
        form = SubmitMovieForm()

    return render(
        request,
        "movies/submit_movie.html",
        {
            "form": form,
        },
    )
