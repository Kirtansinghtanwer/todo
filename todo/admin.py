from django.contrib import admin
from .models import Task
class taskadmin(admin.ModelAdmin):
    list_display = ('task','is_completed','updated_at')
    search_fields = ('task',)
admin.site.register(Task,taskadmin)
