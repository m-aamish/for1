from django.db import models

# Create your models here.

class customer(models.Model):
    cusid=models.CharField(max_length=20)
    firstitem=models.CharField(max_length=50)
    date=models.CharField(max_length=20)
    purchase=models.IntegerField()