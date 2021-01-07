from .base import *

DEBUG = True

ALLOWED_HOSTS = []

ALLOWED_HOSTS = ["https://www.madalinpopa.com", "www.madalinpopa.com", "http://www.madalinpopa.com"]

DATABASES['production'] = {
    "ENGINE": "django.db.backends.mysql",
    "HOST": os.environ.get("DB_HOST"),
    "NAME": os.environ.get("DB_NAME_BLOG_MADALIN"),
    "USER": os.environ.get("DB_USER"),
    "PASSWORD": os.environ.get("DB_PASSWORD"),
}
