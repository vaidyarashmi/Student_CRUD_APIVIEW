from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no=models.IntegerField()
    name=models.CharField(max_length=64)
    address=models.CharField(max_length=64)
    mobile_number=models.IntegerField()
    marks=models.FloatField()