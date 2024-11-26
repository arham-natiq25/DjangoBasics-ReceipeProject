from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    img = models.ImageField()
    file  = models.FileField()
    

class Car(models.Model):
    car_name = models.CharField(max_length=250)
    speed = models.IntegerField();    