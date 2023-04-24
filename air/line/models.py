from django.db import models

# Create your models here.

class contact(models.Model):
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email
    
class book_flight(models.Model):
    name = models.CharField(max_length=122)
    contact = models.CharField(max_length=122)
    frm = models.CharField(max_length=122)
    to = models.CharField(max_length=122)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class add_flight(models.Model):
    name = models.CharField(max_length=122)
    duration = models.CharField(max_length=122)
    frm = models.CharField(max_length=122)
    to = models.CharField(max_length=122)
    date = models.DateField()