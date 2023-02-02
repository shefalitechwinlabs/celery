# feedback/tasks.py

from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task(name = "send_email")
def send_feedback_email_task(email_address, message):
    """Sends an email when the feedback form has been submitted."""
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    DEFAULT_CRONTAB = {
        "minute": "01",
        "hour": "*",
        "day_of_week": "*",
        "day_of_month": "*",
        "month_of_year": "*"
    }
    schedule = dict() 
    schedule['data'] = send_mail(
                        "Your Feedback",
                        f"\t{message}\n\nThank you!",
                        "support@example.com",
                        [email_address],
                        fail_silently=False,
                    )
    schedule['crontab'] = DEFAULT_CRONTAB
    schedule['run_immediately'] = True
    serializer = PeriodicTask(data=schedule)
    if serializer.is_valid():
        serializer.save()
    else:
        return ('Mail not sent')


@shared_task(name = "print_msg_main")
def print_message(message, *args, **kwargs):
  print(f"Celery is working!! Message is {message}")