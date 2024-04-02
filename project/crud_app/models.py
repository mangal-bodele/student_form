from django.db import models

class Student(models.Model):
    BLOOD = [('+ve O','O positive'),('-ve O','O negative'),('+ve A','A positive'),('-ve A','A negative'),('+ve B','B positive'),('-ve B','B negative'),('+ve AB','AB positive'),('-ve AB','AB negative')]
    GENDER =[('male','M'),('Female','F'),('Others','O')]
    roll = models.IntegerField(primary_key=True)
    fn = models.CharField(max_length=10)
    ln = models.CharField(max_length=10)
    address = models.CharField(max_length=20)
    institute = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=10, choices=BLOOD)
    gender = models.CharField(max_length=10,choices=GENDER)


