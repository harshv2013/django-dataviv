# Generated by Django 3.1 on 2020-10-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camera', '0020_modelanalysis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelanalysis',
            name='updatedclasstype',
            field=models.CharField(choices=[('E', 'Employee'), ('C', 'Customer'), ('O', 'Other')], default=None, max_length=1, null=True),
        ),
    ]