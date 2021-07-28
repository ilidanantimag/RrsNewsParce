# Generated by Django 3.2.5 on 2021-07-23 19:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sources',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=200, unique=True),
        ),
    ]
