python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser

gunicorn global.wsgi:application --workers=2 --timeout 120 --bind=0.0.0.0:80