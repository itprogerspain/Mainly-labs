from django.db import models
from apps.accounts.models import CustomUser
from datetime import datetime


# Create your models here.
class Course(models.Model):

    MODALITY_CHOICES = [
        ('online', 'online'),
        ('personal' 'personal')
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    created_by = models.DateField(auto_now=True)
    modality = models.CharField(max_length=20, choices=MODALITY_CHOICES)


class UserCourseProgress(models.Model): # execute this one, once the user click on start course
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_started = models.DateField(auto_now=True, blank=True, null=True) 
    date_finished = models.DateField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True) 

    def save(self, *args, **kwargs):
        if self.date_started and self.date_finished:
            self.duration = self.date_finished - self.date_started
        super().save(*args, **kwargs)


class certificate(models.Model):
    pass
