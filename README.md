# Hackathon App

This is a very simple Django app that can be used as a boilerplate for hackathons.

It contains one `Record` model and 3 simple views:
1. The dashboard
2. The records list view
3. The records detail view

## Python version

This app uses Python version `3.10.14`.

## Get started

1. Ensure `pip` is installed - see instructions [here](https://pip.pypa.io/en/stable/installation/)
2. Install `virtualenv`: `python -m pip install --user virtualenv`
3. Create a virtual environment:  `virtualenv .venv`
4. Activate the virtual enviroment: `source .venv/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Install pre-commit hooks: `pre-commit install`
7. Run all migrations: `python manage.py migrate`
8. Run the local server: `python manage.py runserver`
9. Go to `http://127.0.0.1:8000/`

## Helpful commands

Make migrations for the `records` app:
```
python manage.py makemigrations records
```

Run migrations for the `records` app:
```
python manage.py migrate records
```

Create a superuser:
```
python manage.py createsuperuser
```