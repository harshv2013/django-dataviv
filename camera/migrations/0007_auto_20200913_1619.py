# Generated by Django 3.1 on 2020-09-13 16:19

import camera.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0006_employee_embedding'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUserb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testuser_media', models.FileField(upload_to='home/harsh/django-dataviv/embedding')),
            ],
        ),
        migrations.RemoveField(
            model_name='testuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testuser',
            name='testuser_media',
        ),
        migrations.AddField(
            model_name='testuser',
            name='media',
            field=models.FileField(default='', upload_to=camera.models.path_and_rename),
        ),
    ]