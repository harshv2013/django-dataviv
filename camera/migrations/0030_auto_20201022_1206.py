# Generated by Django 3.1 on 2020-10-22 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0029_auto_20201022_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storemanager',
            name='store',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='storemanager', to='camera.store'),
        ),
    ]