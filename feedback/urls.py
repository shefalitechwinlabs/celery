from django.urls import path
from .views import celery_task
from feedback.views import  SuccessView, schedule_task

app_name = "feedback"

urlpatterns = [
    path("", celery_task, name="celery_task"),
    path("success/", SuccessView.as_view(), name="success"),
    path("schedule_task/", schedule_task, name="schedule_task"),
]
