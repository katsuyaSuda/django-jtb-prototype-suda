from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.ContentId)
class ContentIdAdmin(admin.ModelAdmin):
    pass

@admin.register(models.RequirementsInfometion)
class RequirementsInfometionAdmin(admin.ModelAdmin):
    pass
