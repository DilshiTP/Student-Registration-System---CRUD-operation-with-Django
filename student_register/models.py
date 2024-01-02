from django.db import models

# Create your models here.

class Department(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    index_number = models.CharField(max_length=10)
    mobile = models.CharField(max_length=15)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)