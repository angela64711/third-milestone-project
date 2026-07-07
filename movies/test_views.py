from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Genre, Movie, Review


class PublicPageViewsTest(TestCase):
    def test_home_page_returns_200(self):
        """
        Test that the homepage loads successfully.
        """
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_browse_movies_page_returns_200(self):
        """
        Test that the browse movies page loads successfully.
        """
        response = self.client.get(reverse("movie_list"))

        self.assertEqual(response.status_code, 200)


class AuthenticationRequiredViewsTest(TestCase):
    def test_submit_movie_redirects_when_logged_out(self):
        response = self.client.get(reverse("submit_movie"))
        self.assertEqual(response.status_code, 302)

    def test_my_activity_redirects_when_logged_out(self):
        response = self.client.get(reverse("my_reviews"))
        self.assertEqual(response.status_code, 302)


class MovieDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

    def test_approved_movie_detail_returns_200_for_logged_in_user(self):
        """
        Test that a logged-in user can view an approved movie detail page.
        """
        movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            approved=True,
        )

        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("movie_detail", args=[movie.slug]))

        self.assertEqual(response.status_code, 200)

    def test_unapproved_movie_detail_returns_404_for_logged_in_user(self):
        """
        Test that an unapproved movie detail page cannot be accessed.
        """
        movie = Movie.objects.create(
            title="Pending Movie",
            release_year=2024,
            approved=False,
        )

        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("movie_detail", args=[movie.slug]))

        self.assertEqual(response.status_code, 404)


class SubmitMovieViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.genre = Genre.objects.create(name="Drama")

    def test_submit_movie_page_returns_200_for_logged_in_user(self):
        """
        Test that a logged-in user can access the submit movie page.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("submit_movie"))

        self.assertEqual(response.status_code, 200)

    def test_submit_movie_post_creates_movie_and_review(self):
        """
        Test that a valid movie submission creates one movie and one review.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(
            reverse("submit_movie"),
            {
                "title": "Past Lives",
                "genres": [self.genre.id],
                "director": "Celine Song",
                "release_year": 2023,
                "rating": 5,
                "review_text": "This is a thoughtful and beautiful movie.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Review.objects.count(), 1)


class MyActivityViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            submitted_by=self.user,
            approved=True,
        )

        self.review = Review.objects.create(
            movie=self.movie,
            author=self.user,
            rating=5,
            review_text="This is a thoughtful movie review.",
            approved=True,
        )

    def test_my_activity_page_returns_200_for_logged_in_user(self):
        """
        Test that a logged-in user can access their activity page.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("my_reviews"))

        self.assertEqual(response.status_code, 200)

    def test_my_activity_page_contains_user_movie_and_review(self):
        """
        Test that My Activity contains the logged-in user's movie and review.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(reverse("my_reviews"))

        self.assertContains(response, "Past Lives")
        self.assertContains(response, "This is a thoughtful movie review.")


class EditReviewViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            approved=True,
        )

        self.review = Review.objects.create(
            movie=self.movie,
            author=self.user,
            rating=5,
            review_text="This is the original approved review text.",
            approved=True,
        )

    def test_edit_review_page_returns_200_for_review_author(self):
        """
        Test that a user can access the edit page for their own review.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(
            reverse(
                "edit_review",
                args=[self.review.id],
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_edit_review_post_updates_review_and_sets_unapproved(self):
        """
        Test that editing a review updates it and sets approved to False.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(
            reverse("edit_review", args=[self.review.id]),
            {
                "rating": 4,
                "review_text": "This is the updated review after editing.",
            },
        )

        self.review.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(
            self.review.review_text,
            "This is the updated review after editing.",
        )
        self.assertFalse(self.review.approved)


class DeleteReviewViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            approved=True,
        )

        self.review = Review.objects.create(
            movie=self.movie,
            author=self.user,
            rating=5,
            review_text="This is an approved review that can be deleted.",
            approved=True,
        )

    def test_delete_review_page_returns_200_for_review_author(self):
        """
        Test that a user can access the delete page for their own review.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(
            reverse(
                "delete_review",
                args=[self.review.id],
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_delete_review_post_deletes_review(self):
        """
        Test that a user can delete their own approved review.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(
            reverse(
                "delete_review",
                args=[self.review.id],
            )
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 0)


class EditMovieViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.genre = Genre.objects.create(name="Drama")

        self.movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            director="Celine Song",
            submitted_by=self.user,
            approved=True,
        )

        self.movie.genres.set([self.genre])

    def test_edit_movie_page_returns_200_for_submitter(self):
        """
        Test that a user can access the edit page for a movie they submitted.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(
            reverse(
                "edit_movie",
                args=[self.movie.slug],
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_edit_movie_post_updates_movie_and_sets_unapproved(self):
        """
        Test that editing a movie updates it and sets approved to False.
        """
        self.client.login(username="testuser", password="testpass123")

        response = self.client.post(
            reverse("edit_movie", args=[self.movie.slug]),
            {
                "title": "Past Lives Updated",
                "genres": [self.genre.id],
                "director": "Celine Song",
                "release_year": 2023,
            },
        )

        self.movie.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.movie.title, "Past Lives Updated")
        self.assertFalse(self.movie.approved)


class OwnershipProtectionViewTest(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="owner",
            password="testpass123",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123",
        )

        self.movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            submitted_by=self.owner,
            approved=True,
        )

        self.review = Review.objects.create(
            movie=self.movie,
            author=self.owner,
            rating=5,
            review_text="This is an approved review written by another user.",
            approved=True,
        )

    def test_user_cannot_edit_another_users_movie(self):
        """
        Test that users cannot access the edit page
        for movies they did not submit.
        """
        self.client.login(username="otheruser", password="testpass123")

        response = self.client.get(
            reverse(
                "edit_movie",
                args=[self.movie.slug],
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_edit_another_users_review(self):
        """
        Test that users cannot access the edit page
        for reviews they did not write.
        """
        self.client.login(username="otheruser", password="testpass123")

        response = self.client.get(
            reverse(
                "edit_review",
                args=[self.review.id],
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_another_users_review(self):
        """
        Test that users cannot access the delete page
        for reviews they did not write.
        """
        self.client.login(username="otheruser", password="testpass123")

        response = self.client.get(
            reverse("delete_review", args=[self.review.id]),
        )

        self.assertEqual(response.status_code, 404)


class MovieDetailReviewSubmissionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )

        self.movie = Movie.objects.create(
            title="Past Lives",
            release_year=2023,
            approved=True,
        )

    def test_user_can_submit_review_on_movie_detail(self):
        """
        Test that a logged-in user can submit a review for a movie.
        """
        self.client.login(
            username="testuser",
            password="testpass123",
        )

        response = self.client.post(
            reverse("movie_detail", args=[self.movie.slug]),
            {
                "rating": 5,
                "review_text": (
                    "This is a thoughtful review submitted through "
                    "the movie detail page."
                ),
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Review.objects.count(), 1)

        review = Review.objects.first()

        self.assertEqual(review.author, self.user)
        self.assertEqual(review.movie, self.movie)
        self.assertFalse(review.approved)
