from django.db import models
from django_countries.fields import CountryField
from django.contrib import auth
class User(auth.models.User,auth.models.PermissionsMixin):
    fullname=models.CharField(max_length=255)
    country=CountryField()
    def __str__(self):
        return "@{}".format(self.username)

# class UserProfile(models.Model):
#     fullname=models.CharField(max_length=255)
#     username=models.CharField(max_length=255,unique=True)
#     email=models.EmailField(unique=True)
#     country=CountryField()
#     password= models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.fullname
#     def save(self):
#         self.save()
