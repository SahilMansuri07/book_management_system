from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=255,default='')
    email = models.EmailField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    
class Author(models.Model):
    name = models.CharField(max_length=255,default='')
    address = models.CharField(max_length=255,default='')
    
class Book(models.Model):
    name = models.CharField(max_length=255,default='')
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=timezone.now())
    isbn = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)