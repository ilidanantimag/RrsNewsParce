# Generated by Django 3.2.5 on 2021-07-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0015_alter_rrsfeeditems_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='rrsfeeditems',
            name='data_time',
            field=models.DateTimeField(null=True),
        ),
    ]