# Generated by Django 3.2.5 on 2021-07-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrs', '0009_alter_rrsfeeditems_image_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rrsfeeditems',
            name='pub_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='sources',
            name='lastBuildDate',
            field=models.DateTimeField(null=True),
        ),
    ]