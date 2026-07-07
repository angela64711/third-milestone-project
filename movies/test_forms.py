from django.test import TestCase

from .forms import SubmitMovieForm, ReviewForm, EditMovieForm
from .models import Genre, Movie


class SubmitMovieFormTest(TestCase):
    def test_submit_movie_form_is_valid(self):
        """
        Test that the submit movie form is valid with correct data.
        """
        genre = Genre.objects.create(name="Drama")

        form = SubmitMovieForm(
            data={
                "title": "Past Lives",
                "genres": [genre.id],
                "director": "Celine Song",
                "release_year": 2023,
                "rating": 5,
                "review_text": (
                    "This is a beautiful and thoughtful movie recommendation."
                ),
            }
        )

        self.assertTrue(form.is_valid())

    def test_submit_movie_form_rejects_duplicate_title_case_insensitive(self):
        """
        Test that duplicate movie titles are rejected regardless of case.
        """
        genre = Genre.objects.create(name="Thriller")

        Movie.objects.create(
            title="The Departed",
            submitted_by=None,
        )

        form = SubmitMovieForm(
            data={
                "title": "the departed",
                "genres": [genre.id],
                "director": "Martin Scorsese",
                "release_year": 2006,
                "rating": 5,
                "review_text": (
                    "This is a strong crime thriller with great performances."
                ),
            }
        )

        self.assertFalse(form.is_valid())

    def test_submit_movie_form_rejects_more_than_three_genres(self):
        """
        Test that users cannot choose more than 3 genres.
        """
        genre_1 = Genre.objects.create(name="Drama")
        genre_2 = Genre.objects.create(name="Comedy")
        genre_3 = Genre.objects.create(name="Romance")
        genre_4 = Genre.objects.create(name="Action")

        form = SubmitMovieForm(
            data={
                "title": "Everything Everywhere All at Once",
                "genres": [
                    genre_1.id,
                    genre_2.id,
                    genre_3.id,
                    genre_4.id,
                ],
                "director": "Daniel Kwan and Daniel Scheinert",
                "release_year": 2022,
                "rating": 5,
                "review_text": (
                    "This is a creative and emotional movie recommendation."
                ),
            }
        )

        self.assertFalse(form.is_valid())


class EditMovieFormTest(TestCase):
    def test_edit_movie_form_is_valid(self):
        """
        Test that the edit movie form is valid with correct data.
        """
        genre = Genre.objects.create(name="Drama")
        movie = Movie.objects.create(title="Past Lives", submitted_by=None)

        form = EditMovieForm(
            data={
                "title": "Past Lives",
                "genres": [genre.id],
                "director": "Celine Song",
                "release_year": 2023,
            },
            movie=movie,
        )

        self.assertTrue(form.is_valid())

    def test_edit_movie_form_allows_same_movie_title(self):
        """
        Test that keeping the same title on the same movie is allowed.
        """
        genre = Genre.objects.create(name="Drama")
        movie = Movie.objects.create(title="Past Lives", submitted_by=None)

        form = EditMovieForm(
            data={
                "title": "Past Lives",
                "genres": [genre.id],
                "director": "Celine Song",
                "release_year": 2023,
            },
            movie=movie,
        )

        self.assertTrue(form.is_valid())

    def test_edit_movie_form_rejects_duplicate_title_from_another_movie(self):
        """
        Test that a movie cannot be edited to use another movie's title.
        """
        genre = Genre.objects.create(name="Thriller")
        movie = Movie.objects.create(title="Past Lives", submitted_by=None)
        Movie.objects.create(title="The Departed", submitted_by=None)

        form = EditMovieForm(
            data={
                "title": "The Departed",
                "genres": [genre.id],
                "director": "Martin Scorsese",
                "release_year": 2006,
            },
            movie=movie,
        )

        self.assertFalse(form.is_valid())

    def test_edit_movie_form_rejects_more_than_three_genres(self):
        """
        Test that users cannot choose more than 3 genres when editing.
        """
        genre_1 = Genre.objects.create(name="Drama")
        genre_2 = Genre.objects.create(name="Comedy")
        genre_3 = Genre.objects.create(name="Romance")
        genre_4 = Genre.objects.create(name="Action")
        movie = Movie.objects.create(title="Past Lives", submitted_by=None)

        form = EditMovieForm(
            data={
                "title": "Past Lives",
                "genres": [
                    genre_1.id,
                    genre_2.id,
                    genre_3.id,
                    genre_4.id,
                ],
                "director": "Celine Song",
                "release_year": 2023,
            },
            movie=movie,
        )

        self.assertFalse(form.is_valid())


class ReviewFormTest(TestCase):
    def test_review_form_rejects_short_review_text(self):
        """
        Test that review text must be at least 20 characters.
        """
        form = ReviewForm(
            data={
                "rating": 5,
                "review_text": "Too short",
            }
        )

        self.assertFalse(form.is_valid())

    def test_review_form_is_valid(self):
        """
        Test that the review form is valid with correct data.
        """
        form = ReviewForm(
            data={
                "rating": 5,
                "review_text": "This is a thoughtful and useful movie review.",
            }
        )

        self.assertTrue(form.is_valid())

    def test_review_form_requires_rating(self):
        """
        Test that the review form is invalid without a rating.
        """
        form = ReviewForm(
            data={
                "rating": "",
                "review_text": "This is a thoughtful and useful movie review.",
            }
        )

        self.assertFalse(form.is_valid())
