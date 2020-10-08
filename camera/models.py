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


def path_and_rename2(instance, filename):
    upload_to = 'Attendence_data'
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

#########################################


# class TestUserb(models.Model):
#     name = models.CharField(max_length=200)
#     testuser_media = models.FileField(upload_to='home/harsh/django-dataviv/embedding')

class TestUser(models.Model):
    media = models.FileField(upload_to=path_and_rename,default = "")

    
#######################################


class Store(models.Model):
    location = models.CharField(max_length=200)
    total_camera = models.IntegerField()
    outer_camera_channel_no = models.CharField(max_length=200)
    billing_camera_channel_no = models.CharField(max_length=200)
    camera_sequence = ArrayField(models.CharField(max_length=200), blank=True)
    organization = models.ForeignKey(
        Organization, related_name='stores', on_delete=models.DO_NOTHING)


class StoreManager(User):
    store = models.OneToOneField(
        Store, on_delete=models.DO_NOTHING, default=None)


# class Employee(models.Model):
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     name = models.CharField(max_length=200)
#     email = models.EmailField(default="")
#     contact = models.CharField(max_length=200, default="")
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     age = models.PositiveIntegerField()
#     address = models.CharField(max_length=200, default="")
#     # employee_media = models.FileField(upload_to='Face_data')
#     # employee_media = models.FileField(upload_to=path_and_rename)
#     embedding = models.BooleanField(default=False)
#     store = models.ForeignKey(
#         Store, related_name='employees', on_delete=models.DO_NOTHING)


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(default="")
    contact = models.CharField(max_length=200, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=200, default="")
    # employee_media = models.FileField(upload_to='Face_data')
    employee_media = models.FileField(upload_to=path_and_rename,default="")
    embedding = models.BooleanField(default=False)
    store = models.ForeignKey(
        Store, related_name='employees', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey('User', related_name='employees', on_delete=models.DO_NOTHING)

# import pytz
# tz = pytz.timezone("Asia/Calcutta")
# from datetime import datetime as dt
# # import datetime.datetime as dt
# dt.now(tz)


class Attendence(models.Model):
    employee = models.ForeignKey(
        Employee, related_name='attendences', on_delete=models.DO_NOTHING, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class AttendenceMedia(models.Model):
    attendence_media = models.FileField(upload_to=path_and_rename2)


class EmployeeMedia(models.Model):
    employee_media = models.FileField(upload_to=path_and_rename)
    employee = models.ForeignKey(
        Employee, related_name='employeemedias', on_delete=models.DO_NOTHING, default=None)


class Analytic(models.Model):
    in_time = models.DateTimeField()
    out_time = models.DateTimeField()
    store_heat_map = models.FileField(upload_to=path_and_rename, default=None)
    store_hot_zone = models.FileField(upload_to=path_and_rename, default=None)
    # store = models.ForeignKey(
    #     Store, related_name='analytics', on_delete=models.CASCADE)
    # organization = models.ForeignKey(
    #     Organization, related_name='analytics', on_delete=models.CASCADE)
    employee = models.ForeignKey(
        Employee, related_name='analytics', on_delete=models.DO_NOTHING, default=None)


class AnalyticDisplay(models.Model):
    store_heat_map = models.ImageField(upload_to=path_and_rename)
    store_hot_zone = models.ImageField(upload_to=path_and_rename)
    gender = models.ImageField(upload_to=path_and_rename)
    age = models.ImageField(upload_to=path_and_rename)
    duration_of_visit = models.ImageField(upload_to=path_and_rename)
    no_of_purchasing_visit = models.IntegerField()
    no_of_missed_customers = models.IntegerField()
    days_with_most_walkings = models.ImageField(upload_to=path_and_rename)
    average_employee_count = models.ImageField(upload_to=path_and_rename)
    average_line_length = models.ImageField(upload_to=path_and_rename)
    time_analysis = models.ImageField(upload_to=path_and_rename)


class TotalDisplay(models.Model):
    total_walkings = models.IntegerField()
    clients = models.CharField(max_length=200)
    customer_flow = models.ImageField(upload_to=path_and_rename)
    number_of_family_member = models.IntegerField()
    client_gender = models.CharField(max_length=200)
    client_age = models.IntegerField()
    client_purchase_amount = models.FloatField()
    client_previous_visit_time = models.DateTimeField()
    client_visits_this_month = models.IntegerField()


class DailyLog(models.Model):
    total_in = models.IntegerField()
    total_out = models.IntegerField()
    store = models.ForeignKey(
        Store, related_name='dailylogs', on_delete=models.DO_NOTHING)
    # organization = models.ForeignKey(
    #     Organization, related_name='dailylogs', on_delete=models.CASCADE)


class Client(models.Model):
    client_name = models.CharField(max_length=200)
    entry_time = models.TimeField(default='12:34:56.000000')
    exit_time = models.TimeField(default='13:34:56.000000')
    customer_flow = models.ImageField(upload_to=path_and_rename)
    number_of_family_member = models.IntegerField()
    client_gender = models.CharField(max_length=200)
    client_age = models.IntegerField()
    client_purchase_amount = models.FloatField()
    client_previous_visit_time = models.DateTimeField(auto_now=True)
    client_visits_this_month = models.IntegerField()


class AnalyticEntry(models.Model):
    AvgMaleCount = models.IntegerField()
    AvgFemaleCount = models.IntegerField()
    Ageunder18 = models.IntegerField()
    Age18to24 = models.IntegerField()
    Age25to34 = models.IntegerField()
    Age35to44 = models.IntegerField()
    Age45to54 = models.IntegerField()
    Age55to64 = models.IntegerField()
    Age65above = models.IntegerField()
    Totalin = models.IntegerField()
    Totalout = models.IntegerField()
    AvgMissedcustomer = models.IntegerField()
    AvgPurchasedvisit = models.IntegerField()
    Avglinelength = models.IntegerField()
    DateTime = models.DateTimeField(auto_now=True)
    store = models.ForeignKey(
        Store, related_name='analyticentrys', on_delete=models.DO_NOTHING)


class Analysis1(models.Model):
    avg_male_count = models.PositiveIntegerField()
    avg_female_count = models.PositiveIntegerField()
    age_child = models.PositiveIntegerField()
    age_teenge = models.PositiveIntegerField()
    age_adult = models.PositiveIntegerField()
    age_old = models.PositiveIntegerField()
    total_in = models.PositiveIntegerField()
    total_out = models.PositiveIntegerField()
    customer_walkin = models.PositiveIntegerField()
    timestamp = models.DateTimeField()
    store = models.ForeignKey(
        Store, related_name='analysis1s', on_delete=models.DO_NOTHING)


class Analysis2(models.Model):
    avg_purchased_visit = models.PositiveIntegerField()
    avg_linelength = models.PositiveIntegerField()
    timestamp = models.DateTimeField()
    store = models.ForeignKey(
        Store, related_name='analysis2s', on_delete=models.DO_NOTHING)


class ModelAnalysis(models.Model):
    CLASSTYPE_CHOICES = (
        ('E', 'Employee'),
        ('C', 'Customer'),
        ('O', 'Other')
    )
    img_url = models.TextField()
    timestamp = models.DateTimeField()
    classtype = models.CharField(max_length=1, default=None)
    updatedclasstype = models.CharField(max_length=1, choices=CLASSTYPE_CHOICES, null=True, default=None)
    flag = models.BooleanField(default=False)
    store = models.ForeignKey(
        Store, related_name='modelanalysiss', on_delete=models.DO_NOTHING)
    
