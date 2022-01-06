from django.contrib import admin

from .models import UrlEntry, UrlBookmarked


class MyHistory(admin.ModelAdmin):
    list_display = ('id_url', 'url', 'add_at')

admin.site.register(UrlEntry, MyHistory)
admin.site.register(UrlBookmarked, MyHistory)

