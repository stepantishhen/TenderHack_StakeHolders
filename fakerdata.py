from django.contrib.auth.models import User
from django.db import models
from faker import Faker
import random

from dashboard.models import *

fake = Faker()

# Генерация пользователей
for _ in range(10):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    User.objects.create_user(username=username, email=email, password=password)

# Генерация ошибок
for _ in range(20):
    error = fake.sentence()
    other_details = fake.paragraph()
    user = random.choice(User.objects.all())
    Error.objects.create(error=error, other_details=other_details, user_id=user)

# Генерация уведомлений
for _ in range(15):
    recipient = random.choice(User.objects.all())
    text = fake.text()
    status = random.choice(['unread', 'read'])
    Notification.objects.create(recipient=recipient, text=text, status=status)

# Генерация системных логов
for _ in range(30):
    date_time = fake.date_time_this_year()
    log = fake.sentence()
    category = fake.word()
    SystemLog.objects.create(date_time=date_time, log=log, category=category)

# Генерация тикетов
for _ in range(10):
    subject = fake.sentence()
    text = fake.text()
    performer = random.choice(User.objects.all())
    initiator = random.choice(User.objects.all())
    status = random.choice(['open', 'closed'])
    Ticket.objects.create(subject=subject, text=text, performer=performer, initiator=initiator, status=status)
