# Generated by Django 2.0.3 on 2018-03-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library_app', '0006_auto_20180309_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file_path',
            field=models.TextField(blank=True),
        ),
    ]