from os import environ
from redis.client import Redis

SECRET_KEY = b'\x80\xf2/\xc7\xfb\xf2\xa3E\xb34OCI\xd9~.'

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'charset': 'utf8mb4'
    }
}

ENVIRONMENT_DEVELOPMENT_MODE = environ['FLASK_ENV'] == 'development'
DEBUG = ENVIRONMENT_DEVELOPMENT_MODE
TEMPLATES_AUTO_RELOAD = ENVIRONMENT_DEVELOPMENT_MODE
SEND_FILE_MAX_AGE_DEFAULT = 0
STATIC_URL = 'http://127.0.0.1:7070/'

CSRF_COOKIE_NAME = 'csrf_token'

JWT_SECRET_KEY = b'%\xc3o\xec\\\xcc\x80\xcd\xcd\x96\xfc\x8d\nS\xd11'

REDIS_URL = environ['REDIS_URL']


def redis_cli(db: int = 0):
    return Redis.from_url(REDIS_URL, db=db)
