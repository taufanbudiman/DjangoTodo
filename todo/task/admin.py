from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status']
    fields = ['description']
    ordering = ('-status', 'id')

    actions = ['set_done']

    def set_done(self, request, queryset):
        updated = queryset.update(status=Task.DONE)
        self.message_user(request, ngettext(
            '%d task was successfully marked as done.',
            '%d tasks were successfully marked as done.',
            updated,
        ) % updated, messages.SUCCESS)
    set_done.short_description = "Mark selected task as Done"

admin.site.register(Task, TaskAdmin)
