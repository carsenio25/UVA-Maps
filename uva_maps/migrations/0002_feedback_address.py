# Generated by Django 4.2.5 on 2023-11-08 03:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("uva_maps", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="address",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]