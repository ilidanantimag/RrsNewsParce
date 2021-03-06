# Generated by Django 3.2.5 on 2021-07-23 19:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0003_alter_sources_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sources',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, max_length=200, null=True, unique=True),
        ),
    ]
