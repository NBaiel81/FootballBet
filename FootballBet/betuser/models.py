from django.contrib.auth.models import User
from django.db import models

class BetUser(models.Model):
    full_name=models.CharField(max_length=40)
    country=models.CharField(max_length=20)
    wallet=models.PositiveIntegerField(default=0)
    age=models.PositiveIntegerField()
    email=models.CharField(null=True,blank=True,max_length=100)
    phone=models.PositiveIntegerField(null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.full_name

