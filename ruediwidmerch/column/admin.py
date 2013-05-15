from . import models
from django.contrib import admin


class ColumnAdmin(admin.ModelAdmin):
    model = models.Column
    list_display = ('title', 'date',)
    search_fields = ('title', 'date',)
    list_filter = ('title', 'date',)

admin.site.register(models.Column, ColumnAdmin)
