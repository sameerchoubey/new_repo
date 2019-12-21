# Generated by Django 3.0.1 on 2019-12-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='main_db',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('video_title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
                ('thumbnail_url', models.CharField(max_length=200)),
                ('video_url', models.CharField(max_length=200)),
            ],
        ),
    ]
