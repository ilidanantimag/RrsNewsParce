# Generated by Django 3.2.5 on 2021-07-23 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0004_alter_sources_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sources',
            name='slug',
        ),
    ]
