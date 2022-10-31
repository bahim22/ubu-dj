
# dj-ded-py

## Python notes for Django, React Full stack app

## Initialize Django Project

[]: # Language: python
[]: # Requires: django
[]: # virtualenv: true

1. Verify you have `python` and `pip` installed and up to date
   1. Can use package managers such as Anaconda, Miniconda, Homebrew
2. Open terminal to create dev environment (using bash and pwsh for this project)
3. Check env to insure python is in Path
4. Make and cd into a directory to contain parent project and apps
5. Create and activate a virtual env and open in VS-code
   1. Alternates: virtualenv, venv, conda env
6. Depending on OS you may need to adjust shell scripts (pip3, python3; source, scripts, bin, sudo)
7. Select python interpreter and install dependencies
8. Create Django App
9. Make a super user to use admin dashboard gui

```bash
mkdir proj-name && cd proj-name/
python3 -m venv .venv
source .venv/bin/activate
code .
```

## Project

1. create project
2. create empty database
   1. Using SQLite for boilerplate structure
   2. Will create MongoDB and PostgreSQL for prod
3. run server
4. create requirements.txt for Dep
5. create launch.json in vs-code dir for debug
6. create .env file for env var
   1. dev.env and prod.env
7. to define an env var in def file use
   1. ex: VAR2='${env:VAR1}'

```bash
pip freeze > requirements.txt
# // must reactivate venv and install req.txt when restarting dev
pip install -r requirements.txt
# // alternatively //
conda create -n env-01 python=3.9
```

```bash
django-admin startproject stack_project .
python manage.py migrate
python manage.py runserver
python manage.py startapp app1
```

## Django App 1

1. Main app info
   1. _urls.py_
      1. used for routing urls to views
      2. any urls from app need to be configured in project urls.py also
   2. _models.py_
      1. data objects for database using classes
   3. _views.py_
      1. http request and response functions
      2. api functions
   4. _forms.py_
2. `Templates` dir
   1. html pages
      1. add _base.html with meta tags in head for css, fonts, js etc.
      2. can use load static and block content to customize other pages off of base
3. `Static` dir
   1. css and js code files

## App Views

```python
from . import views
from django.urls import path
urlpatterns = [
    path(route: str, views: (...) => HttpResponseBase)
    path('/', views.index, name='index')
]
# (route: str, view: (...) -> HttpResponseBase, kwargs: Dict[str, Any] = ..., name: str = ...) -> URLPattern
# (route: str, view: Sequence[URLResolver | str], kwargs: Dict[str, Any] = ..., name: str = ...) -> URLResolver
# (route: str, view: Sequence[URLResolver | str], kwargs: Dict[str, Any] = ..., name: str = ...) -> URLResolver
```

- URL patterns contain path() function that's passed four args
  - route and view and optional args: kwargs, name
  - name alawys ref the URL in other parts of the Django app (such as in the temps)
- starts at top of urlpatters list until it finds a match for the req

```txt
"When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments"
```

> Can create add'l apps to compartmentalize different aspects of the web app and use as modules for other projects
> Add (# type: ignore) to a line or top of file to disable type checking