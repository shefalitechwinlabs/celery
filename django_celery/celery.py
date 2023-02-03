# django_celery/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_celery.settings")
app = Celery("django_celery")
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')
app.config_from_object("django.conf:settings", namespace="CELERY")

# from mongoengine import connect

# DEFAULT_CONNECTION_NAME = connect('test')

# app.conf.beat_schedule = {
#     #Scheduler Name
#     'send-email-one-minute': {
#         # Task Name (Name Specified in Decorator)
#         'task': 'send_email',  
#         # Schedule      
#         'schedule': 60.0,
#         # Function Arguments 
#         'args': ("shefali.techwinlabs@gmail.com","Hello") 
#     }
# }

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# from celerybeatmongo.models import PeriodicTask

# periodic = PeriodicTask(
#     # name='send-email-one-minute',
#     task="send_email",
#     interval=PeriodicTask.Interval(every=10, period="seconds"), # executes every 10 seconds.
#     args=("shefali.techwinlabs@gmail.com","Hello")
# )
# periodic.save()


