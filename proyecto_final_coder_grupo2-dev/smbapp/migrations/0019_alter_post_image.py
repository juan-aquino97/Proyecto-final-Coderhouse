# Generated by Django 4.1.2 on 2022-12-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smbapp', '0018_alter_musician_image_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]