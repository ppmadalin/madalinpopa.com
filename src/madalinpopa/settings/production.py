from .base import *

DEBUG = False

ALLOWED_HOSTS = []

ALLOWED_HOSTS = ["https://www.madalinpopa.com", "www.madalinpopa.com", "http://www.madalinpopa.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME_BLOG_MADALIN"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
}
