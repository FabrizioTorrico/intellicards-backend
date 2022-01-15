This is a [Django](https://django.com/) project bootstrapped with [`django-admin startproject mysite`](https://docs.djangoproject.com/en/4.0/intro/tutorial01/).

## Getting Started

### don't forget to copy the project

First, install the dependencies. For that we need to:

```bash
#create virtual environment
python -m venv venv

# activate virtual environment
venv/Scripts/activate

#install dependencies
pip install -r requirements.txt
```

Then configure your database and credentials by modifying `settings.py`.

finally run the development server:

```bash

#make migrations
python manage.py makemigrations
python manage.py migrate

#start the debvelopment server
python manage.py runserver

```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

happy coding :)
