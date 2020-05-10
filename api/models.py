from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Audio(models.Model):
    title: models.CharField(max_length=200)
    audioLink: models.CharField(max_length=500)
    isTranscribed: models.BooleanField(default=False)
    user:  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
