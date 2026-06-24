from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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

    Related to :model:`auth.User` through submitted_by.
    Related to :model:`movies.Genre` through genres.
    """

    title = models.CharField(max_length=200, unique=True)
    submitted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="submitted_movies"
    )
    genres = models.ManyToManyField(Genre, related_name="movies")
    recommendation_text = models.TextField()
    poster = CloudinaryField("image", default="placeholder")
    director = models.CharField(max_length=200, blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | submitted by {self.submitted_by}"
