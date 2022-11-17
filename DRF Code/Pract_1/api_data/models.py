from django.db import models

class Employee(models.Model):

    eid = models.IntegerField()
    ename = models.CharField(max_length=20)
    eadd = models.CharField(max_length=200)
    esal = models.FloatField()

 
    def __str__(self):
        return self.ename