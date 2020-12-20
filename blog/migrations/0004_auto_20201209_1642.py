# Generated by Django 3.1.4 on 2020-12-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201209_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_post',
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
