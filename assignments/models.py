from django.db import models


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    first_term = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    second_term = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    sum = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


"""
Source:
https://saasitive.com/tutorial/django-celery-redis-postgres-docker-compose/
"""
