web: gunicorn navigus_assignment.wsgi
web: daphne navigus_assignment.asgi:application --port $PORT --bind 0.0.0.0
worker: python manage.py runworker -v2
worker: celery -A navigus_assignment worker -l info -B