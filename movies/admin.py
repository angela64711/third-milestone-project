from django.contrib import admin
from django.utils.html import format_html

from .models import Genre, Movie, Review

# Register your models here.

# Customises admin list views to support content moderation.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "submitted_by",
        "release_year",
        "approved",
        "created_on",
    )
    list_filter = ("approved", "genres", "created_on")
    search_fields = ("title", "director", "submitted_by__username")
    filter_horizontal = ("genres",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("poster_preview",)

    def poster_preview(self, obj):
        if obj.poster_url:
            return format_html(
                '<img src="{}" style="max-height: 250px; width: auto;" />',
                obj.poster_url,
            )
        return "No poster available"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "movie",
        "author",
        "rating",
        "approved",
        "is_submission_review",
        "created_on",
    )
    list_filter = ("approved", "is_submission_review", "rating", "created_on")
    search_fields = ("movie__title", "author__username", "review_text")
