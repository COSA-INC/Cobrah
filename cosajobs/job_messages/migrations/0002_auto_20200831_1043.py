# Generated by Django 3.0.8 on 2020-08-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='receiver',
            new_name='message_sender',
        ),
        migrations.AddField(
            model_name='messages',
            name='message_receiver',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
