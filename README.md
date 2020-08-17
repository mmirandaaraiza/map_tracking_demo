Map Demo App.
An API that manages vehicles and displays them on a map based on their coordinates.

# Instructions:

## Installing dependencies
Dependencies were locked using pipenv and python 3.8

- pipenv install
- pipenv shell


## Create database
Database will use sqlite3

- python manage.py makemigrations
- python manage.py migrate

## Create user(s)
- python manage.py createsuperuser

## Modify the map token
The map uses mapbox, you'll need an [access token](https://www.mapbox.com/studio/account/tokens/).

This token needs to be changed in root > website > static > scripts > main.js

## Run the development server
- python manage.py runserver

## Usage
App will be visible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Browseable API will be visible at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

Vehicles can be created, updated, or deleted in the browseable API.

If you want to use curl instead here are a couple examples, be sure to change the needed data marked with brackets:

**List**

curl -H 'Accept: application/json; indent=4' -u user:pass http://127.0.0.1:8000/api/vehicles/

**Create**

curl -d '{"plate":"plate", "lat": "lat", "long": "long"}' -H 'Content-Type: application/json' -H 'Accept: application/json; indent=4' -u user:pass http://127.0.0.1:8000/api/vehicles/

**Update**

curl -X PUT -d '{"plate":"plate", "lat": "lat", "long": "long"}' -H 'Content-Type: application/json' -H 'Accept: application/json; indent=4' -u user:pass http://127.0.0.1:8000/api/vehicles/id/

**Delete**

Delete returns a 204 no content response, a json response will only be seen if there was an error

curl -X DELETE -H 'Accept: application/json; indent=4' -u user:pass http://127.0.0.1:8000/api/vehicles/id/
