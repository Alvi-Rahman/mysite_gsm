# Generated by Django 3.0.4 on 2020-04-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0025_productwiseusercomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='meta_des',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='brandinfo',
            name='meta_des',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='brandinfo',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='meta_des',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='meta_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]