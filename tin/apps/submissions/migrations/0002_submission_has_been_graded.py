# Generated by Django 2.1.4 on 2018-12-06 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='has_been_graded',
            field=models.BooleanField(default=False),
        ),
    ]
