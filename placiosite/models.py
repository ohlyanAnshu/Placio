from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class City(models.Model):
    class Meta:
        verbose_name_plural = 'City'
    city = models.CharField(max_length=200)
   
    def __str__(self):
        return self.city 

class University(models.Model):
    class Meta:
        verbose_name_plural = 'University'
    university = models.CharField(max_length=500)

    def __str__(self):
        return self.university      

class PostYourReq(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)    
    area = models.CharField(max_length=200)
    budget = models.FloatField()
    roomtype_choices = (
            ('private', 'Private Room'),
            ('shared', 'Shared Room'),
        )
    roomtype = models.CharField(max_length=200, choices=roomtype_choices)
    comment = models.TextField()
    

    def __str__(self):
            return self.name
