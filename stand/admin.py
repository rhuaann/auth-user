from django.contrib import admin

from . import models


# Register your models here.
class StandAdmin(admin.ModelAdmin):
    search_fields = ["localização", "valor"]
    readonly_fields = ["updated_by", "created_at"]

admin.site.register(models.Stand, StandAdmin)