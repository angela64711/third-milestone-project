# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


## Code Validation


### HTML


I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| movies | [browse.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/browse.html) | (https://validator.w3.org/nu/?doc=https://superangela-2348acaf62bb.herokuapp.com/movies/&out=html) | ![screenshot](documentation/validation/html-movies-browse.png) | Passed by URI validation. |
| movies | [delete_review.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/delete_review.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-movies-delete_review.png) | Passed by input validation from rendered page source. |
| movies | [edit_movie.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/edit_movie.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-movies-edit_movie.png) | Passed by input validation from rendered page source. |
| movies | [edit_review.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/edit_review.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-movies-edit_review.png) | Passed by input validation from rendered page source. |
| movies | [index.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/index.html) | (https://validator.w3.org/nu/?doc=https://superangela-2348acaf62bb.herokuapp.com/accounts/login/&out=html) | ![screenshot](documentation/validation/html-movies-index.png) | Passed by URI validation. |
| movies | [movie_detail.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/movie_detail.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-movies-movie_detail.png) | Passed by input validation from rendered page source. |
| movies | [my_reviews.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/my_reviews.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-movies-my_reviews.png) | Passed by input validation from rendered page source. |
| movies | [submit_movie.html](https://github.com/angela64711/third-milestone-project/blob/main/movies/templates/movies/submit_movie.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-movies-submit_movie.png) | Passed by input validation from rendered page source. |
| templates | [404.html](https://github.com/angela64711/third-milestone-project/blob/main/templates/404.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-templates-404.png) | Passed by input validation from rendered page source. |
| templates | [login.html](https://github.com/angela64711/third-milestone-project/blob/main/templates/account/login.html) | https://validator.w3.org/nu/?doc=https://superangela-2348acaf62bb.herokuapp.com/accounts/login/&out=html | ![screenshot](documentation/validation/html-templates-login.png) | Passed by URI validation. |
| templates | [logout.html](https://github.com/angela64711/third-milestone-project/blob/main/templates/account/logout.html) | N/A - validated by input from rendered source. | ![screenshot](documentation/validation/html-templates-logout.png) | Passed by input validation from rendered page source. |
| templates | [signup.html](https://github.com/angela64711/third-milestone-project/blob/main/templates/account/signup.html) | https://validator.w3.org/nu/?doc=https://superangela-2348acaf62bb.herokuapp.com/accounts/signup/&out=html | ![screenshot](documentation/validation/html-templates-signup.png) | Passed by URI validation. |

**HTML Validation Notes**

During HTML validation, a local browser/security extension injected an additional fontawsome script into the page source, which caused validation issues unrelated to the project code. To ensure the submitted code was validated accurately, the injected script was removed from the copied validation input and replaced with the original project script tag before re-running validation. The corrected validation then passed successfully.



### CSS


I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [style.css](https://github.com/angela64711/third-milestone-project/blob/main/static/css/style.css) | (https://jigsaw.w3.org/css-validator/validator?uri=https://superangela-2348acaf62bb.herokuapp.com/static/css/style.css&output=html#warnings) | ![screenshot](documentation/validation/css-static-style.png) | No CSS errors found. Validator warnings relate to CSS variables used for Google Font declarations and do not affect functionality. |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [manage.py](https://github.com/angela64711/third-milestone-project/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | Pass |
| movie_project | [settings.py](https://github.com/angela64711/third-milestone-project/blob/main/movie_project/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movie_project/settings.py) | ![screenshot](documentation/validation/py-movie_project-settings.png) | Pass - Django default long lines handled with # noqa |
| movie_project | [urls.py](https://github.com/angela64711/third-milestone-project/blob/main/movie_project/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movie_project/urls.py) | ![screenshot](documentation/validation/py-movie_project-urls.png) | Pass |
| movies | [admin.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/admin.py) | ![screenshot](documentation/validation/py-movies-admin.png) | Pass |
| movies | [forms.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/forms.py) | ![screenshot](documentation/validation/py-movies-forms.png) | Pass - long validation messages and placeholders reformatted |
| movies | [models.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/models.py) | ![screenshot](documentation/validation/py-movies-models.png) | Pass - limited # noqa used for long Django model fields |
| movies | [test_forms.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/test_forms.py) | ![screenshot](documentation/validation/py-movies-test_forms.png) | Pass - long test strings reformatted |
| movies | [test_models.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/test_models.py) | ![screenshot](documentation/validation/py-movies-test_models.png) | Pass |
| movies | [test_views.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/test_views.py) | ![screenshot](documentation/validation/py-movies-test_views.png) | Pass - long test client calls reformatted |
| movies | [urls.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/urls.py) | ![screenshot](documentation/validation/py-movies-urls.png) | Pass |
| movies | [views.py](https://github.com/angela64711/third-milestone-project/blob/main/movies/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/angela64711/third-milestone-project/main/movies/views.py) | ![screenshot](documentation/validation/py-movies-views.png) | Pass - long messages and conditions reformatted |


## Responsiveness


I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Browse Movies | ![screenshot](documentation/responsiveness/mobile-browse.png) | ![screenshot](documentation/responsiveness/tablet-browse.png) | ![screenshot](documentation/responsiveness/desktop-browse.png) | Works as expected |
| Movie Detail | ![screenshot](documentation/responsiveness/mobile-detail.png) | ![screenshot](documentation/responsiveness/tablet-detail.png) | ![screenshot](documentation/responsiveness/desktop-detail.png) | Works as expected |
| Submit Movie | ![screenshot](documentation/responsiveness/mobile-submit.png) | ![screenshot](documentation/responsiveness/tablet-submit.png) | ![screenshot](documentation/responsiveness/desktop-submit.png) | Works as expected |
| Edit Movie | ![screenshot](documentation/responsiveness/mobile-edit-movie.png) | ![screenshot](documentation/responsiveness/tablet-edit-movie.png) | ![screenshot](documentation/responsiveness/desktop-edit-movie.png) | Works as expected |
| My Activity | ![screenshot](documentation/responsiveness/mobile-my-activity.png) | ![screenshot](documentation/responsiveness/tablet-my-activity.png) | ![screenshot](documentation/responsiveness/desktop-my-activity.png) | Works as expected |
| Edit Review | ![screenshot](documentation/responsiveness/mobile-edit-review.png) | ![screenshot](documentation/responsiveness/tablet-edit-review.png) | ![screenshot](documentation/responsiveness/desktop-edit-review.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Logout | ![screenshot](documentation/responsiveness/mobile-logout.png) | ![screenshot](documentation/responsiveness/tablet-logout.png) | ![screenshot](documentation/responsiveness/desktop-logout.png) | Works as expected |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |



## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Edge | Notes |
| --- | --- | --- | --- | --- |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/edge-home.png) | Works as expected |
| Browse Movies | ![screenshot](documentation/browsers/chrome-browse.png) | ![screenshot](documentation/browsers/firefox-browse.png) | ![screenshot](documentation/browsers/edge-browse.png) | Works as expected |
| Movie Detail | ![screenshot](documentation/browsers/chrome-detail.png) | ![screenshot](documentation/browsers/firefox-detail.png) | ![screenshot](documentation/browsers/edge-detail.png) | Works as expected |
| Submit Movie | ![screenshot](documentation/browsers/chrome-submit.png) | ![screenshot](documentation/browsers/firefox-submit.png) | ![screenshot](documentation/browsers/edge-submit.png) | Works as expected |
| Edit Movie | ![screenshot](documentation/browsers/chrome-edit-movie.png) | ![screenshot](documentation/browsers/firefox-edit-movie.png) | ![screenshot](documentation/browsers/edge-edit-movie.png) | Works as expected |
| My Activity | ![screenshot](documentation/browsers/chrome-my-activity.png) | ![screenshot](documentation/browsers/firefox-my-activity.png) | ![screenshot](documentation/browsers/edge-my-activity.png) | Works as expected |
| Edit Review | ![screenshot](documentation/browsers/chrome-edit-review.png) | ![screenshot](documentation/browsers/firefox-edit-review.png) | ![screenshot](documentation/browsers/edge-edit-review.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/edge-login.png) | Works as expected |
| Logout | ![screenshot](documentation/browsers/chrome-logout.png) | ![screenshot](documentation/browsers/firefox-logout.png) | ![screenshot](documentation/browsers/edge-logout.png) | Works as expected |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/edge-register.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/edge-404.png) | Works as expected |





## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Home Page| ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Browse Movies | ![screenshot](documentation/lighthouse/mobile-browse.png) | ![screenshot](documentation/lighthouse/desktop-browse.png) |
| Movie Detail | ![screenshot](documentation/lighthouse/mobile-movie-detail.png) | ![screenshot](documentation/lighthouse/desktop-movie-detail.png) |
| Submit Movie | ![screenshot](documentation/lighthouse/mobile-submit-movie.png) | ![screenshot](documentation/lighthouse/desktop-submit-movie.png) |
| Edit Movie | ![screenshot](documentation/lighthouse/mobile-edit-movie.png) | ![screenshot](documentation/lighthouse/desktop-edit-movie.png) |
| My Activity | ![screenshot](documentation/lighthouse/mobile-my-activity.png) | ![screenshot](documentation/lighthouse/desktop-my-activity.png) |
| Edit Review | ![screenshot](documentation/lighthouse/mobile-edit-review.png) | ![screenshot](documentation/lighthouse/desktop-edit-review.png) |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Logout | ![screenshot](documentation/lighthouse/mobile-logout.png) | ![screenshot](documentation/lighthouse/desktop-logout.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |


**Lighthouse Notes**

Mobile performance scores were generally lower than desktop scores due to render-blocking resources, image delivery recommendations, cache lifetime warnings, and font loading considerations identified by Lighthouse. Some of these recommendations relate to third-party resources, including externally hosted movie poster images retrieved through the TMDB API, and therefore fall outside the direct scope of project optimisation.

Accessibility, SEO, and Best Practices scores remained consistently high across the audited pages, indicating that the application provides a good overall user experience despite minor performance recommendations.


## Defensive Programming


Defensive programming was manually tested with the below user acceptance testing:


## Defensive Programming                                                        

| Page | Expectation | Test Performed | Result | Screenshot |
|-------|-------------|----------------|--------|------------|
| Navigation | Guest users should only see public navigation links. | Visited the site while logged out. | Submit Movie, My Activity and Logout were hidden. Login and Register links were displayed. | ![screenshot](documentation/defensive/guest-navbar.png) |
| Movie Detail | Guests should not be able to access movie details and reviews. | Selected **View Details** from a movie card while logged out. | User was redirected to the registration page. | ![screenshot](documentation/defensive/movie-detail-redirect.png) |
| My Activity | Users should only be able to manage their own content. | Logged in as User A and viewed the My Activity page. | Only movies and reviews submitted by User A were displayed. Content belonging to other users was not visible. | ![screenshot](documentation/defensive/my-reviews.png) |
| My Activity | Users should not be able to edit movies submitted by other users. | Logged in as User A and attempted to locate edit controls for a movie submitted by User B. | The movie was not displayed in My Activity and no edit controls were available. | ![screenshot](documentation/defensive/my-movies.png) |
| My Activity | Users should not be able to modify reviews created by other users. | Logged in as User A and viewed reviews written by User B. | No Edit or Delete options were displayed. | ![screenshot](documentation/defensive/user-b-review.png) |
| My Activity | Edit and Delete actions should only be available within My Activity. | Reviewed available actions on public pages and My Activity. | Edit and Delete buttons were only available for the user's own content within My Activity. | ![screenshot](documentation/defensive/my-activity.png) |
| Browse Movies / Home | Public pages should not expose content management actions. | Viewed public pages while logged in and logged out. | No Edit or Delete controls were displayed. | ![screenshot](documentation/defensive/public-movies.png) |
| Movie Detail | Users should only be able to submit one review per movie. | Submitted a review and revisited the movie detail page. | The review form was hidden and the user's existing review appeared first as **Your Review**. | ![screenshot](documentation/defensive/your-review.png) |
| Movie Submission | Duplicate movie titles should not be accepted. | Attempted to submit a movie already present in the database. | Submission was prevented and an appropriate validation message was displayed. | ![screenshot](documentation/defensive/duplicate-movie.png) |
| Movie Submission | Required fields should prevent incomplete submissions. | Attempted to submit a movie with missing required information. | Validation errors were displayed and submission was prevented. | ![screenshot](documentation/defensive/missing-fields.png) |
| Review Submission | Required fields should prevent incomplete reviews. | Attempted to submit a review with missing required information. | Validation errors were displayed and submission was prevented. | ![screenshot](documentation/defensive/missing-review-fields.png) |
| Moderation | Newly submitted movies should require administrator approval. | Submitted a movie recommendation. | The movie was stored as pending approval and remained hidden from public pages. | ![screenshot](documentation/defensive/movie-approval.png) |
| Moderation | Newly submitted reviews should require administrator approval. | Submitted a review. | The review remained remained hidden until approved by an administrator. | ![screenshot](documentation/defensive/no-reviews.png) |
| Moderation | Unapproved movies should not be publicly accessible. | Submitted a movie and verified public pages before approval. | The movie was inaccessible to other users and could not receive reviews until approved. | Manual test |
| Moderation | Users should be able to edit their own pending submissions. | Submitted content awaiting approval and attempted to edit it. | Content remained editable by its owner while pending approval. | ![screenshot](documentation/defensive/review-approval.png) |
| Moderation | Edited movies should require approval again. | Edited an approved movie submission. | The movie returned to pending approval status. | ![screenshot](documentation/defensive/movie-pending.png) |
| Moderation | Edited reviews should require approval again. | Edited an approved review. | The review returned to pending approval status. | ![screenshot](documentation/defensive/review-approval.png) |
| My Activity | Users should be able to edit movie submissions but not delete them. | Reviewed available actions for submitted movies. | Edit controls were available, while no Delete option was provided. | ![screenshot](documentation/defensive/no-delete-movie.png) |
| My Activity | Users should be able to edit and delete their own reviews. | Reviewed available actions for personal reviews. | Edit and Delete controls were available only for the user's own reviews. | ![screenshot](documentation/defensive/review-controls.png)|
| Movie Detail | Movies should remain visible even when no reviews exist. | Removed all reviews associated with a movie. | The movie remained visible and displayed a **Not reviewed yet** message. | ![screenshot](documentation/defensive/no-reviews.png) |
| Delete Protection | Users should confirm deletion actions. | Attempted to delete a review. | A confirmation page was displayed before deletion was completed. | ![screenshot](documentation/defensive/delete-protection.png) |
| User Feedback | Users should receive clear feedback after submitting or editing content. | Submitted and edited movies and reviews. | Success messages confirmed that the action was received and that content was awaiting approval where applicable. Messages remained visible until dismissed by the user. | ![screenshot](documentation/defensive/movie-approval.png) |
| Administration | Standard users should not have access to administrative functionality. | Attempted to access administrative pages as a regular user. | Access was denied. | ![screenshot](documentation/defensive/access-denied.png) |
| 404 Page | Invalid URLs should display a custom 404 page. | Navigated to a non-existent URL. | Custom 404 page was displayed successfully. | ![screenshot](documentation/defensive/404.png) |



## User Story Testing



| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse approved movie recommendations | so that I can discover movies recommended by the community. | ![screenshot](documentation/user-stories/browse.png) |
| As a guest user | I would like to be able to view the details of a movie | so that I can learn more about it and why it was recommended. | ![screenshot](documentation/user-stories/movie-detail.png) |
| As a guest user | I would like to filter and sort movie recommendations | so that I can find movies that match my interests more easily. | ![screenshot](documentation/user-stories/filter-sort.png)|
| As a guest user | I would like to register an account | so that I can contribute movie recommendations and reviews to the community. | ![screenshot](documentation/user-stories/register.png) |
| As a guest user | I would like to quickly understand the purpose of the website | so that I can decide whether it is relevant to me. | ![screenshot](documentation/user-stories/homepage.png)|
| As a user | I would like to navigate the website easily | so that I can quickly access the information and features I need. | ![screenshot](documentation/user-stories/navbar.png)|
| As a registered user | I would like to be able to log in and log out of my account | so that I can securely access member-only features. | ![screenshot](documentation/user-stories/login.png)|
| As a registered user | I would like to submit a movie recommendation | so that I can share movies I think other community members would enjoy. | ![screenshot](documentation/user-stories/submit.png)|
| As a registered user | I would like to submit a review for an existing movie | so that I can share my own opinion with the community. | ![screenshot](documentation/user-stories/movie-detail.png)|
| As a registered user | I would like to edit my own review | so that I can correct or update my opinion after submitting it. | ![screenshot](documentation/user-stories/edit-review.png)|
| As a registered user | I would like to delete my own review | so that I can remove content that I no longer wish to share. | ![screenshot](documentation/user-stories/delete-review.png)|
| As a site owner | I would like to approve submitted movie recommendations | so that I can make sure only suitable content is published on the website. | ![screenshot](documentation/user-stories/approve-movies.png) |
| As a site owner | I would like to approve submitted reviews | so that I can ensure that only appropriate user reviews are visible to the community. | ![screenshot](documentation/user-stories/approve-reviews.png)|
| As a site owner | I would like to manage movie records | so that the movie database remains accurate, relevant, and free of inappropriate content. | ![screenshot](documentation/user-stories/manage-movies.png) |
| As a site owner | I would like to manage the list of movie genres | so that movies can be categorised consistently across the website. | ![screenshot](documentation/user-stories/genres.png) |
| As a site owner | I would like an engaging homepage that clearly introduces the movie community | so that visitors better understand the community and are encouraged to participate. | ![screenshot](documentation/user-stories/homepage.png) |
| As a user | I would like to see a helpful custom 404 error page when I visit a broken link | so that I can easily return to the website instead of feeling stuck. | ![screenshot](documentation/user-stories/404.png) |
| As a user | I would like to see the average rating of a movie | so that I can quickly understand the community's opinion before reading reviews. | ![screenshot](documentation/user-stories/movie-detail.png) |
| As a user | I would like forms and review sections to be easy to read and interact with | so that submitting and managing reviews feels intuitive and pleasant. | ![screenshot](documentation/user-stories/review-controls.png) |
| As a user | I would like to see movie posters of the suggested films | so that browsing the website feels more engaging and visual. | ![screenshot](documentation/user-stories/poster.png)|



