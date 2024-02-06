from django.db import models

# Create your models here.
#makemigrations - create Change and store in a file 
#migrate -apply the pending changes created by makemigrations

class Contact(models.Model):
    name= models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    

class Offline(models.Model):
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    zip=models.CharField(max_length=122)
    address=models.CharField(max_length=150)
    email1=models.CharField(max_length=122)

    def __str__(self):
        return self.fname
    

class Service(models.Model):
    icename=models.CharField(max_length=122)
    special_item=models.CharField(max_length=122)
    ice_quantity=models.CharField(max_length=122)
    delivery_type=models.CharField(max_length=120)
    delivery_area=models.CharField(max_length=120)

    def __str__(self):
        return self.delivery_type

