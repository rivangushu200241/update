web: gunicorn djangoWebsite.wsgi:application --log-file - --log-level debug

release: python manage.py makemigrations VRCpubs
release: python manage.py migrate VRCpubs
