from datetime import date
from email.headerregistry import Address
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import AutoField, EmailField
from django.contrib.auth.base_user import BaseUserManager

class User(models.Model):
    fname = models.CharField(max_length=20, null=True)
    lname = models.CharField(max_length=20, null=True)
    Uname = models.CharField(max_length=20, null=True)
    Pass = models.CharField(max_length=20, null=True)
    email = models.EmailField()

    class meta:
        db_table = 'user'
class ResBook(models.Model):
    res_number = models.IntegerField()
    Name = models.CharField(max_length=20, null=True)
    Address = models.CharField(max_length=20, null=True)
    tel_Number = models.CharField(max_length=20, null=True)
    room_number = models.CharField(max_length=20, null=True)
    date = models.DateField(max_length=20, null=True)
    time = models.CharField(max_length=20, null=True)

class Room(models.Model):
    room_number = models.CharField(max_length=20, primary_key = True)
    room_type = models.CharField(max_length=20, null=True)
    no_guest = models.CharField(max_length=20, null=True)

    class meta:
        db_table = 'tblRooms'