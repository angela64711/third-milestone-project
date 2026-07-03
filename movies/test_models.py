from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase
from .models import Genre, Movie, Review


class GenreModelTest(TestCase):
    def test_genre_string_method_returns_name(self):
        """
        Test that the Genre string method returns the genre name.
        """
        genre = Genre.objects.create(name="Drama")
        self.assertEqual(str(genre), "Drama")


class MovieModelTest(TestCase):
    def test_movie_string_method_returns_title(self):
        """
        Test that the Movie string method returns the movie title.
        """
        user = User.objects.create_user(username="testuser", password="testpass")
        movie = Movie.objects.create(
            title="Inception",
            submitted_by=user,
        )

        self.assertEqual(str(movie), "Inception")

    def test_movie_slug_created_on_save(self):
        """
        Test that a slug is automatically created from the movie title.
        """
        user = User.objects.create_user(username="testuser2", password="testpass")
        movie = Movie.objects.create(
            title="The Grand Budapest Hotel",
            submitted_by=user,
        )

        self.assertEqual(movie.slug, "the-grand-budapest-hotel")


class ReviewModelTest(TestCase):
    def test_review_string_method_returns_movie_and_author(self):
        """
        Test that the Review string method returns movie and author.
        """
        user = User.objects.create_user(username="testuser3", password="testpass")
        movie = Movie.objects.create(
            title="Arrival",
            submitted_by=user,
        )
        review = Review.objects.create(
            author=user,
            movie=movie,
            rating=5,
            review_text="This is a thoughtful and excellent science fiction film.",
        )

        self.assertEqual(str(review), "Arrival | review by testuser3")

    def test_user_cannot_review_same_movie_twice(self):
        """
        Test that one user cannot create two reviews for the same movie.
        """
        user = User.objects.create_user(username="testuser4", password="testpass")
        movie = Movie.objects.create(
            title="Get Out",
            submitted_by=user,
        )

        Review.objects.create(
            author=user,
            movie=movie,
            rating=5,
            review_text="This is a smart and memorable thriller with great tension.",
        )

        with self.assertRaises(IntegrityError):
            Review.objects.create(
                author=user,
                movie=movie,
                rating=4,
                review_text="This is a second review and should not be allowed.",
            )
