from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    technology = models.CharField(max_length=30)
    product_manager = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    crated_at = models.DateTimeField(blank=True, null=True)
