from django.contrib import admin

from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ("company", "recommender", "post_date")


admin.site.register(Job, JobAdmin)