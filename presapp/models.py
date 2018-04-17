# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models
from django.db import connection
from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField



class Patient(models.Model):
    patientid = models.AutoField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    pyear = models.DecimalField(db_column='Pyear', max_digits=10, decimal_places=0, blank=True, null=True)  # Field
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    fname = models.TextField(db_column='FName', blank=True, null=True)  # Field name made lowercase.
    lname = models.TextField(db_column='LName', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    pamonth = models.TextField(db_column='PAMonth', blank=True, null=True)
    payear = models.TextField(db_column='PAYear', blank=True, null=True)
    padays = models.TextField(db_column='PADays', blank=True, null=True)
    sex = models.TextField(db_column='Sex', blank=True, null=True)
    rdate = models.DateTimeField(db_column='rDate', blank=True, null=True, default=datetime.now())
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    pin = models.TextField(db_column='Pin', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)
    cellular = models.TextField(db_column='Cellular', blank=True, null=True, max_length=10)
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.



    class Meta:

        db_table = 'Patient'


class presciptiontemplates(models.Model):
    templateid = models.AutoField(primary_key=True)
    template = RichTextField()
    draft = models.BooleanField(default=False)
    savedate = models.DateTimeField(default=datetime.now())
    patientid=models.IntegerField()
