# Static folder purpose

This folder is used when serving static files with Django. When running `python manage.py collectstatic`, Django will merge this folder content with it's own content and the result will be copied to `STATIC_ROOT` (which in this project, is `public/static_root/`).
