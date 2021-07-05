from django.contrib import admin

from .models import blog


@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['user','title','content','photo']