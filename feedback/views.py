from django.views.generic.base import TemplateView
# from django.views.generic.edit import FormView
import sys
# from feedback.forms import FeedbackForm


# class FeedbackFormView(FormView):
#     template_name = "feedback/feedback.html"
#     form_class = FeedbackForm
#     success_url = "/success/"
#     print(sys.platform)
#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "feedback/success.html"
