# ylwang.codes - fullstack personal portfolio/blog

> A Django backend/frameworkless front-end lightweighted personal website, intended for IMT549 web client development

## Grading checklist:
### Basic:
- ✔️ Valid HTML as checked by https://validator.w3.org/ (Links to an external site.)
    - 2 unfixed warning, 0 errors for all pages
- ✔️ Be responsive at multiple screen sizes
- ✔️ More than a single page
    - each post is a independent sub page
- ✔️ More than a single page
- ❕  Data should be stored in a Javascript array
    - meet the requirement of external source API instead
- ✔️ At least one dropdown or open text field to filter the data
    - support title keyword search   
### Extra:
- ✔️ Overall visual style consistency
    - I think it is consistent
- ✔️ Pulling in data from an external source (API)
    - the data are fetched from REST API provided by djangorestframework
- ❕ Pass the accessibility automated checker (aXe browser extension)
    - 40 issues of #Elements must have sufficient color contrast# 
    - Heading levels should only increase by one (oh, come on..)


## Installation

### Self-hosting server


- Install dependencies

    ```bash
    $ cd ylwang.me
    $ pipenv install --dev
    ```

- migrate database

    ```bash
    $ pipenv run python manage.py migrate
    ```

- register admin

    ```bash
    $ pipenv run python manage.py createsuperuser
    ```

- run server

    ```bash
    $ pipenv run python manage.py runserver
    ```

Index page:

https://github.com/LouisYLWang/ylwang.codes/blob/master/templates/blog/index.html
