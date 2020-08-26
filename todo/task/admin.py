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

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.has_perm('task.view_task'):
            return qs.filter(status=Task.TODO)
        else:
            return qs.none()


admin.site.register(Task, TaskAdmin)
