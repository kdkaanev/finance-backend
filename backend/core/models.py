from django.db import models

# Create your models here.
class Transactions(models.Model):
    avatar = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=60)