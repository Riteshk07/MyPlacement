from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your models here.
class Company(models.Model):
    name        = models.CharField(blank=True, max_length=100)
    desc        = models.TextField(max_length=200)
    link        = models.CharField(blank=True, max_length=200)
    icon_url    = models.CharField(blank=True, max_length=200)

    class Meta:
        ordering = ('id', )
        verbose_name_plural = 'Company'


class Saved_Company(models.Model):
    company_id  = models.ForeignKey(Company, on_delete=models.CASCADE)
    user_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    last_open   = models.DateTimeField(default=datetime.now,blank=True)

    class Meta:
        ordering = ('id', )
        verbose_name_plural = 'Saved_Company'


class Salary(models.Model):
    company_id  = models.ForeignKey(Company, on_delete=models.CASCADE)
    position    = models.CharField(blank=True, max_length=100)
    country     = models.CharField(blank=True, max_length=100)
    base        = models.PositiveIntegerField(default=0, null=False)
    bonus       = models.PositiveIntegerField(default=0, null=False)
    stock       = models.PositiveIntegerField(default=0, null=False)

    class Meta:
        ordering = ('id', )
        verbose_name_plural = 'Salary'

class New_Job(models.Model):
    company_id   = models.ForeignKey(Company, on_delete=models.CASCADE)
    position     = models.CharField(blank=True, max_length=100)
    job_id       = models.CharField(blank=True, max_length=100)
    location     = models.CharField(blank=True, max_length=100)
    link         = models.CharField(blank=True, max_length=500)
    date_updated = models.DateTimeField(default=datetime.now,blank=True)

    class Meta:
        ordering = ('id', )
        verbose_name_plural = 'New_Jobs'

class Saved_Job(models.Model):
    job_id      = models.ForeignKey(New_Job, on_delete=models.CASCADE)
    user_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    applied     = models.BooleanField(default=False)
    reffred     = models.BooleanField(default=False)
    rejected    = models.BooleanField(default=False)
    selected    = models.BooleanField(default=False)
    apply_date  = models.DateTimeField(default=datetime.now,blank=True)

    class Meta:
        ordering = ('id', )
        verbose_name_plural = 'Saved_Job'


        