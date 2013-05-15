from . import models
from django.contrib import admin


class NewsAdmin(admin.ModelAdmin):
    model = models.News
    list_display = ('title', 'date', 'featured')
    search_fields = ('title', 'date', 'featured')
    list_filter = ('title', 'date', 'featured')

admin.site.register(models.News, NewsAdmin)
