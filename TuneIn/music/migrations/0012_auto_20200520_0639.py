# Generated by Django 3.0.5 on 2020-05-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_album_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]