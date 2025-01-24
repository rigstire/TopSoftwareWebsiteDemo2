import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TopSoftware.TopSoftware.settings.py')

application = get_wsgi_application()
