from . import models
from django.contrib import admin


class CartoonAdmin(admin.ModelAdmin):
    model = models.Cartoon
    list_display = ('ordering', 'category', 'date', 'image',)
    search_fields = ('ordering', 'category', 'image',)
    list_filter = ('ordering', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(models.Cartoon, CartoonAdmin)
admin.site.register(models.Category, CategoryAdmin)
