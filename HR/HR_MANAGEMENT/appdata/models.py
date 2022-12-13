from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    addr = models.TextField()
    city = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=12)
    department = models.CharField(max_length=50)
    sal = models.FloatField()
    dob = models.DateField()

    def __str__(self):
        return self.name

class TODO(models.Model):

    work_sheet = models.TextField()
    date = models.DateTimeField()
