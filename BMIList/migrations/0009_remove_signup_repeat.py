# Generated by Django 3.1.6 on 2021-08-09 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BMIList', '0008_auto_20210809_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='repeat',
        ),
    ]
