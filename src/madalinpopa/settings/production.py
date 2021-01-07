from .base import *

DEBUG = True

ALLOWED_HOSTS = []

ALLOWED_HOSTS = ["https://www.madalinpopa.com", "www.madalinpopa.com", "http://www.madalinpopa.com"]

DATABASES['default'] = {
    "ENGINE": "django.db.backends.mysql",
    "HOST": os.environ.get("DB_HOST"),
    "NAME": os.environ.get("DB_NAME_BLOG_MADALIN"),
    "USER": os.environ.get("DB_USER"),
    "PASSWORD": os.environ.get("DB_PASSWORD"),
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True