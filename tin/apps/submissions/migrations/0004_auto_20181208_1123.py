# Generated by Django 2.1.4 on 2018-12-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_submission_filename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='points_received',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
