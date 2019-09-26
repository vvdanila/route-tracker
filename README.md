# Route Tracker App

# Local Development

To run the project locally:

`docker-compose build`
`docker-compose up` or `docker-compose up -d` to run docker-compose in detached mode

## Migrations

To make migrations:

`docker-compose run web python manage.py makemigrations`

To run the migrations:

`docker-compose run web python manage.py migrate`

## Unit Tests

To run the test suite:

`docker-compose run web python manage.py test`
