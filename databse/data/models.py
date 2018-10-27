from django.db import models
class Employee(model.Model):
    eno=models.IntergerField()
    ename=models.CharField(max_length=30)
    esal=models.IntergerField()
    eaddr=models.CharField(max_length=30)
    def  __str__(self):
        return self.ename



# Create your models here.
