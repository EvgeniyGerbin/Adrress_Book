from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):

    first_name = models.CharField("Name", max_length=32, null=False, blank=False)
    last_name = models.CharField("Surname", max_length=32, null=False, blank=False)
    email = models.EmailField("Email")
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    url = models.URLField(blank=True, null=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)
    img = models.ImageField(upload_to='media/', blank=True, null=True)






