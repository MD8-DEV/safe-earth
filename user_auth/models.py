from django.db import models
from django.contrib.auth.models import User

class User(User):
    carbon_footprint = models.CharField(max_length=10)


class Message(models.Model):
    text = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
