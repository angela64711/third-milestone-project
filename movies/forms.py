from django import forms
from .models import Genre, Movie


class SubmitMovieForm(forms.Form):
    """
    Form for submitting a new movie recommendation.

    This form collects data for two models:
    - Movie
    - Review
    """

    title = forms.CharField(
        max_length=200,
        required=True,
        label="Movie title",
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        required=True,
        widget=forms.CheckboxSelectMultiple,
        label="Genres",
        help_text="Choose between 1 and 3 genres.",
    )

    director = forms.CharField(
        max_length=200,
        required=False,
        label="Director",
    )

    release_year = forms.IntegerField(
        required=False,
        label="Release year",
        min_value=1900,
        max_value=2035,
    )

    rating = forms.ChoiceField(
        choices=[
            ("", "Choose a rating "),
            (5, "Excellent"),
            (4, "Great"),
            (3, "Good"),
            (2, "Okay"),
            (1, "Not for me"),
        ],
        required=True,
        label="Your rating",
    )

    review_text = forms.CharField(
        required=True,
        label="Why would you recommend this movie?",
        min_length=20,
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "placeholder": "Tell the community why this movie is worth watching...",
            }
        ),
    )

    def clean_title(self):
        """
        Check that the submitted movie title does not already exist.
        """

        title = self.cleaned_data.get("title")

        if Movie.objects.filter(title__iexact=title).exists():
            raise forms.ValidationError("This movie has already been submitted.")

        return title

    def clean_genres(self):
        """
        Ensure users choose between 1 and 3 genres.
        """

        genres = self.cleaned_data.get("genres")

        if genres and genres.count() > 3:
            raise forms.ValidationError("Please choose no more than 3 genres.")

        return genres
