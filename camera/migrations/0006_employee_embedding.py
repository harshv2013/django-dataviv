# Generated by Django 3.1 on 2020-09-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0005_auto_20200910_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='embedding',
            field=models.BooleanField(default=False),
        ),
    ]