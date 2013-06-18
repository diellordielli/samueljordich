from . import models
from django.contrib import admin


class GrafikAdmin(admin.ModelAdmin):
    model = models.Grafik
    list_display = ('ordering', 'category', 'date', 'image',)
    search_fields = ('ordering', 'category', 'image',)
    list_filter = ('ordering', 'category',)


class CategorygAdmin(admin.ModelAdmin):
    model = models.Categoryg
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(models.Grafik, GrafikAdmin)
admin.site.register(models.Categoryg, CategorygAdmin)
