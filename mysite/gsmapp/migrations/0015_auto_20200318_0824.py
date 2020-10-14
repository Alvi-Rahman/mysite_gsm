# Generated by Django 3.0.4 on 2020-03-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0014_auto_20200317_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='battery_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='battery_music_play',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='battery_talk_time',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='launch_announced',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
