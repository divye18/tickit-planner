from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """
    Model representing a planning Task, mapped from your CLI task structure.
    """
    PRIORITY_CHOICES = [
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    """
    Model representing a Calendar Event, mapped from your CLI event structure.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title
