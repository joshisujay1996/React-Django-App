# Generated by Django 2.2.4 on 2019-08-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='jobid',
            field=models.IntegerField(max_length=64, unique=True),
        ),
    ]
