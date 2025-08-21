"""
Test settings for xblock-pdf
"""
import os

SECRET_KEY = 'test-secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'pdf',
]

USE_TZ = True

# XBlock settings
XBLOCK_MIXINS = ()
XBLOCK_SELECT_FUNCTION = lambda block_type: block_type  # pylint: disable=unnecessary-lambda
