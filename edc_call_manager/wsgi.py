import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'edc_call_manager.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()