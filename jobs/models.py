from django.db import models
from accounts.models import UserAccount

# Create your models here.
class Job(models.Model):
    # recommender
    recommender = models.ForeignKey(UserAccount, null=True, on_delete=models.SET_NULL)
    # company name
    company = models.CharField(max_length=255)
    # all jobs
    refer_scope_link = models.URLField(max_length=1023)
    # refer scope description
    refer_scope_description = models.CharField(max_length=511)
    # refer requirement
    refer_requirement = models.CharField(max_length=511)
    # applied users
    applied_users = models.JSONField(blank=True, null=True)
    
    # post date
    post_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"{self.company}"

    
