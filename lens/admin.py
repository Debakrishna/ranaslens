from django.contrib import admin
from .models import Image, QueryForm
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "date"]

admin.site.register(QueryForm)
