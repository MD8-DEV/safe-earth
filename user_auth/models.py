from django.db import models
from django.contrib.auth.models import User

class User(User):
    carbon_footprint = models.CharField(max_length=10)


class Room(models.Model):
    name = models.CharField(null=True, max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    text = models.TextField(null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("date",)
