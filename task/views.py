from django.http import HttpResponse
from .tasks import send_email_task


def home(request):
    send_email_task.delay()
    return HttpResponse('<h2>Celery process done...</h2>')
