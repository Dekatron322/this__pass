# Generated by Django 4.0.6 on 2022-07-24 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ThisPass', max_length=150)),
                ('tag_title', models.CharField(default='Sale', max_length=150)),
                ('color', models.CharField(default='ThisPass Black Card', max_length=150)),
                ('image', models.FileField(blank=True, default='default_files/default_face.jpg', upload_to='card/image/')),
                ('quantity', models.IntegerField(default=1)),
                ('threshold', models.IntegerField(blank=True, default=1, null=True)),
                ('price', models.IntegerField(default=1)),
                ('shipping_charge', models.FloatField(default=1)),
                ('delivery_info', models.CharField(default='none', max_length=150)),
                ('slug', models.SlugField(default='myslug', unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]