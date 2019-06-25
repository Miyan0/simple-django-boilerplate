# Simple Django Boilerplate
Home page [simple-django-boilerplate](https://github.com/Miyan0/simple-django-boilerplate)

## Differences from Django Turorial

### TLDR

Principal differences from the Django tutorial for creating a new project

- no nested project structure,
- multiple settings files for development, staging, production,
- custom user,
- environment variables,
- core app for management and other common tasks,
- public folder for static_root and media folders,
- default editorconfig, eslint, gitignore setting files

---

### Project structure

If you follow the [tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/) for creating a new Django project using `django-admin startproject mysite` you'll end up with a structure like this:

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

I find having a folder `mysite` inside a folder `mysite` confusing. Sure, you can rename the outer one anything you want but I prefer avoiding unecessary nesting. In many tutorials around the web, you'll often find creating projects this way `django-admin startproject mysite .` (note the '.') which creates this structure:

```
manage.py
mysite/
    __init__.py
    settings.py
    urls.py
    wsgi.py

```

This is the way this boilerplate was created. It's just that the project name is `config`.

---
### Usage


This project assumes you have `pipenv` installed, if not:

For macOS users:
```bash
brew install pipenv
```

For other OS see [Installing Pipenv](https://docs.pipenv.org/en/latest/install/#installing-pipenv)

Feel free to use any virtual environment manager. If you do, you will need to:

- install Django (pip install Django)
- use some way (Ex: python-dotenv) to load environment variables.

### Misc files

`.editorconfig`

Edit or remove this if you don't use [Editor config](https://editorconfig.org/)

`.eslintrc`

Edit or remove this if you don't use [ESLint](https://eslint.org/)

`.gitattribute`

Edit or remove this if you don't use [Git Documentation](https://www.git-scm.com/docs/gitattributes)

### Packages

The only required package is Django

This boilerplate does not use any development packages but if you
want to, use the following command:

```bash
pipenv install --dev <name-of-your-package>
```

Some great development packages:
- django-debug-toolbar -> adds a debuging toolbar to the Browser
- django-extensions -> various utilities
- flake8 -> linter
- black -> code formatter

### Clone or fork the repo

Fork the project

### 1- Setup virtual environment

Note: If you are using Pipenv do not use `pip install`, use `pipenv install`

- execute `pipenv shell` to create the virtual environment
- execute `pipenv install` to install the production's packages



### 2- Environment variables

- in `example.env` change the placeholders values for the database variables
- rename `example.env` to `.env`

### Note

If you need to change the SECRET_KEY you can use the provided key_generator command:

```bash
python manage.py key_generator
```
This will create a 50 characters string which you can copy from the terminal.

### Included Django Applications

__core__

Common place for project specific stuff.

__users__

Latest Django documentation strongly suggest to use a custom user. See why here:
[Django documentation](https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project)

### Purpose of the public folder

This is where all static files (yours, django etc.) will end up when you run `python manage.py collectstatic`. This
is also where you should place `media` files. In this boilerplate, the `public` folder is under version control for convenience, but you should include it in `.gitignore` so you don't overwrite uploaded images from your users in production.

This way, when using `Gunicorn` and `nginx` in production, you can tell `nginx` to serve the public folder.


### 3- Running the project for the first time

The default database is Sqlite and you don't need to do anything to use it. If you want to use Postgres though, make sure you create your database first.

Create a new Postgres database:

```bash
psql
```

Look at the invite (your_name), this will be the owner of the db.

### Note 2

Make sure you have a user of that name with all privileges in your Postgresql installation. And don't forget the semi-colon!

```psql
<your_name>=# CREATE DATABASE <your_database_name>;
```

Run the migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

### Note 3

If your using Pipenv, the `Pipfile` include a script to start the Django server.
```bash
pipenv run server
```

## Production setup

- for safety, generate a new SECRET_KEY.

Edit `templates/robot.txt` as it currently disallow everything.
