from django.urls import path
from . import views 


urlpatterns = [
    path('', views.chat, name = 'chat'),
    path('messages/<int:pk>', views.messagechat, name = 'messagechat')
]