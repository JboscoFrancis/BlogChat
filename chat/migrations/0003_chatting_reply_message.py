# Generated by Django 3.1.4 on 2020-12-18 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatting'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatting',
            name='reply_message',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
