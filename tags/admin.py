from django.contrib import admin

from . import models

# Register your models here.

admin.register(models.Tag)

admin.register(models.TaggedItem)