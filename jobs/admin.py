from django.contrib import admin

# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'posted_at', 'is_active')
    list_filter = ('is_active', 'posted_at')
    search_fields = ('title', 'description', 'location')