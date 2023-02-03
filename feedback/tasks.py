# feedback/tasks.py

from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task(name = "send_email")
def send_feedback_email_task():
    """Sends an email when the feedback form has been submitted."""
    # sleep(20)  # Simulate expensive operation(s) that freeze Django
    send_mail(
        "Your Feedback",
        f"\t{'hi'}\n\nThank you!",
        "support@example.com",
        ['shefali.techwinlabs@gmail.com'],
        fail_silently=False,
    )

# @shared_task(name = "print_msg_main")
# def print_message(message, *args, **kwargs):
#   print(f"Celery is working!! Message is {message}")
