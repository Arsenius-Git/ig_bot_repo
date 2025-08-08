from django.db import models

# Create your models here.

class IgModel(models.Model):
    message = models.TextField()
    sender = models.CharField(max_length=1000, blank=True, null=True)