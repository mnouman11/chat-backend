from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    # Add additional fields here
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Add any other fields or custom methods if needed
    def __str__(self):
        return self.username
    
class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    members = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

class Message(models.Model):
    chat = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(MyUser, related_name='sender', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'