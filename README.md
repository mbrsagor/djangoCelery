# Task scheduling

## Setup

### Dependancies

- Python 3.6.9 
- postgres 13.2
- Django 3.0

The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed the django apps run on Windows, you should have little problem getting
up and running.

### Install ```vritualenv```
Activate `virutalenv` like
```
source venv/bin/activate
```

### Install radis server 
On Mac OS
```
brew install redis
brew services start redis
```
Brew permission errors? Try ```sudo chown -R "$USER":admin /usr/local```

Open & Test Redis: open terminal
```
redis-cli ping
```
Output:
```PONG```

Then run redis server: ```redis-server```
![alt text](<https://res.cloudinary.com/mbrsagor/image/upload/v1589358011/Screenshot_2020-05-13_at_2.16.29_PM_v9uglj.png>)

##### Install Celery + Redis in your virtualenv.
```
pip install "celery[redis]"
pip install redis
pip install django-celery-beat
pip install django-celery-results
pip freeze > requirements.txt
```

##### Settings.py which install app added `2` third party app.
````
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
]
````
Then
``````
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
``````

#### Create celery.py to setup Celery app:
   - [ ] Navigate to root project config module (where `settings` and `urls` modules are)
   - [ ] Navigate to root project config module (where settings and urls modules are)

   - [ ] ![alt text](<https://res.cloudinary.com/mbrsagor/image/upload/v1589358693/celery_frfxio.png>)

Then clone the project from `git` then the documentation follow. Hopefully, the project will run successfully. If any
 kind of errors please search `google` or `youtube` you will get very good result.
 
 
#### Migrate and create superuser
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

###### Run Celery Locally
* Run the Celery Consumer Worker (locally). Make sure virtualenv is activated and this command where you run runserver*

- First run a new terminal and follow the command
`celery -A CeleryTask worker -l info`

- Then open another terminal and run the command.
`celery -A CeleryTask beat -l info -S django`

* To see Celery Worker status

###### Here `CeleryTask` is a project name. If you develop same like app you may change there app name.
