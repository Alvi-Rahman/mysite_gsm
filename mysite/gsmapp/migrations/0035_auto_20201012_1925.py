# Generated by Django 2.2.9 on 2020-10-12 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gsmapp', '0034_auto_20201012_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpermalink',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gsmapp.ProductInfo'),
        ),
    ]