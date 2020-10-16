web: python manage.py migrate
web: gunicorn blogproject.wsgi -w 2 -k gthread -b 0.0.0.0:8000 --log-file -
