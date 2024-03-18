"""
WSGI config for global project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from utils.environment import get_env

DEBUG = get_env('DEBUG') == '1'

if DEBUG :
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'global.settings.dev')
else :
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'global.settings.prod')

application = get_wsgi_application()