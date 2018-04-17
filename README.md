
# Semantic Versioning Server

Yet another semantic versioning server made with Django

Semantic Versioning: https://semver.org/

**Features**

 - Getting build/release versions through GET requests
 - Incrementing version types seperately through POST requests
 - Creating or deleting projects using django-admin panel

**TO-DO**
 - Authentication
 - Creating, deleting projects using API

## Database Settings

Change this file if you're going to use a different database backend.
By default the application uses a containerized postgresql server.

Changes should be made in **versioning/settings.py** file.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }

## Starting the application

    docker-compose up -d

and that's it!

**docker-compose.yml**  > Change the port 8000 to 80 for production. (and do the other things such as setting the DEBUG mode to False in **versioning/settings.py**:26)

    version: '2'
    
    services:
      db:
        image: postgres
        ports: 
          - "5432:5432"
      web:
        build: .
        command: >
            bash -c "sleep 10s
            && python3 manage.py migrate
            && python3 manage.py shell -c \"from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')\"
            && python3 manage.py runserver 0.0.0.0:8000"
        volumes:
          - .:/code
        ports:
          - "8000:8000"
        depends_on:
          - db

## Usage

**GET REQUESTS**

    http://hostname:8000/project/projectName/getBuildVersion

returns the project's version (including the build number)
4.0.2.b001

    http://hostname:8000/project/projectName/getReleaseVersion
returns the project's version (without the build number)
4.0.2

**POST REQUESTS**

    curl -X POST -d version_type=major http://hostname:8000/project/projectName/incrementVersion
increments the project's major version
4.0.2.b001 -> 5.0.0.b000

## Using Django-Admin

    http://hostname:8000/admin
from here you can create new projects and change the current versions  

    Username: admin  
    Password: admin


