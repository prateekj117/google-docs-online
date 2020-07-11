#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic            # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn navigus_assignment.wsgi:application \
    --name navigus_assignment \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
