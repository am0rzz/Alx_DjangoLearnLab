from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class ModelAdmin(UserAdmin):
    pass
admin.site.register(UserProfile)
# admin.site.register(ModelAdmin)