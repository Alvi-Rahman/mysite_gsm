# Generated by Django 2.2.9 on 2020-03-17 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0009_productinfo_selfie_cam_type_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfo',
            name='battery_capacity_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='battery_technology_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='camera_photo_pixel_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='camera_video_pixel_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='chipset_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='display_resolution_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='display_size_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='ram_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='reviews_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='specifications_top',
            field=models.TextField(blank=True, null=True),
        ),
    ]
