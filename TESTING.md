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
