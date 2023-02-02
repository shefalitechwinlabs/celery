# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    #Scheduler Name
    'send-email-one-minute': {
        # Task Name (Name Specified in Decorator)
        'task': 'send_email',  
        # Schedule      
        'schedule': 60.0,
        # Function Arguments 
        'args': ("shefali.techwinlabs@gmail.com","Hello") 
    }
}
