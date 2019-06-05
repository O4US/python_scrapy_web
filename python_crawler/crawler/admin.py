from django.contrib import admin
from . import models
# Register your models here.
admin.site.register([models.Movies,models.Weathers,models.Phones,models.User])
