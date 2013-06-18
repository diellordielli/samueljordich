from . import models
from django.contrib import admin


class IllustrationAdmin(admin.ModelAdmin):
    model = models.Illustration
    list_display = ('ordering', 'category', 'date', 'image',)
    search_fields = ('ordering', 'category', 'image',)
    list_filter = ('ordering', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(models.Illustration, IllustrationAdmin)
admin.site.register(models.Category, CategoryAdmin)
