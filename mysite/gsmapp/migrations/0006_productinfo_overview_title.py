# Generated by Django 2.2.9 on 2020-03-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0005_auto_20200314_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='overview_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
