from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Error(models.Model):
    error = models.CharField(max_length=255)
    other_details = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(max_length=255)


class SystemLog(models.Model):
    date_time = models.DateTimeField()
    log = models.TextField()
    category = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Ticket(models.Model):
    subject = models.CharField(max_length=255)
    text = models.TextField()
    performer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets')
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')

    def __str__(self):
        return self.subject
