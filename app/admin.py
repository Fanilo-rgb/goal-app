from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Goal)
class Goal_admin(admin.ModelAdmin):
    list_display = ['description', "priority", "status", "created_date"]

admin.site.register(Category)
admin.site.register(Subcategory)
