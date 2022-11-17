from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.FloatField()
    add = models.CharField(max_length=500)
