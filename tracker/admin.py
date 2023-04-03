from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "created_datetime", "deadline_datetime", "done")
    search_fields = ("title",)
    list_filter = ("tags", "done", "deadline_datetime")


admin.site.register(Tag)
admin.site.unregister(Group)
