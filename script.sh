/usr/local/bin/gunicorn mankiapp.wsgi:application --bind 0.0.0.0:8000 --pid /tmp/gunicorn.pid
