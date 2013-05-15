from . import models
from django.contrib import admin


class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = ('title', 'date',)
    search_fields = ('title', 'date',)
    list_filter = ('title', 'date',)

admin.site.register(models.Event, EventAdmin)
