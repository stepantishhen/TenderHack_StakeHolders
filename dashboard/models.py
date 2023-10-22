# encoding: utf-8
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Error(models.Model):
    error = models.CharField(max_length=255)
    # status, priority
    other_details = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(max_length=255)


class SystemLog(models.Model):
    date_time = models.DateTimeField()
    log = models.TextField()
    category = models.CharField(max_length=255, null=True)


class Ticket(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема")
    text = models.TextField(verbose_name="Обращение")
    performer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets', verbose_name="Исполнитель")
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets', verbose_name="Инициатор")
    status = models.CharField(max_length=255,  verbose_name="Статус")
