# Generated by Django 3.0.5 on 2020-05-17 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200517_0631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('artist_name', models.CharField(max_length=100)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='music.Album')),
            ],
        ),
    ]
