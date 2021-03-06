# Generated by Django 3.1.4 on 2020-12-18 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chatting_reply_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatting',
            old_name='reply_message',
            new_name='chat_message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.AlterField(
            model_name='chatting',
            name='chatting_to',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='chat.message'),
        ),
    ]
