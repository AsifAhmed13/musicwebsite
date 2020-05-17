# Generated by Django 3.0.5 on 2020-05-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=50)),
                ('artist_name', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('album_logo', models.CharField(max_length=200)),
            ],
        ),
    ]