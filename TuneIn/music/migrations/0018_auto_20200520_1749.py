# Generated by Django 3.0.5 on 2020-05-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20200520_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(blank=True, default='music/images/default.png', null=True, upload_to=''),
        ),
    ]
