# Generated by Django 3.0.4 on 2020-07-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0028_auto_20200711_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='img_alt_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='page_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brandinfo',
            name='img_alt_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='brandinfo',
            name='page_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='img_alt_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productinfo',
            name='page_title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productpricing',
            name='img_alt_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productthreedview',
            name='img_alt_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sliderinfo',
            name='img_alt_tag',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sliderinfo',
            name='page_title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
