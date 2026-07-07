from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
)

# from cloudinary.models import CloudinaryField

# Create your models here.


class Genre(models.Model):
    """
    Stores a movie genre that can be assigned to movies.
    """

    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Movie(models.Model):
    """
    Stores a movie recommendation submitted by a registered user.

    Related to: model:`auth.User` through submitted_by.
    Related to: model:`movies.Genre` through genres.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    submitted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="submitted_movies",
    )
    genres = models.ManyToManyField(Genre, related_name="movies")
    poster_url = models.URLField(max_length=500, blank=True)
    director = models.CharField(max_length=200, blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    Stores a review and rating submitted by a registered user for a movie.

    Related to: model:`auth.User` through author.
    Related to: model:`movies.Movie` through movie.
    """

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="movie_reviews"  # noqa
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="reviews"  # noqa
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review_text = models.TextField(
        validators=[MinLengthValidator(20), MaxLengthValidator(1000)]
    )
    approved = models.BooleanField(default=False)
    is_submission_review = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
        constraints = [
            models.UniqueConstraint(
                fields=["author", "movie"], name="unique_author_movie_review"
            )
        ]

    def __str__(self):
        return f"{self.movie} | review by {self.author}"
