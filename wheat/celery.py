<<<<<<< HEAD
from __future__ import absolute_import
=======
>>>>>>> b5b906d1a8704941c008928e7f7f528a0d7d45fb
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wheat.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wheat.settings')
>>>>>>> b5b906d1a8704941c008928e7f7f528a0d7d45fb

app = Celery('wheat')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.

app.config_from_object('django.conf:settings',namespace='CELERY')

#Load task modules from all registered Django app configs.

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
	print('Request:{0!r}'.format(self.request))
