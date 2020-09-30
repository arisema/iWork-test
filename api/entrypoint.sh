#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
# python manage.py migrate

if [ "$ENV" = "development" ];
then
    python manage.py runserver 0.0.0.0:5000
elif [ "$ENV" = "testing" ];
then
    ./manage.py test
elif [ "$ENV" = "production" ];
then 
    gunicorn api.wsgi:application --bind 0.0.0.0:5500
fi

exec "$@"