from django.contrib import admin
from .models import Task, Event

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Customize the display and filtering of Tasks in the Admin panel.
    """
    list_display = ('title', 'user', 'due_date', 'priority', 'completed')
    list_filter = ('completed', 'priority', 'due_date')
    search_fields = ('title', 'description')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Customize the display and filtering of Events in the Admin panel.
    """
    list_display = ('title', 'user', 'date', 'start_time', 'end_time', 'location')
    list_filter = ('date', 'location')
    search_fields = ('title', 'description', 'location')
