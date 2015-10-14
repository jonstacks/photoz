from django.contrib import admin

from photos.models import TemporaryImage


@admin.register(TemporaryImage)
class TemporaryImageAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_dt'
    list_display = ('__str__', 'created_dt')
    readonly_fields = ('created_dt', 'updated_dt')
