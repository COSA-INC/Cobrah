# Generated by Django 3.0.8 on 2020-08-28 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_delete_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job_pic',
            new_name='job_image',
        ),
    ]