from conf.settings.base import *

with open("secret.json", "r", encoding="UTF-8") as f:
    secret_list = loads(f.read())

def get_secret(key, secret_list = secret_list):
    try:
        return secret_list[key]

    except KeyError:
        raise ImproperlyConfigured(f"{key}오류") 

SECRET_KEY = get_secret("KEY_DJANGO") 


DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "project_online_shop_develop",
        "USER":     get_secret("KEY_DB_DV_USER"),
        "PASSWORD": get_secret("KEY_DB_DV_PASSWORD"),
        "HOST":     get_secret("KEY_DB_DV_HOST"),
        "PORT":     get_secret("KEY_DB_DV_PORT"),
    }
}