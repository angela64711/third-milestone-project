import requests

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from .forms import SubmitMovieForm, ReviewForm, EditMovieForm
from .models import Movie, Review, Genre

# Create your views here.


def get_tmdb_poster_url(title, release_year=None):
    """
    Return a TMDB poster URL for a given movie title and release year.

    If no token, result, or poster path is found, return an empty string
    so the templates can fall back to the placeholder image.
    """
    if not settings.TMDB_API_TOKEN:
        return ""

    url = "https://api.themoviedb.org/3/search/movie"

    headers = {
        "Authorization": f"Bearer {settings.TMDB_API_TOKEN}",
    }

    params = {
        "query": title,
    }

    if release_year:
        params["primary_release_year"] = release_year

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException:
        return ""

    data = response.json()
    results = data.get("results", [])

    if not results:
        return ""

    poster_path = results[0].get("poster_path")

    if not poster_path:
        return ""

    return f"https://image.tmdb.org/t/p/w500{poster_path}"


# Home Page


def home(request):
    """
    Display the homepage with the latest approved movie recommendations.
    """
    latest_movies = Movie.objects.filter(
        approved=True,
    ).order_by(
        "-created_on"
    )[:4]

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

    model = Movie
    template_name = "movies/browse.html"
    paginate_by = 12

    def get_queryset(self):
        queryset = Movie.objects.filter(approved=True)

        genre = self.request.GET.get("genre")
        sort = self.request.GET.get("sort")

        if genre:
            queryset = queryset.filter(genres__name=genre)

        if sort == "az":
            queryset = queryset.order_by("title")
        else:
            queryset = queryset.order_by("-created_on")

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["genres"] = Genre.objects.all()
        context["selected_genre"] = self.request.GET.get("genre", "")
        context["selected_sort"] = self.request.GET.get("sort", "")
        return context


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
            poster_url = get_tmdb_poster_url(
                form.cleaned_data["title"],
                form.cleaned_data["release_year"],
            )

            movie = Movie.objects.create(
                title=form.cleaned_data["title"],
                poster_url=poster_url,
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
                "Thank you! Your movie recommendation has been "
                "submitted and is pending approval.",
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

    # Returns the user's existing review for this movie,
    # if they have not reviewed it yet.
    # filter() returns a QuerySet, so first() gives one review object or None.
    user_review = Review.objects.filter(
        movie=movie,
        author=request.user,
    ).first()

    reviews = Review.objects.filter(
        movie=movie,
        approved=True,
    ).order_by("-created_on")

    # Calculate average rating

    review_count = reviews.count()

    if review_count > 0:
        total_rating = 0

        for review in reviews:
            total_rating += review.rating

        average_rating = round(total_rating / review_count, 1)
    else:
        average_rating = None

    if request.method == "POST" and user_review is None:
        review_form = ReviewForm(request.POST)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.author = request.user
            review.approved = False
            review.is_submission_review = False
            review.save()

            messages.success(
                request,
                "Your review has been submitted and is pending approval.",
            )

            return redirect("movie_detail", slug=movie.slug)

    else:
        review_form = ReviewForm()

    context = {
        "movie": movie,
        "reviews": reviews,
        "review_form": review_form,
        "user_review": user_review,
        "average_rating": average_rating,
    }

    return render(request, "movies/movie_detail.html", context)


# My Activity Page


@login_required
def my_reviews(request):
    """
    Display activity for the logged-in user:
    movies they submitted and reviews they wrote.
    """

    my_movies = Movie.objects.filter(
        submitted_by=request.user,
    ).order_by("title")

    reviews = Review.objects.filter(
        author=request.user,
    ).order_by("movie__title")

    paginator = Paginator(reviews, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "my_movies": my_movies,
        "reviews": reviews,
        "page_obj": page_obj,
    }

    return render(request, "movies/my_reviews.html", context)


@login_required
def edit_movie(request, slug):
    """
    Allow users to edit movies they submitted.
    Edited movies require admin approval again.
    """

    movie = get_object_or_404(
        Movie,
        slug=slug,
        submitted_by=request.user,
    )

    if request.method == "POST":
        form = EditMovieForm(request.POST, movie=movie)

        if form.is_valid():
            old_title = movie.title
            old_release_year = movie.release_year

            movie.title = form.cleaned_data["title"]
            movie.director = form.cleaned_data["director"]
            movie.release_year = form.cleaned_data["release_year"]

            title_changed = movie.title != old_title
            year_changed = movie.release_year != old_release_year

            if title_changed or year_changed:
                movie.poster_url = get_tmdb_poster_url(
                    movie.title,
                    movie.release_year,
                )

            movie.approved = False
            movie.save()

            movie.genres.set(form.cleaned_data["genres"])

            success_message = (
                "Your movie update has been submitted and is pending approval."
            )

            messages.success(
                request,
                success_message,
            )

            return redirect("my_reviews")

    else:
        form = EditMovieForm(
            movie=movie,
            initial={
                "title": movie.title,
                "genres": movie.genres.all(),
                "director": movie.director,
                "release_year": movie.release_year,
            },
        )

    context = {
        "form": form,
        "movie": movie,
    }

    return render(request, "movies/edit_movie.html", context)


@login_required
def edit_review(request, review_id):
    """
    Allow users to edit their own reviews.
    Edited reviews require admin approval again.
    """
    review = get_object_or_404(
        Review,
        id=review_id,
        author=request.user,
    )

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            edited_review = form.save(commit=False)
            edited_review.approved = False
            edited_review.save()

            messages.success(
                request,
                "Your review has been updated and is pending approval.",
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
    Allow users to delete any review they authored.
    """
    review = get_object_or_404(
        Review,
        id=review_id,
        author=request.user,
        approved=True,
    )

    if request.method == "POST":
        review.delete()
        messages.success(request, "Your review has been deleted.")
        return redirect("my_reviews")

    context = {
        "review": review,
    }

    return render(request, "movies/delete_review.html", context)
