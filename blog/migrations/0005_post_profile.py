# Generated by Django 3.1.4 on 2020-12-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201209_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
