from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class  OurFleet(models.Model):
    vehicle_type  =  models.CharField(max_length=100)
    updatedAt  =  models.DateField

    class Meta:
        verbose_name_plural  =  "Our Fleet" 

    def  __str__(self):
        return  self.vehicle_type

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
    ('DR', 'Dr'),
    ('PROF', 'Prof'),
    ('ENG', 'Eng'),
    ('HON', 'Hon'),
]
GENDER_CHOICES = [
    ('MALE' , 'Male'),
    ('FEMALE', 'Female'),
    ('OTHER', 'Other')
]
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=6 ,choices=TITLE_CHOICES)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.CharField(max_length=20)
    phone_number = PhoneNumberField()
    createdAt = models.DateField(blank=True, null=True )

    class Meta:
        verbose_name_plural  =  "Customers list" 

    def  __str__(self):
        return  f"{self.first_name},{self.last_name}"

class Bookings(models.Model):
    customer_title = models.CharField(max_length=6 ,choices=TITLE_CHOICES)
    customer_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    vehicle_type  =  models.CharField(max_length=100)
    pick_up_Location = models.CharField(max_length=100)
    drop_off_Location = models.CharField(max_length=100)
    pick_up_time = models.DateField(blank=True, null=True)
    drop_off_time = models.DateField(blank=True, null=True)
    bookedOn = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural  =  "View Bookings sent via website" 
        ordering= ("pick_up_time",)
    def  __str__(self):
        return  f"{self.customer_title}, {self.customer_name}"

class CustomersMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,blank=True,unique=True)
    subject = models.CharField(max_length=255,blank=True)
    body = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural  =  "Customers Message Sent via website" 
    
    def  __str__(self):
        return  self.name
