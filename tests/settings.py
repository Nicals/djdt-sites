SECRET_KEY = 'no-so-secret'

INSTALLED_APPS = [
    'django.contrib.sites',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}


INTERNAL_IPS = ['127.0.0.1']
