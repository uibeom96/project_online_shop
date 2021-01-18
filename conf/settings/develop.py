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