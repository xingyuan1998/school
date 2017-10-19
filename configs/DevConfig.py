import os

DEBUG = True
WTF_CSRF_ENABLED = False
SECRET_KEY = 'youcannotguessit'

MONGODB_DB = 'test2'
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017

BASE_DIR = os.getcwd() + '/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
