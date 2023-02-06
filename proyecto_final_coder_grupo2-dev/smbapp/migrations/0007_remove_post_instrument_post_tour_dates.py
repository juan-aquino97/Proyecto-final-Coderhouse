# Generated by Django 4.1.2 on 2022-12-13 02:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('smbapp', '0006_alter_instrument_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='instrument',
        ),
        migrations.AddField(
            model_name='post',
            name='tour_dates',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]