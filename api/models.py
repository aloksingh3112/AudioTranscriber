from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Audio(models.Model):
    title = models.CharField(max_length=200, null=True)
    audioLink = models.CharField(max_length=500, null=True)
    transcribedData = models.TextField(null=True)
    isTranscribed = models.BooleanField(default=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
