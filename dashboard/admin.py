from django.contrib import admin

from dashboard.models import *

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Error)
admin.site.register(Notification)
admin.site.register(SystemLog)
admin.site.register(Category)
