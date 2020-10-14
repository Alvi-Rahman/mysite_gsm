# Generated by Django 2.2.9 on 2020-03-14 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0003_auto_20200314_1535'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LatestNews',
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='latest_news',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='blog_img',
            field=models.ImageField(blank=True, upload_to='blog'),
        ),
    ]
