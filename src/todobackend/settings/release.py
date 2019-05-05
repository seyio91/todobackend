from base import *
import os

if os.environ.get('DEBUG'):
	DEBUG = True
else:
	DEBUG = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', '*')]

#Prod DB Setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
        'USER': os.environ.get('MYSQL_USER', 'todo'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306')
    }
}

#Path to whether static content will be located
STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/www/todobackend/static')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/www/todobackend/media')
