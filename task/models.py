from django.db import models


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Calculator(BaseEntity):
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

    
    class Task(BaseEntity):
        task_name = models.CharField(max_length=100)
        start_day = models.CharField(max_length=100)
        
        def __str__(self):
            return self.task_name
        
