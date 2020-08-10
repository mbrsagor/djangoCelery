from django.db import models


class Calculator(models.Model):
    title = models.CharField(max_length=70)
    first_number = models.IntegerField(default=0)
    last_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def add_number(self):
        return self.first_number + self.last_number

    @property
    def sub_number(self):
        return self.first_number - self.last_number

    @property
    def multiple_number(self):
        return self.first_number * self.last_number

    @property
    def division_number(self):
        return self.first_number / self.last_number
