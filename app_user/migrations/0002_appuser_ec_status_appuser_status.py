# Generated by Django 4.0.6 on 2022-07-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='ec_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='appuser',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
