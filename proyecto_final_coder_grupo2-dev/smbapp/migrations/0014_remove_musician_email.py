# Generated by Django 4.1.2 on 2022-12-15 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smbapp', '0013_musician_bio_link_musician_email_alter_post_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musician',
            name='email',
        ),
    ]