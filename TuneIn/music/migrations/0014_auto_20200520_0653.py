# Generated by Django 3.0.5 on 2020-05-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20200520_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='language',
            field=models.CharField(max_length=50),
        ),
    ]
