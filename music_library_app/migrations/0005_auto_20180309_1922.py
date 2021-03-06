# Generated by Django 2.0.3 on 2018-03-09 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_library_app', '0004_auto_20180309_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='music_library_app.Album'),
        ),
    ]
