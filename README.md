# Food Tracker App

This is a simple application that can enable users to keep track of their daily eating habits by keeping record of food stuffs they eat as well as their dietary info. The backend is in Flask and Frontend in React.

## The Front-end

I am thinking of something to use from the front-end. (PLEASE CONTRIBUTE IF YOU ARE GOOD AT REACT :) I AM JUST BEGINNING TO LEARN IT.)

## The Backend

The backend is a REST API written in Python using:

- Flask (web framework)
- Flask-SQLAlchemy (Object Relational Mapper for SQL Databases)
- Flask-Marshmallow (Object SErialization and Desrialization library)
- SQLite (Database In Development)
- PostgreSQL (Database In Production)

## About The API

The API has two URL prefixes, `/api` and `/auth`. The `/api` routes are those that return data neede by users( In this case data containing food they have consumed and other info.).

On the other hand the `/auth` routes are for user authentication and authorization.

### A table about the API

| ENDPOINT | HTTP VERB | DESCRIPTION | DATA RETURNED |
| -------- | --------- | ----------- | ------------- |


### Run the backend with

Get this project

#### `git clone https://github.com/jod35/food-tracker-app.git`

Set the flask environment variables

#### `export FLASK_APP=run.py`

You can also set debug mode in case you want to develop (Optional)

#### `export FLASK_APP=1`

Finally run with

#### flask run

## Contributors

- [Ssali Jonathan](https://github.com/jod35)
- [A51F221B](https://github.com/A51F221B)
