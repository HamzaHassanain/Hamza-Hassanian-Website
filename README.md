# A Personal Website (My Website)

### Contents

- [Description](#description)
- [About The Structure of the Application](#about-the-structure-of-the-application)
  - [Packages Used](#packages-used)
  - [Apps in this Project](#apps-in-this-project)
  - [About The .env File](#about-the-env-file)
  - [About The build.sh File](#about-the-buildsh-file)
- [How To Run The Project](#how-to-run-the-project)
- [Demo Video And How To Use The Admin Dashboard](#demo-video-and-how-to-use-the-admin-dashboard)

## Description

This is a Resume Website that I created to showcase my skills and projects. It is a single page website that is responsive and mobile friendly. It is Built with python Django, used Django Admin Panel to manage the content of the website. It is hosted on OnRender.

I also used PostgreSQL database to store the data of the website. I used Cloudinary to store the images and media files.

HTML CSS Template From <a href="https://designstub.com/" target="_blank">Designstub</a>

## About The Structure of the Application

- ### Packages Used

  - <strong> django:</strong> Is The Framework Used to build the website.
  - <strong> django-jazzmin:</strong> To Customize the Admin Panel.
  - <strong>cloudinary:</strong> To store the images and handel the media files.
  - <strong>python-decouple:</strong> To store the secret keys and passwords, (.env Files)
  - <strong>whitenoise:</strong> To serve the static files in production environment.
  - <strong>gunicorn:</strong> To serve the website in production environment.
  - <strong>psycopg2:</strong> To connect to the postgresql database.
  - <strong>martor:</strong> To add markdown editor to the admin panel. (But it is not used in the website)

- ### Apps in this Project:

  - <strong>project:</strong> This is the project folder, it contains the settings.py.
  - <strong>website:</strong> This is the app where I use the models from the other applications, and handle the views and urls.
  - <strong>NOTE THAT: Every app below is only responsible for the models and registering in the admin panel </strong>
  - <strong>experience:</strong> In this website I consider the experience to be: Education, Work, Volunteer, Open Source, and Awards ...... and whatever can be described as experience.
    - <strong> ExperienceCategory: </strong> This what spacifies the type of the experience as mentioned above.
    - <strong> Experience: </strong> This is the model that contains the information about the experience.
  - <strong> hero: </strong> This is the app that contains the information about the hero section of the website and the links on the navbar.
    - <strong> Hero: </strong> This is the model that contains the information about the hero section. NOTE: There can only be one hero section, if you try to add another one, it will throw an error.
    - <strong> BladeIcon: </strong> This is the model responsible for the links on the navbar. NOTE: The template uses the blade icons <a herf="https://blade-ui-kit.com/blade-icons#search" traget="_balnk"> icons library </a>, to use it, you copy the name of the icon and paste it in the icon field in the admin panel. For the icon to work it has to start with <code>ri</code>
  - <strong> personal_projects: </strong> This is the app that contains the information about the personal projects.
    - <strong> PersonalProject: </strong> This is the model that contains the information about the personal projects.
  - <strong> skills: </strong> This is the app that contains the information about the skills.
    - <strong> SkillCategory: </strong> This is the model that contains the information about the skill category.
    - <strong> Skill: </strong> This is the model that contains the information about the skills.
  - <strong> Photos </strong> This is the app responsible for the photos uploaded to the website (Note that the photos uploaded through other fileds are not saved in the database, they are saved in cloudinary directly)
    - <strong> Photo: </strong> This is the model itself.

- ### About The <code>.env</code> File:

```bash

# App
SECRET_KEY=#The-Secret-Key-Of-The-App
ALLOWED_HOST=localhost,
DEBUG=True # Change it to False in production environment

#supbase, we use it as the database host
host=#the-host-of-the-database
port=#the-port-of-the-database
database_name=#the-name-of-the-database
user=#the-username-of-the-database
password=#the-password-of-the-database

# Cloudinary (To store the images and media files)
cloud_name=#the-cloud-name
api_key=#the-api-key
api_secret=#the-api-secret

```

- ### About The <code>build.sh</code> File:

  - This file is used to build the website in the production environment, so when you deploy the website, you run this file to build the website. using the command <code>bash build.sh</code>

## How To Run The Project

- ### Clone the project

```bash
git clone https://github.com/HamzaHassanain/Hamza-Hassanian-Website.git

cd Hamza-Hassanian-Website
```

- ### Create the <code>.env</code> File

  - The way is described above.

- ### Generate a new Djagno Secret Key
  - you can then copy the secret key and paste it in the <code>.env</code> file in the <code>SECRET_KEY</code> field.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

- ### Activate the virtual environment and install the requirements

  - Note That you may encounter some errors while installing the requirements, if you do, you can install the requirements manually, by installing the packages in the <code>Pipfile</code> file. Using <code>pip install pacage-name</code> command.

  - When you open a new Terminal in VS Code, Make sure that the virtual environment is activated, if not, you can activate it using the command <code>pipenv shell</code>. You can also set the python interpreter to the virtual environment by clicking on the python interpreter in the bottom right corner of the VS Code and selecting the virtual environment.

```bash
pipenv shell
pipenv install
```

- ### Run the migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

- ### Create a superuser

```bash
python manage.py createsuperuser
```

- ### Collect the static files

```bash
python manage.py collectstatic
```

- ### Run the server

```bash
python manage.py runserver
```

## Demo Video And How To Use The Admin Dashboard

[![Demo](/thubmnail.png)](https://youtu.be/w7KCpos6J1U)
