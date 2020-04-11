from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Survey(models.Model):
    user        = models.OneToOneField(User , on_delete=models.CASCADE)
    name        = models.CharField(max_length=200 ,blank=True)
    subject     = models.CharField(max_length=300 ,blank=True)

    def __str__(self):
        return self.name