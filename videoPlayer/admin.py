from django.contrib import admin

from .models import UrlEntry


class MyHistory(admin.ModelAdmin):
    list_display = ('id_url', 'url', 'add_at')

admin.site.register(UrlEntry, MyHistory)
