# Generated by Django 3.2.5 on 2021-07-23 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='Категория ленты', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('col', models.CharField(db_index=True, help_text='col', max_length=200)),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='RrsFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='Категория ленты', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, help_text='Категория ленты', max_length=200)),
                ('link', models.CharField(db_index=True, help_text='Сылка rrs', max_length=200)),
                ('categories', models.ManyToManyField(null=True, related_name='categories', to='rrs.Categories')),
            ],
            options={
                'verbose_name': 'Источники',
                'verbose_name_plural': 'Источники',
            },
        ),
        migrations.CreateModel(
            name='RrsFeedItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название статьи')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(verbose_name='Текст статьи')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('feed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='rrs.rrsfeed')),
            ],
        ),
    ]