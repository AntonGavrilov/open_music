# Generated by Django 2.0.3 on 2018-03-08 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='gener',
            options={'ordering': ('name',)},
        ),
    ]
