# Generated by Django 3.1 on 2020-09-15 08:29

import camera.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0010_auto_20200914_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_media',
            field=models.FileField(default='', upload_to=camera.models.path_and_rename),
        ),
    ]
