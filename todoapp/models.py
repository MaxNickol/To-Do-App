from datetime import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class To_Do(models.Model):
    description = models.CharField(max_length=500, blank=False)
    time_creation = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDos'