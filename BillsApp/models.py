from __future__ import unicode_literals
from django.db import models
import pandas as pd
import random

# , on_delete=models.CASCADE
class UserInfo(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    sex=models.CharField(max_length=30)
    age=models.CharField(max_length=30)


# Create your models here.
class OnesBills(models.Model):
    time = models.CharField(max_length=30)
    money = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    mood = models.CharField(max_length=30)
    host = models.ForeignKey("UserInfo", on_delete=models.CASCADE)




