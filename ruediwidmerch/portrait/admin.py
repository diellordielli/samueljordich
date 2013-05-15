from . import models
from django.contrib import admin


class PortraitAdmin(admin.ModelAdmin):
    model = models.Portrait
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

admin.site.register(models.Portrait, PortraitAdmin)
