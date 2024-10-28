import os
import sys

# Adjust the paths below
path = '/home/Sodiqjon/restaurant-booking-system'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

# Activate the virtual environment
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
