from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'Face_data'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class User(AbstractUser):
    pass


class Store(models.Model):
    location = models.CharField(max_length=200)
    total_camera = models.IntegerField()
    outer_camera_channel_no = models.CharField(max_length=200)
    billing_camera_channel_no = models.CharField(max_length=200)
    camera_sequence = ArrayField(models.CharField(max_length=200), blank=True)
    organization = models.ForeignKey(
        Organization, related_name='stores', on_delete=models.DO_NOTHING)


class StoreManager(User):
    store = models.OneToOneField(Store, on_delete=models.DO_NOTHING, default=None)


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    # employee_media = models.FileField(upload_to='Face_data')
    employee_media = models.FileField(upload_to=path_and_rename)
    store = models.ForeignKey(
        Store, related_name='employees', on_delete=models.DO_NOTHING)

class Analytic(models.Model):
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    # store = models.ForeignKey(
    #     Store, related_name='analytics', on_delete=models.CASCADE)
    # organization = models.ForeignKey(
    #     Organization, related_name='analytics', on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee, related_name='analytics', on_delete=models.DO_NOTHING)


class DailyLog(models.Model):
    total_in = models.IntegerField()
    total_out = models.IntegerField()
    store = models.ForeignKey(
        Store, related_name='dailylogs', on_delete=models.DO_NOTHING)
    # organization = models.ForeignKey(
    #     Organization, related_name='dailylogs', on_delete=models.CASCADE)

