from django.shortcuts import render
from . models import Message, Chatting
from . forms import messageForm

# Create your views here.

def chat(request):
    message = Message.objects.all()

    context = {'message':message}
    return render(request, 'chat/chat.html',context)

def messagechat(request,pk):
    chat = Chatting.objects.all()
    context = {'chat':chat}
    return render(request, 'chat/chatmessage.html',context)
