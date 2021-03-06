# Generated by Django 2.2.9 on 2020-03-14 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150, unique=True)),
                ('blog_details', models.TextField()),
                ('blog_img', models.ImageField(blank=True, upload_to='slider')),
                ('ordering', models.IntegerField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BrandInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=150, unique=True)),
                ('brand_img', models.ImageField(blank=True, upload_to='brand')),
                ('ordering', models.IntegerField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='LatestNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=250)),
                ('product_img', models.ImageField(blank=True, upload_to='latest_news')),
                ('news_details', models.TextField()),
                ('ordering', models.IntegerField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SliderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_name', models.CharField(max_length=150, unique=True)),
                ('slider_details', models.TextField()),
                ('slider_img', models.ImageField(blank=True, upload_to='slider')),
                ('ordering', models.IntegerField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('product_img', models.ImageField(blank=True, upload_to='product_img')),
                ('network_technology', models.CharField(blank=True, max_length=250, null=True)),
                ('network_2g_bands', models.CharField(blank=True, max_length=250, null=True)),
                ('network_3g_bands', models.CharField(blank=True, max_length=250, null=True)),
                ('network_4g_bands', models.CharField(blank=True, max_length=250, null=True)),
                ('network_5g_bands', models.CharField(blank=True, max_length=250, null=True)),
                ('network_speed', models.CharField(blank=True, max_length=250, null=True)),
                ('launch_announced', models.DateTimeField(blank=True, null=True)),
                ('launch_status', models.CharField(blank=True, max_length=250, null=True)),
                ('body_dimensions', models.CharField(blank=True, max_length=250, null=True)),
                ('body_weight', models.CharField(blank=True, max_length=250, null=True)),
                ('body_build', models.CharField(blank=True, max_length=250, null=True)),
                ('body_sim', models.CharField(blank=True, max_length=250, null=True)),
                ('display_type', models.CharField(blank=True, max_length=250, null=True)),
                ('display_size', models.CharField(blank=True, max_length=250, null=True)),
                ('display_resolution', models.CharField(blank=True, max_length=250, null=True)),
                ('display_protection', models.CharField(blank=True, max_length=250, null=True)),
                ('platform_os', models.CharField(blank=True, max_length=250, null=True)),
                ('platform_chipset', models.CharField(blank=True, max_length=250, null=True)),
                ('platform_cpu', models.CharField(blank=True, max_length=250, null=True)),
                ('platform_gpu', models.CharField(blank=True, max_length=250, null=True)),
                ('memory_card_slot', models.CharField(blank=True, max_length=250, null=True)),
                ('memory_internal', models.CharField(blank=True, max_length=250, null=True)),
                ('main_camera_type', models.CharField(blank=True, max_length=250, null=True)),
                ('main_camera_features', models.CharField(blank=True, max_length=150, null=True)),
                ('main_camera_video', models.CharField(blank=True, max_length=250, null=True)),
                ('selfie_camera_type', models.CharField(blank=True, max_length=150, null=True)),
                ('selfie_camera_features', models.CharField(blank=True, max_length=150, null=True)),
                ('selfie_camera_video', models.CharField(blank=True, max_length=150, null=True)),
                ('sound_loudspeaker', models.BooleanField(default=False)),
                ('sound_3_5mm_jack', models.BooleanField(default=False)),
                ('comms_wlan', models.CharField(blank=True, max_length=250, null=True)),
                ('comms_bluetooth', models.CharField(blank=True, max_length=250, null=True)),
                ('comms_gps', models.CharField(blank=True, max_length=250, null=True)),
                ('comms_nfc', models.CharField(blank=True, max_length=250, null=True)),
                ('comms_radio', models.CharField(blank=True, max_length=250, null=True)),
                ('comms_usb', models.CharField(blank=True, max_length=250, null=True)),
                ('features_sensors', models.CharField(blank=True, max_length=250, null=True)),
                ('battery_type', models.CharField(blank=True, max_length=250, null=True)),
                ('battery_charging', models.CharField(blank=True, max_length=250, null=True)),
                ('misc_colors', models.CharField(blank=True, max_length=250, null=True)),
                ('misc_models', models.CharField(blank=True, max_length=250, null=True)),
                ('misc_sar', models.CharField(blank=True, max_length=250, null=True)),
                ('misc_sar_eu', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.CharField(blank=True, max_length=250, null=True)),
                ('bd_price', models.CharField(blank=True, max_length=250, null=True)),
                ('disclaimer', models.CharField(blank=True, max_length=250, null=True)),
                ('total_view', models.IntegerField(default=0)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('ordering', models.IntegerField(default=0)),
                ('latest_device', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gsmapp.BrandInfo')),
            ],
        ),
    ]
