from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
# from django.views.generic.edit import FormView
import sys
import json
from .tasks import send_feedback_email_task
# from feedback.forms import FeedbackForm


# class FeedbackFormView(FormView):
#     template_name = "feedback/feedback.html"
#     form_class = FeedbackForm
#     success_url = "/success/"
#     print(sys.platform)
#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)

def celery_task(request):
    send_feedback_email_task.delay
    return HttpResponse('task done')

class SuccessView(TemplateView):
    template_name = "feedback/success.html"

def schedule_task(request):
    schedule, crontab = CrontabSchedule.objects.get_or_create(hour=19, minute=26)
    task = PeriodicTask.objects.create(
        crontab = schedule,
        name = 'schedule_task_1',
        task = 'feedback.tasks.send_feedback_email_task',
        # args = json.dumps('shefali.techwinlabs@gmail.com',)
    )
    return HttpResponse('taskcreated')
