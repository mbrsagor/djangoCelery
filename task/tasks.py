from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from time import sleep
from django.core.mail import send_mail

from celery import shared_task


@task(name="sum_two_numbers")
def add(x, y):
    return x + y


@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Send mail to server',
              'Hello there, I am django full-stack developer.',
              'your_mail@gmail.com',
              ['verepit474@demail3.com']
              )
    return None
