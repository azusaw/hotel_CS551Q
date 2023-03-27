# Disaster information Website

Team hotel_CS551Q

## Website

https://disaster-info.onrender.com/

## Member

`@azusaw` AZUSA WATANABE

`@darryl484` ARUN DARRYL MATHEW

`@kksaki` SUN JIAQ

`@t21ka22` AGYENIM BOKOFI

`@PhilipUkwamedua` UKWAMEDUAPHILIP CHUKA

## Prepared Data

[ALL NATURAL DISASTERS 1900-2021 / EOSDIS](https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis)
by Kaggle

## For Starting Server

Create `.env` file in root directory with below contents.

⚠️ DO NOT commit `.env` file into this repository.

```.env
DEBUG=True
```

Then, start the server with this command.

```commandline
# install dependencies
pip install -r requirements.txt

# create database
python3 manage.py parse_csv

# run server
python3 manage.py runserver 8000
```

## For run Testing

```commandline
python3 manage.py test
```

## When edit models

```commandline
# create files for migration after editing models
python3 manage.py makemigrations

# execute migration
python3 manage.py migrate
```

## For deployment in render

```commandline
# create requirements.txt
pip list --format=freeze > requirements.txt
```
