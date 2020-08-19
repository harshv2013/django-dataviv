from django.db import models
from django.contrib.postgres.fields import ArrayField


class Student(models.Model):
    shop_name = models.CharField(max_length=200)
    shop_location = models.CharField(max_length=200)


class Organization(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    age = models.PositiveIntegerField()


class Store(models.Model):
    location = models.CharField(max_length=200)
    total_camera = models.IntegerField()
    outer_camera_channel_no = models.CharField(max_length=200)
    billing_camera_channel_no = models.CharField(max_length=200)
    camera_sequence = ArrayField(models.CharField(max_length=200), blank=True)
    organization = models.ForeignKey(
        Organization, related_name='stores', on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee, related_name='stores', on_delete=models.CASCADE)


class Analytic(models.Model):
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    store = models.ForeignKey(
        Store, related_name='analytics', on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization, related_name='analytics', on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee, related_name='analytics', on_delete=models.CASCADE)


class DailyLog(models.Model):
    total_in = models.IntegerField()
    total_out = models.IntegerField()
    store = models.ForeignKey(
        Store, related_name='dailylogs', on_delete=models.CASCADE)
    organization = models.ForeignKey(
        Organization, related_name='dailylogs', on_delete=models.CASCADE)




    




