from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import SubmitMovieForm, ReviewForm
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


# Movie Detail Page


@login_required
def movie_detail(request, slug):
    """
    Display one approved movie and handle normal review submission.
    """

    # Only approved movies can be accessed, even if someone guesses the URL.
    movie = get_object_or_404(Movie, slug=slug, approved=True)

    # Returns the user's existing review for this movie, if they have not reviewed it yet.
    # filter() returns a QuerySet, so first() gives one review object or None.
    user_review = Review.objects.filter(movie=movie, author=request.user).first()

    reviews = Review.objects.filter(movie=movie, approved=True).order_by("-created_on")

    if request.method == "POST" and user_review is None:
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.author = request.user
            review.approved = False
            review.is_submission_review = False
            review.save()

            return redirect("movie_detail", slug=movie.slug)

    else:
        review_form = ReviewForm()

    context = {
        "movie": movie,
        "reviews": reviews,
        "review_form": review_form,
        "user_review": user_review,
    }

    return render(request, "movies/movie_detail.html", context)


# My Reviews Page


@login_required
def my_reviews(request):
    """
    Display all reviews written by the logged-in user.
    Each review is shown together with its related movie.
    """

    # Show only reviews that are approved and linked to approved movies.
    # Both filters are needed so unapproved content is not visible.
    reviews = Review.objects.filter(
        author=request.user,
        approved=True,
        movie__approved=True,
    ).order_by("-created_on")

    context = {
        "reviews": reviews,
    }

    return render(request, "movies/my_reviews.html", context)


@login_required
def edit_review(request, review_id):
    """
    Allow users to edit their own approved reviews.
    Edited reviews require admin approval again.
    """
    review = get_object_or_404(
        Review, id=review_id, author=request.user, approved=True, movie__approved=True
    )

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            edited_review = form.save(commit=False)
            edited_review.approved = False
            edited_review.save()

            messages.success(
                request,
                "Your review has been updated and is waiting for approval.",
            )

            return redirect("my_reviews")

    else:
        form = ReviewForm(instance=review)

    context = {
        "form": form,
        "review": review,
    }

    return render(request, "movies/edit_review.html", context)


# Delete Review Page


@login_required
def delete_review(request, review_id):
    """
    Allow users to delete their own normal reviews.
    Original submission reviews cannot be deleted.
    """
    review = get_object_or_404(
        Review,
        id=review_id,
        author=request.user,
        approved=True,
        movie__approved=True,
        is_submission_review=False,
    )

    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect("my_reviews")

    context = {
        "review": review,
    }

    return render(request, "movies/delete_review.html", context)
