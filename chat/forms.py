from django.forms import ModelForm
from . models import Chatting


class messageForm(ModelForm):
    class Meta:
        model = Chatting
        fields = ('chat_message',)