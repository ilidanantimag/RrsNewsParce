# Generated by Django 3.2.5 on 2021-07-24 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0011_auto_20210724_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='rrsfeeditems',
            name='date2',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
