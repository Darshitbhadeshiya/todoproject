from django.contrib import admin
from .models import todo

# Register your models here.

@admin.register(todo)
class blogadmin(admin.ModelAdmin):
    list_display=['id','Title','Created_at','Updated_at']
    ordering=['id']