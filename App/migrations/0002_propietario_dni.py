# Generated by Django 4.0 on 2022-01-19 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='dni',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
