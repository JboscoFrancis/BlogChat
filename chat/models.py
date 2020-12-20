from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    message_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)


class Chatting(models.Model):
    chatting_to = models.ForeignKey(Message, blank=True, on_delete=models.CASCADE)
    chat_message = models.TextField(max_length=200, null=True)
    date_created = models.DateField(auto_now_add=True)
