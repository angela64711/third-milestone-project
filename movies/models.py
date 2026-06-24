from django.db import models

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
