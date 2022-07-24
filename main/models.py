import email
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class OrderModel(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class WorkersModel(models.Model):
    firts_name =models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.last_name
    
class Workerscome(models.Model):
    date = models.DateField()
    arrival_time = models.TimeField()
    leave_time = models.TimeField()
    
    def __str__(self):
        return self.date


