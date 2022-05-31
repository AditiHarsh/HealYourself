from django.db import models



# Create your models here.

class patient(models.Model):
    name= models.CharField(max_length=100)
    phone= models.BigIntegerField()
    email= models.EmailField(max_length=200)
    age= models.IntegerField()
    gender= models.CharField(max_length=10)
    doctor= models.CharField(max_length=200,default=None)
   
class doctor(models.Model):
    doctor_id=None
    dname= models.CharField(max_length=100)
    specialization= models.CharField(max_length=200)
    contact= models.BigIntegerField()
    address= models.CharField(max_length=300)
    timing= models.CharField(max_length=20)


   
