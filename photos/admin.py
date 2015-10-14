from django.contrib import admin

from photos.models import TemporaryImage


@admin.register(TemporaryImage)
class TemporaryImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_dt', 'updated_dt')
