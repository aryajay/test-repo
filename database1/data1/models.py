from django.db import models
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=30)
    def  __str__(self):
        return self.ename

# Create your models here.
