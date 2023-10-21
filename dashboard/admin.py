from django.contrib import admin
from .models import Error, Notification, SystemLog, Ticket

class ErrorAdmin(admin.ModelAdmin):
    list_display = ('error', 'other_details', 'user_id')
    search_fields = ('error', 'other_details', 'user_id__username')
    list_filter = ('user_id__username', )

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'text', 'status')
    search_fields = ('recipient__username', 'text', 'status')
    list_filter = ('recipient__username', 'status')
    list_display_links = ('text', )

class SystemLogAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'log', 'category')
    search_fields = ('log', 'category')
    list_filter = ('category', )

class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'text', 'performer', 'initiator', 'status')
    list_display_links = ('subject', )
    list_editable = ('status', )
    search_fields = ('subject', 'text', 'performer__username', 'initiator__username')
    list_filter = ('status', 'performer__username', 'initiator__username')

admin.site.register(Error, ErrorAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(SystemLog, SystemLogAdmin)
admin.site.register(Ticket, TicketAdmin)
